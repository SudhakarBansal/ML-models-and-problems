# Turn detection — all approaches considered

The approaches I evaluated for end-of-utterance detection (endpointing) in a voice-agent setting, and the reasoning behind which two I built.

For each approach: what it is, why I'm picking or skipping it, and when it would be the right call. The "why skipping" reasons are technical, not "takes too much time."

## 1. Energy-based silence detection

**What it is.** Look at the audio's amplitude (loudness) directly. If amplitude < some threshold for X ms, mark as silence. No ML at all — just signal processing.

**Why I'm skipping.** Too fragile. Background noise (fans, traffic, the person's own breathing) trips it. A soft speaker looks like silence even when they're talking. A loud noise looks like speech even when no one is. Doesn't handle real-world conditions. It's also pure signal processing — there's no modelling to reason about, which is the part of the problem I actually wanted to dig into.

**When it would be right.** Studio recording with one loud, clear speaker and zero background noise. Almost no real situation matches this.

## 2. WebRTC VAD + silence threshold

**What it is.** WebRTC VAD is a 2010-era voice activity detector from Google's WebRTC project (used in video calling). It uses hand-crafted features — energy in different frequency bands, spectral shape — and a small classifier to decide speech vs silence per frame. Then add a silence threshold rule on top: silence > X ms = "user done."

**Why I'm skipping (vs Silero).** WebRTC VAD was designed for video conferencing — its job there is to compress silence in audio transmission, so it tolerates a lot of false positives ("this might be speech"). It struggles with soft speakers, accented English, and audio with music or background noise. Silero is a modern neural network trained on much more diverse data, including speech in noisy conditions and many accents. Silero is also better at handling Indian English specifically. In 2026, choosing WebRTC VAD over a stronger, freely available modern model would be hard to justify.

**When it would be right.** Extremely low compute environments — a tiny embedded chip where you can't run even a small neural network. Also when latency requirements are sub-10ms. Not our case.

## 3. Silero VAD + silence threshold (CHOSEN — baseline)

**What it is.** Silero VAD is a small, modern, pretrained neural network. Takes audio in 30ms frames, outputs probability of "speech is happening" per frame. Threshold the probability (e.g., > 0.5 = speech). Glue consecutive speech frames into segments. Then add the silence threshold rule on top: if the silence between two speech segments is longer than X ms, predict "user done."

**Why I'm picking this.** It's the cleanest, modern baseline. Most production voice systems started here in 2022-2024 before moving to smarter approaches. Building this version lets me show the failure mode of pure silence-based endpointing on natural speech (people pause mid-sentence) and explain WHY moving to a smarter approach is necessary.

## 4. Pure semantic endpointing (no VAD, ASR continuously)

**What it is.** Skip VAD entirely. Send all audio to ASR continuously. Get a streaming transcript. The LLM (or a rule) watches the transcript and decides "user is done" purely from the words — never from acoustic silence.

**Why I'm skipping.** Three problems:
- ASR is much more compute-heavy than VAD. Running ASR on every frame, including the long silent stretches in conversations, wastes a lot of compute.
- You lose the cheap acoustic gate. The two-stage design (VAD first, ASR + LLM only on candidates) is what makes the smart approach affordable. Pure semantic loses that.
- Latency. ASR has its own latency (often hundreds of ms). If you're running it continuously, you're paying that latency on every decision, not just on candidate moments.

**When it would be right.** Research setting with unlimited compute. Or when audio is so noisy that VAD is unreliable but ASR can still pull words out (rare). Some research papers explore this for academic interest.

## 5. VAD + ASR + LLM (CHOSEN — smart approach)

**What it is.** Two-stage. VAD finds candidate "maybe done" moments cheaply. For each candidate, run ASR on audio so far → get transcript. Send transcript to an LLM and ask for a **3-class label**: `finished` / `unfinished` / `wait`.

- **finished** — user has completed their thought, agent can respond now.
- **unfinished** — user paused mid-sentence and is still speaking (e.g., "I want to book a flight to... [pause]... Bangalore for Tuesday"). Keep listening.
- **wait** — user explicitly told the agent to hold ("wait", "hold on", "don't respond yet"). Agent must stay silent even if the sentence is grammatically complete.

Binary done/not-done misses the `wait` class entirely. A user saying "wait, let me think" sounds like a complete sentence acoustically and looks like one semantically — but responding there would be a user-experience failure. Three classes handle this cleanly.

**LLM prompt (revised):**
```
User is talking to a voice assistant. Classify the transcript below as one of:
- "finished": user has completed their thought and expects a response
- "unfinished": user paused mid-sentence and is still speaking
- "wait": user explicitly asked the agent not to respond yet

Reply with exactly one word: finished, unfinished, or wait.

Transcript: {transcript}
```

