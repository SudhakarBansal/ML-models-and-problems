# Smart Turn Detection for Voice Assistants

This repository explores and evaluates a "Smart" approach to Endpointing / Turn Detection for real-time conversational AI. 

Traditional Voice Activity Detection (VAD) relies purely on acoustic silence. If a user pauses for 500ms, the system assumes they are done and interrupts them. This causes a frustrating user experience when humans pause mid-sentence to think.

This project implements a semantic tier on top of VAD: **Silero VAD + Whisper ASR + LLM**. Instead of cutting off the user when silence is detected, the system transcribes the speech up to the pause and asks an LLM to classify if the user's intent is actually complete.

## Repository Structure

* `data/` — Contains 14 test audio clips (`.wav`) and their ground-truth endpointing labels (`labels.json`).
* `models/` — Contains the `silero_vad.onnx` model file.
* `notebooks/` — The core experimentation pipeline:
  * `01-data-exploration.ipynb`: Analyzes the waveform and energy of human speech to demonstrate why simple energy thresholds fail.
  * `02-baseline-vad-silence.ipynb`: Implements the baseline approach (Silero VAD + 500ms silence threshold).
  * `03-smart-vad-asr-llm.ipynb`: Implements the smart approach, adding Whisper and an LLM to evaluate the text semantically during pauses.
  * `04-comparison-cells.ipynb`: Runs a side-by-side evaluation of both approaches, generating metrics, latency profiles, and failure analysis.

## Setup & Installation

The project requires the following dependencies:
```bash
pip install onnxruntime librosa matplotlib openai-whisper openai
```

Note: We use the ONNX version of Silero VAD via `onnxruntime` to avoid dependency/ABI mismatches with `torchaudio`, mimicking a lightweight production inference environment.

## Running the Evaluation

To see the results yourself:
1. Ensure your `OpenRouter` or `OpenAI` API key is set in `03-smart-vad-asr-llm.ipynb` and `04-comparison-cells.ipynb`.
2. Run notebooks 01 through 03 to understand the pipeline.
3. Run `04-comparison-cells.ipynb` to execute the full evaluation suite over all 14 test clips and view the final comparative metrics.

Please read `WRITEUP.md` for a detailed breakdown of the methodology, metrics, and production implications.
