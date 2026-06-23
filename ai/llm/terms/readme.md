# The Ultimate Local LLM Naming Convention Guide

When downloading cutting-edge local LLMs from Hugging Face, model names often look like a chaotic string of buzzwords. This guide breaks down those complex names into logical categories, explaining exactly what each component means and what it aims to improve (Speed, Accuracy, Memory Footprint, or Specialised Capabilities).

---

## 1. The Anatomy of an LLM File Name

Every advanced LLM name typically follows a structured pipeline from left to right:

[Creator] / [Base Model & Size] - [Architecture/Fine-Tuning] - [Optimizations & Quantization] - [File Format]

### Reference Models Decoded:
1. `majentik/Qwen3.6-35B-A3B-TurboQuant-MLX-4bit`
2. `yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF`
3. `mlx-community/RavenX-CyberAgent-Qwen3.6-35B-A3B-Opus-4.7-OpenMythos-Pentester-BugHunter-RATH-mlx-4bit-msq`
4. `mlx-community/gemma-4-31B-it-OptiQ-4bit`
5. `unsloth/Qwen3.6-35B-A3B-UD-MLX-4bit`
6. `mlx-community/Qwen3.6-35B-A3B-MTP-4bit`

---

## 2. Core Taxonomy: Technology Groupings & Metrics

To understand what to stack and what to choose, look at what each name component is trying to fix. Technologies within the same sub-category cannot be stacked.

### Category A: Foundations (Who Made It & How Big)
These tags define the baseline hardware required to host the model file before any optimization takes place.

*   `majentik / yuxinlu1 / mlx-community / unsloth`
    *   Target: Corporate or Independent Publisher / Finetuner.
    *   Takeaway: Defines who did the math, training, or quantization work.
*   `Qwen3.6 / gemma-4`
    *   Target: Base Model Architecture. (Alibaba's Qwen series vs. Google's Gemma series).
*   `12B / 31B / 35B`
    *   Target: Total Parameters (Billions). 
    *   Takeaway: Directly scales the model's baseline intelligence, but also determines how much raw system RAM is required.
*   `-it`
    *   Target: Instruction-Tuned.
    *   Takeaway: The model is configured as a conversational assistant out of the box, rather than a raw text-completer.

---

### Category B: Static Weight Quantization (The VRAM Shrinkers)
These algorithms compress the permanent, static weights of the model file down to smaller bit-widths so large models fit on consumer hardware. Pick only one per model.

*   `4bit` (Standard Uniform Quantization)
    *   Aims to improve: VRAM Footprint.
    *   How it works: Compresses the whole model uniformly from 16-bit to 4-bit. Reduces VRAM usage by ~75%.
*   `OptiQ` (mlx-optiq)
    *   Aims to improve: Accuracy Retention.
    *   How it works: A Mac-native mixed-precision method. It detects critical layers and leaves them at 8-bit, while aggressively compressing less vital layers to 3-bit or 4-bit.
*   `UD` (Unsloth Dynamic 2.0)
    *   Aims to improve: Accuracy Retention.
    *   How it works: A highly advanced, cross-platform mathematical calculation that scales layer bit-rates dynamically based on sensitivity, resulting in near-lossless 4-bit files.
*   `msq` (Mixed Stochastic Quantization / Multi-Scale)
    *   Aims to improve: Dequantization Speed & Efficiency.
    *   How it works: A highly specialized, modern sub-quantization layout built into certain MLX-community weights to speed up processing cycles on Apple Silicon.

---

### Category C: Context Cache Compressors (The Chat History Savers)
As your chat conversation grows longer, your computer's memory fills up with "context memory" (KV Cache). These tools stop long conversations from crashing your machine.

*   `TurboQuant`
    *   Aims to improve: Context Window Size & VRAM Headroom.
    *   How it works: Applies complex matrix rotation math to compress live conversation memory down to 3-bits on the fly. It allows you to run tens of thousands of words of chat history without hitting an Out-of-Memory (OOM) error.

---

### Category D: Generation Acceleration (The Speed Boosters)
These represent architectural changes or execution modes that push out text at a much higher rate.

