# Turn Detection Evaluation Writeup

This document summarizes the methodology, findings, and production implications from the Smart Turn Detection project.

## The Problem
Real-time conversational agents must determine when a user has finished speaking to respond naturally. The industry standard baseline relies on **Acoustic Silence Thresholds** (e.g., if the user pauses for >500ms, they are done). However, human speech is non-linear; we often pause mid-sentence to think or search for words. A purely acoustic system interrupts the user repeatedly during these natural hesitations.

## The Solution: Semantic Endpointing
This project evaluates a "Smart" pipeline that layers semantic understanding over acoustic VAD:
1. **Silero VAD** detects a silence gap (>500ms).
2. **Whisper ASR** transcribes the speech up to that exact moment.
3. An **LLM** classifies the partial transcript into a **3-class taxonomy**:
   * `finished`: The thought is complete. The agent responds.
   * `unfinished`: The thought is incomplete (e.g., ends in a dangling preposition). The agent waits.
   * `wait`: The thought is grammatically complete, but the user explicitly intended to hold the floor (e.g., "Wait, let me think"). The agent waits.

*Note: For this evaluation, streaming ASR is simulated by re-transcribing the growing audio buffer from scratch at each gap. In production, a streaming ASR engine would maintain state.*

## Results & Metrics
Tested across 14 ground-truth conversational clips featuring mid-sentence pauses, the Smart approach heavily outperformed the baseline:

| Metric | Baseline (VAD + 500ms) | Smart (VAD + ASR + LLM) |
|---|---|---|
| **Precision** | 64.29% | 84.62% |
| **Recall** | 69.23% | 84.62% |
| **False-cut Rate** | 35.71% | 14.29% |

* **False-cut reduction:** The smart approach slashed the rate at which users were erroneously interrupted by more than half.

## Failure Analysis

### Why Binary Systems Fail: The `wait` Intent
The taxonomy uses 3 classes instead of a binary "done/not-done" because of clips like `clip-13.wav` ("Wait, don't respond yet."). This sentence is grammatically complete, and the pause following it looks acoustically identical to a turn-end. A binary system will interrupt the user here. By treating `wait` as a distinct class, the semantic system correctly respects the user's explicit floor-holding intent.

### Where the Smart Approach Succeeds
In clips with long mid-sentence hesitations (e.g., `clip-14.wav`: "I am facing some issues with my... [pause] PNR number"), the LLM successfully recognizes the dangling modifier, returns `unfinished`, and prevents the false cut that the baseline would have triggered.

### Where the Smart Approach Fails
The smart pipeline is not perfect. It failed on `clip-07` and `clip-11` by cutting the user off early. 
**Root Cause:** In both cases, the ASR transcript was perfectly accurate, but the user paused for >500ms *immediately after a grammatically complete thought*, intending to add a secondary thought later. Because the LLM only sees text, it made a reasonable decision that the turn was `finished`. Without prosodic acoustic cues (like pitch or breath intake), text-only VAD has inherent limitations on predicting human continuation after a completed sentence.

## Path to Production

To bring this proof-of-concept into a production environment, the following system-level changes are required:

1. **Reduce LLM Latency:** Currently, the LLM adds significant latency (average ~4 seconds). In production (such as the TEN framework), this general-purpose LLM must be replaced by a fine-tuned small classifier (e.g., DistilBERT or quantized Qwen2.5-3B). This brings classification latency down to ~50ms per gap.
2. **ASR Error Correction:** The LLM's classification is only as good as the transcript it receives. Implementing ASR error correction (especially for highly accented English or poor acoustic environments) is critical to prevent cascading errors where bad transcripts lead to false endpointing cuts.
3. **Multimodal / Prosody Integration:** To solve the remaining false cuts where users pause after complete sentences, future iterations should explore multimodal models (like GPT-4o real-time API) that process audio directly, utilizing pitch and tone to sense if a speaker has truly yielded the floor.