**Why I'm picking this.** It's what production voice agents (Vapi, LiveKit, OpenAI Realtime) actually do in 2026. Two-stage design is well-motivated: cheap acoustic filter first, expensive semantic check second. The 3-class output is validated by TEN (see approach #11) — a production system that ships exactly this taxonomy. Lets me compare against approach #3 to show a clear improvement. It also surfaces real tradeoffs worth analysing — latency from the LLM, cost per check, ASR accuracy, 3-class vs binary.

**Production upgrade path (if this approach had to scale).** In this project the LLM call is a general-purpose model (GPT/Claude). That works for a prototype but has two problems at production scale: (1) latency — a general LLM adds 300-800ms per gap, which compounds across every silence in every conversation; (2) cost — an API call per gap is expensive at millions of conversations/day.

The production path is to **replace the general LLM with a specialized small classifier** — essentially what TEN (approach #11) is. Fine-tune a smaller model (DistilBERT-level, ~100M params, or a quantized Qwen2.5-3B) specifically on the 3-class task using labeled conversation data. Inference drops to ~50ms. Cost drops to near-zero (runs on your own GPU). Accuracy improves because the model is trained on your exact distribution.

The prototype (general LLM) validates that the semantic check adds real value over VAD-alone. Once validated, you replace the LLM with a specialist. That's the standard ML product path: LLM prototype → fine-tuned specialist, and it's the natural next engineering step here.

## 6. Acoustic prosody features

**What it is.** Extract features that describe HOW the person is speaking: pitch (F0) trajectory, energy, speech rate, pause duration, falling vs rising intonation. Train a classifier on labeled data: "this prosody pattern means end of sentence" vs "this prosody pattern means mid-sentence pause."

The intuition: humans don't just stop talking — they often signal it with falling pitch, slower speech rate, and a deliberate pause. Prosody captures this.

**Why I'm skipping.** Needs a labeled training dataset. Hundreds to thousands of audio clips, each labeled with EoU vs mid-sentence at every silence point. We don't have that, and creating it is a separate multi-week project on its own. Also, prosody alone isn't usually enough to beat semantic + acoustic combined — it's most useful as ONE signal in a multimodal system (which is approach #8).

**When it would be right.** Research labs with curated speech datasets like Switchboard or Callhome that have prosodic annotations. Also good as one input into a larger system. Not as the standalone primary approach.

## 7. Specialized end-of-utterance models (Vapi / LiveKit / proprietary)

**What it is.** Closed-source or proprietary models specifically trained for endpointing. Vapi has one called "smart endpointing." LiveKit has a similar one. They typically combine acoustic + semantic + prosody internally and have been trained on millions of conversations.

**Why I'm skipping.** They're closed-source. Even if I called their API, I couldn't explain WHY they decide one way or another internally — and the whole point of this project is to understand and reason about the endpointing tradeoffs, not to call a black-box endpoint. Also, most of these are paid APIs.

**When it would be right.** When building a real production voice agent at a company that pays for them and doesn't need to reason about the internals.

## 8. Multimodal (acoustic + semantic + prosody combined)

**What it is.** Combine approach #5 (VAD + ASR + LLM, the semantic + acoustic side) with approach #6 (prosody features) into one system. Use all three signals to decide.

**Why I'm skipping.** Same blocker as #6 — the prosody side needs labeled training data to be useful, and we don't have it. Also more complex pipeline, harder to write up clearly. Adding multimodal without strong signal that prosody specifically helps would feel like piling on.

**When it would be right.** Production system at a voice AI company with both labeled data and engineering resources. Current state-of-the-art research direction, and a natural "next step" beyond this project.

## 9. Adaptive threshold

**What it is.** Track this specific speaker's average pause length over the conversation so far. Adjust the silence threshold dynamically — slow speakers get a longer threshold (don't cut them off), fast speakers get a shorter one (don't make them wait).

**Why I'm skipping (as primary approach).** This is a small enhancement on top of approaches #3 or #5, not a fundamentally different one. It changes ONE parameter dynamically. Doesn't solve the underlying problem (silence-only endpointing is still fundamentally wrong about mid-sentence pauses, for any threshold setting).

**When it would be right.** As an enhancement layer on top of any other approach in production. Common in real systems — a small win you could stack on top of the chosen approach.

## 10. End-to-end neural endpointing

**What it is.** Train a single neural network on raw audio (or a mix of audio + text features), output a probability of "user is done" at each timestep. No pipeline — one model does everything.

**Why I'm skipping.** Two reasons:
- Needs a LOT of labeled training data. Probably thousands of hours of conversation audio with EoU annotations at every silence point. We don't have that.
- Less interpretable. "The model said so" gives me nothing to reason about. With a pipeline (VAD + ASR + LLM), I can explain each stage and reason about each one's failure modes. With an end-to-end model, debugging requires looking at attention weights or activations — much harder to reason about clearly.

**When it would be right.** At a voice AI company sitting on millions of hours of conversation logs. Some recent research papers do this. Not a 1-week solo project, and not the right call when reasoning depth is the deliverable.

## 11. Fine-tuned LLM for endpointing — TEN framework (production reference)

**What it is.** TEN (by the TEN-framework project) is a Qwen2.5-7B model fine-tuned specifically for end-of-utterance detection. Takes a conversation transcript as input, outputs a 3-class label: `finished` / `unfinished` / `wait`. No VAD, no pipeline — a single model does acoustic + semantic understanding together. Achieves 90.64% accuracy on English and 98.90% on Chinese. Available on Hugging Face.

GitHub: https://github.com/TEN-framework/ten-turn-detection

**Why I'm skipping.** Three reasons:
- **Compute.** Qwen2.5-7B needs ~14GB VRAM to run at full precision. Not feasible on a standard laptop without a GPU. You can quantize it down but this is now a 2-hour setup problem before any ML work begins.
- **Black box.** Calling `model.predict(transcript)` gives me "finished" with no reasoning I can explain. What I wanted out of this project was solution-selection reasoning and tradeoff analysis — a fine-tuned model hides all of that. I can't explain *why* it fires or fails without inspecting attention weights, which is a separate research project.
- **Wrong scope.** This is what approach #10 (end-to-end neural) looks like when a company actually builds it. It requires a curated training dataset, GPU infrastructure, and a fine-tuning pipeline. It's not a 1-week solo project, and it was never the right call here.

**Why it's worth knowing.** It validates two things I already believe: (1) the `finished / unfinished / wait` 3-class taxonomy is the right output format for production systems, not binary done/not-done; (2) the field moved from rule-based silence thresholds toward semantic models. TEN is the concrete production evidence for both.

**When it would be right.** At a voice AI company (Sarvam-type) that has conversation logs to fine-tune on, a GPU cluster to train, and needs a single low-latency model call instead of a VAD+ASR+LLM pipeline. Latency advantage over a pipeline is real: one model call vs three sequential steps.

## 12. STT endpointing (provider-built)

**What it is.** Streaming STT providers (Deepgram, AssemblyAI, Google STT, Sarvam) emit a built-in end-of-utterance signal from inside their streaming WebSocket API — `is_final`, `speech_end`, or `on_utterance_end` depending on the provider. Their own acoustic + language model decides internally when the user is done. You consume the event and act on it. You build nothing extra.

The key distinction from VAD-only: the STT provider's internal LM has access to the words being spoken, not just the audio energy. Deepgram and AssemblyAI in particular use a language model to predict end-of-utterance before trailing silence fully expires — which reduces perceived latency vs waiting for a 500-800ms silence gap.

**Why I'm skipping.** It requires a live streaming STT WebSocket — you're piping real-time audio into a paid API. Our project is offline: we load audio files and run Whisper locally. Whisper has no streaming API and no `is_final` signal; it processes a complete audio clip and returns a transcript. There's no path to get STT endpointing from an offline setup without switching to a streaming provider and adding real-time plumbing (WebSocket client, audio chunking, async state machine). That's exactly the real-time plumbing this offline project deliberately keeps out of scope.

**Sarvam specifically.** Sarvam's streaming API does emit `speech_end` via WebSocket when `vad_signals=true`. However, their `speech_end` is VAD-driven (silence-based), not semantic — it has the same mid-sentence pause failure as approach #3. It's Tier 1 wired into a streaming API, not true STT endpointing. Adding the LLM check on top of Sarvam's stream would get you the same result as our smart approach, just in streaming form.

**Why it's worth knowing.** LiveKit calls this "the best default for most production agents" — it's the free endpointing that comes bundled with any streaming STT subscription. In a real system, you'd use this as your primary signal and only add a model-based layer on top for latency-sensitive or high-accuracy scenarios — the natural default if this project were moved to a real-time setting.

**When it would be right.** Any production voice agent that already uses a streaming STT provider (Deepgram, AssemblyAI). Zero extra cost, no extra model, ships in a day. Only limitation: you can't control or inspect how it decides, and accuracy varies by provider.

## Quick decision summary

| # | Approach | Status | Main reason |
|---|---|---|---|
| 1 | Energy-only silence | Skip | Too fragile, no ML |
| 2 | WebRTC VAD | Skip | Silero is strictly better in 2026 |
| 3 | Silero VAD + threshold | **CHOSEN baseline** | Best modern baseline |
| 4 | Pure semantic | Skip | Wasteful, loses cheap gate |
| 5 | VAD + ASR + LLM | **CHOSEN smart** | Matches production design, 3-class output |
| 6 | Prosody features | Skip | Needs labeled training data |
| 7 | Specialized EoU models | Skip | Closed-source, hides reasoning |
| 8 | Multimodal | Skip | Same blocker as #6 |
| 9 | Adaptive threshold | Skip as primary | Enhancement, not approach |
| 10 | End-to-end neural | Skip | Needs huge labeled data, less interpretable |
| 11 | Fine-tuned LLM (TEN) | Skip | 7B model, black box, needs GPU + training data |
| 12 | STT endpointing (provider) | Skip | Needs streaming STT API; offline project; Sarvam's is VAD-based anyway |