*   `A3B` (Active 3 Billion parameters - Mixture of Experts)
    *   Aims to improve: Inference Speed & Parameter Efficiency.
    *   How it works: The model file is 35B parameters total, but it is split into specialized sub-networks. For every single word generated, it only wakes up and paths data through 3 Billion parameters. You get 35B level intelligence at blazing-fast 3B generation speeds.
*   `MTP` (Multi-Token Prediction)
    *   Aims to improve: Tokens-per-second Output Speed.
    *   How it works: The architecture contains secondary "prediction heads" that guess and push out multiple tokens simultaneously in a single processing step, acting like speculative decoding built straight into the core file.

---

### Category E: Execution Frameworks (The Engines)
The core software ecosystem used to feed the model to your system processors. Pick only one framework.

*   `GGUF`
    *   Aims to improve: Cross-Platform Compatibility.
    *   How it works: Runs universally on CPU and GPU across Windows, Mac, and Linux via engines like llama.cpp, Ollama, or LM Studio.
*   `MLX / mlx`
    *   Aims to improve: Apple Silicon Native Hardware Speed.
    *   How it works: Framework built specifically for macOS. It talks directly to Apple's Unified Memory, Neural Engine, and Mac GPU for optimal speed.

---

### Category F: Dataset Pedigree & Fine-Tuning Targets
These tags indicate that the model has undergone hyper-specialized training on elite datasets to perform specific real-world tasks.

*   `agentic`
    *   Aims to improve: Autonomy & Tool-Calling Stability.
    *   How it works: Trained to run in continuous "agent loops" (thinking, picking tools, executing commands, checking its own work) without human supervision.
*   `fable5 / composer2.5`
    *   Aims to improve: Reasoning & Code Correctness.
    *   How it works: The model was distilled using advanced Chain-of-Thought traces. composer2.5 means it was only trained on reasoning steps that successfully passed automated coding software tests.
*   `v2`
    *   Aims to improve: Feature Expansion.
    *   How it works: Denotes the secondary iteration of the custom dataset, expanding capabilities from simple Python writing to deep OS terminal interaction.
*   `OpenMythos / CyberAgent / RavenX`
    *   Aims to improve: Domain-Specific Logic.
    *   How it works: Indicates custom merge recipes or localized fine-tuning layers designed to enhance creative writing, secure agent execution, or logic routing.
*   `Pentester / BugHunter / RATH`
    *   Aims to improve: Cybersecurity & Vulnerability Assessment.
    *   How it works: Heavily fine-tuned on penetration testing data, software security vulnerabilities, code-auditing loops, and complex network mapping strategies.

---

### Category G: Benchmark Score Achievements
When developers achieve record-breaking scores on elite AI benchmarks, they append the metrics directly into the file name to prove the model's strength.

*   `3.5x`
    *   Aims to improve: Baseline Performance Visibility.
    *   Takeaway: Signifies a major multi-fold performance multiplier on core coding benchmarks compared to the stock baseline model.
*   `tau2`
    *   Aims to improve: Complex System Troubleshooting Accuracy.
    *   Takeaway: Proves highly successful navigation of Tau-Bench 2, an incredibly difficult enterprise agentic benchmark testing live environment debugging.
*   `Opus-4.7`
    *   Aims to improve: Frontier-Class Reasoning Validation.
    *   Takeaway: Custom internal grading metric showing the model scores near elite commercial closed-source standards (like Anthropic's Claude Opus variants) on internal reasoning test suites.

---

## 3. Quick Reference Metric Summary

Use this quick matrix to understand exactly what a tag is trying to optimize:

| If a name contains... | ...It is actively trying to fix: |
| :--- | :--- |
| **4bit, OptiQ, UD, GGUF** | Memory Footprint (Fitting it onto your system) |
| **A3B, MTP** | Speed (Getting words out faster) |
| **TurboQuant** | Context Window (Deep chats without crashing) |
| **agentic, fable5, composer2.5, Pentester** | Capability/Accuracy (Smarter reasoning on tasks) |
| **3.5x, tau2, Opus-4.7** | Validation (Proving it passes brutal exams) |
