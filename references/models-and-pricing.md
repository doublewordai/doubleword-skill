# Doubleword Models and Pricing Reference

This file is a **selection heuristic / pricing snapshot (2026-10-16)**, not the
live model catalogue. Authoritative current models and prices come from
`dw models list` (full `dw login`), the
[Models & Pricing page](https://docs.doubleword.ai/inference-api/models), or
`https://doubleword.ai/llms.txt` and `https://docs.doubleword.ai/llms.txt`.

Use this reference when the user asks about cost, when model choice is
ambiguous, or before submitting a large or expensive job. Prices are per 1M
tokens, input / output, unless otherwise noted.

Realtime inference is available for most models at standard rates. Verify
current Doubleword pricing before submitting high-cost work or quoting exact
costs.

## Deprecations

Check the
[scheduled-for-deprecation list](https://docs.doubleword.ai/inference-api/models#scheduled-for-deprecation)
before choosing or reusing a model ID. Deprecated models stop accepting API
requests on their deprecation date. Never pick a model from that list for new
work, and when an existing job or script uses one, switch it to the listed
replacement.

Models deprecated on **2026-10-30** and their recommended replacements:

| Deprecated | Replacement |
| --- | --- |
| `deepseek-ai/DeepSeek-V4-Flash` | `deepseek-ai/DeepSeek-V4-Flash-0731` |
| `deepseek-ai/DeepSeek-V4-Pro` | `deepseek-ai/DeepSeek-V4-Pro-0813` |
| `deepseek-ai/DeepSeek-OCR-2` | `lightonai/LightOnOCR-2-1B-bbox-soup` |
| `google/gemma-4-26B-A4B-it` | `meta-models/Muse-Glimmer-30B` |
| `zai-org/GLM-5.1-FP8` | `zai-org/GLM-5.2-FP8` |
| `openai/gpt-oss-20b` | `deepseek-ai/DeepSeek-V4-Flash-0731` |
| `openai/gpt-oss-120b` | `deepseek-ai/DeepSeek-V4.1-Flash` (or `google/gemma-4-31B-it` for a US developer) |
| `tencent/Hy3-FP8` | `deepseek-ai/DeepSeek-V4.1-Flash` |
| `thinkingmachines/Inkling-NVFP4` | `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4` |
| `moonshotai/Kimi-K2.6` | `zai-org/GLM-5.2-FP8` (`moonshotai/kimi-k3` within the Kimi family) |
| `XiaomiMiMo/MiMo-V2.5-Pro` | `deepseek-ai/DeepSeek-V4.1-Flash` |
| `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4` | `meta-models/Muse-Glimmer-30B` |
| `allenai/olmOCR-2-7B-1025-FP8` | `lightonai/LightOnOCR-2-1B-bbox-soup` |
| `Qwen/Qwen3-14B-FP8` | `deepseek-ai/DeepSeek-V4-Flash-0731` |
| `Qwen/Qwen3-VL-30B-A3B-Instruct-FP8` | `Qwen/Qwen3-VL-235B-A22B-Instruct-FP8` |
| `Qwen/Qwen3.5-4B`, `Qwen/Qwen3.5-9B` | `deepseek-ai/DeepSeek-V4-Flash-0731` |
| `Qwen/Qwen3.5-397B-A17B-FP8` | `Qwen/Qwen3.8-27B-FP8` |
| `Qwen/Qwen3.5-9B-dottxt`, `Qwen/Qwen3.5-397B-A17B-FP8-dottxt` | `Qwen/Qwen3.5-35B-A3B-FP8-dottxt` |

## Selection Heuristics

- Cheapest capable text generation: start with `DeepSeek-V4-Flash-0731` or
  `Muse-Glimmer-30B`.
- Balanced inexpensive generation: use `DeepSeek-V4.1-Flash`,
  `GLM-5.3-Flash`, `Gemma-4-31B-it`, or `Qwen3.6-35B-A3B-FP8`.
- Harder reasoning, long-form generation, difficult extraction, or eval
  judging: consider `DeepSeek-V4-Pro-0813`, `GLM-5.3`, `GLM-5.2-FP8`,
  `Qwen3.8-27B-FP8`, `Nemotron-3-Ultra-550B-A55B`, or `Kimi-K3`.
- Constrained/structured decoding: `Qwen3.5-35B-A3B-FP8-dottxt`.
- Vision-language tasks: use `Qwen3-VL-235B-A22B-Instruct-FP8`
  (`DeepSeek-V4.1-Flash` also has native vision).
- OCR: use a specialized OCR model unless the task requires custom reasoning
  over extracted text.
- Embeddings: use `Qwen3-Embedding-8B`.

## Text Generation Models

| Model ID | Async | Batch, 24h |
| --- | --- | --- |
| `deepseek-ai/DeepSeek-V4-Flash-0731` | $0.07 / $0.14 | $0.05 / $0.09 |
| `meta-models/Muse-Glimmer-30B` | $0.07 / $0.24 | $0.05 / $0.15 |
| `google/gemma-4-31B-it` | $0.09 / $0.26 | $0.06 / $0.18 |
| `zai-org/GLM-5.3-Flash` | $0.11 / $0.38 | $0.08 / $0.25 |
| `deepseek-ai/DeepSeek-V4.1-Flash` | $0.12 / $0.48 | $0.08 / $0.30 |
| `Qwen/Qwen3.6-35B-A3B-FP8` | $0.11 / $0.75 | $0.07 / $0.50 |
| `Qwen/Qwen3.5-35B-A3B-FP8-dottxt` | $0.14 / $0.60 | $0.10 / $0.40 |
| `Qwen/Qwen3.8-27B-FP8` | $0.35 / $2.25 | $0.25 / $1.50 |
| `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4` | $0.38 / $1.65 | $0.25 / $1.10 |
| `zai-org/GLM-5.2-FP8` | $0.70 / $2.25 | $0.47 / $1.50 |
| `deepseek-ai/DeepSeek-V4-Pro-0813` | $0.99 / $2.97 | $0.66 / $1.98 |
| `zai-org/GLM-5.3` | $1.05 / $3.30 | $0.70 / $2.20 |
| `moonshotai/kimi-k3` | $2.15 / $11.25 | $1.50 / $7.50 |
| `Qwen/Qwen3-VL-235B-A22B-Instruct-FP8` | $0.16 / $1.43 | $0.11 / $0.95 |

Cache-read rates are model-specific; see the Models & Pricing page.

## Specialized Models

| Task | Model ID | Async | Batch |
| --- | --- | --- | --- |
| OCR | `lightonai/LightOnOCR-2-1B-bbox-soup` | $0.08 / $0.08 | $0.05 / $0.05 |
| Embeddings | `Qwen/Qwen3-Embedding-8B` | $0.03 input | $0.02 input |

## Batch Limits

- Maximum batch file size: 200 MB.
- Maximum requests per batch file: 50,000.
- Split larger workloads into numbered shards and submit each shard separately.
