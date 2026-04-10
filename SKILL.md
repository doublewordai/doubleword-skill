---
name: doubleword
description: High-performance LLM inference (realtime, async, batch) and CLI tools via the Doubleword platform
---

# Doubleword Inference API

The Doubleword platform provides high-performance LLM inference with an OpenAI-compatible API. It offers three inference modes, 12 models across text generation, vision, OCR, and embeddings, and a full CLI (`dw`) for managing workflows from the terminal.

## Three Inference Modes

| Aspect | Realtime | Async (autobatcher) | Batch |
|--------|----------|---------------------|-------|
| **Latency** | Immediate | Minutes | Hours |
| **Cost** | Standard | Reduced (50-80%+ savings) | Lowest |
| **Setup** | No changes needed | Single import swap | JSONL file preparation |
| **Best for** | Interactive chat, prototyping | Pipelines, agentic workflows | Dataset processing, evals, bulk generation |

## Documentation

Full docs at https://docs.doubleword.ai/inference-api and https://docs.doubleword.ai/dw-cli

For raw markdown (recommended for AI agents), append `.md` to any URL.

**Inference API**
- Overview: `https://docs.doubleword.ai/inference-api.md`
- Getting started: `https://docs.doubleword.ai/inference-api/intro-to-doubleword-inference.md`
- Models & pricing: `https://docs.doubleword.ai/inference-api/models.md`
- Realtime inference: `https://docs.doubleword.ai/inference-api/realtime-inference.md`
- Async inference (autobatcher): `https://docs.doubleword.ai/inference-api/async-inference.md`
- Batch inference: `https://docs.doubleword.ai/inference-api/batch-inference.md`
- Batch notifications & webhooks: `https://docs.doubleword.ai/inference-api/batch-notifications-and-webhooks.md`
- Creating an API key: `https://docs.doubleword.ai/inference-api/creating-an-api-key.md`
- Tool calling & structured outputs: `https://docs.doubleword.ai/inference-api/tool-calling.md`
- autobatcher: `https://docs.doubleword.ai/inference-api/autobatcher.md`
- JSONL files: `https://docs.doubleword.ai/inference-api/jsonl-files.md`
- API reference (OpenAPI): `https://docs.doubleword.ai/inference-api/api-reference.md`

**CLI**
- Overview: `https://docs.doubleword.ai/dw-cli.md`
- Introduction: `https://docs.doubleword.ai/dw-cli/introduction.md`
- Installation: `https://docs.doubleword.ai/dw-cli/installation.md`
- Authentication: `https://docs.doubleword.ai/dw-cli/authentication.md`
- Quickstart: `https://docs.doubleword.ai/dw-cli/quickstart.md`
- Batch processing: `https://docs.doubleword.ai/dw-cli/batches.md`
- Streaming results: `https://docs.doubleword.ai/dw-cli/streaming.md`
- Realtime inference: `https://docs.doubleword.ai/dw-cli/realtime.md`
- JSONL format: `https://docs.doubleword.ai/dw-cli/jsonl-format.md`
- Local file tools: `https://docs.doubleword.ai/dw-cli/file-tools.md`
- Project system: `https://docs.doubleword.ai/dw-cli/projects.md`
- Examples: `https://docs.doubleword.ai/dw-cli/examples.md`
- Command reference: `https://docs.doubleword.ai/dw-cli/commands.md`
- Accounts: `https://docs.doubleword.ai/dw-cli/accounts.md`
- Keys & webhooks: `https://docs.doubleword.ai/dw-cli/keys-webhooks.md`
- Usage: `https://docs.doubleword.ai/dw-cli/usage.md`
- Global flags: `https://docs.doubleword.ai/dw-cli/global-flags.md`

**Workbooks (examples)**
- CLI examples: `https://docs.doubleword.ai/inference-api/cli-examples`
- Async agents: `https://docs.doubleword.ai/inference-api/async-agents`
- Data processing pipelines: `https://docs.doubleword.ai/inference-api/data-processing-pipelines`
- Structured extraction: `https://docs.doubleword.ai/inference-api/structured-extraction`
- Semantic search without embeddings: `https://docs.doubleword.ai/inference-api/semantic-search-without-embeddings`
- Research paper digest: `https://docs.doubleword.ai/inference-api/research-summaries`
- Image summarization: `https://docs.doubleword.ai/inference-api/image-summarization`
- Embeddings: `https://docs.doubleword.ai/inference-api/embeddings`
- Model evals: `https://docs.doubleword.ai/inference-api/model-evals`
- Synthetic data generation: `https://docs.doubleword.ai/inference-api/synthetic-data-generation`
- Dataset compilation: `https://docs.doubleword.ai/inference-api/dataset-compilation`
- Bug detection ensemble: `https://docs.doubleword.ai/inference-api/bug-detection-ensemble`

## Quick Reference

### Base URL
```
https://api.doubleword.ai/v1
```

### Available Models

#### Text Generation

| Model | Realtime (in/out) | High 1h (in/out) | Standard 24h (in/out) |
|-------|-------------------|-------------------|------------------------|
| Qwen/Qwen3.5-4B | — | $0.05 / $0.08 | $0.04 / $0.06 |
| Qwen/Qwen3.5-9B | $0.08 / $0.70 | $0.04 / $0.35 | $0.03 / $0.29 |
| Qwen/Qwen3-14B-FP8 | $0.05 / $0.60 | $0.03 / $0.30 | $0.02 / $0.20 |
| Qwen/Qwen3.5-35B-A3B-FP8 | $0.25 / $2.00 | $0.07 / $0.30 | $0.05 / $0.20 |
| Qwen/Qwen3-VL-30B-A3B-Instruct-FP8 | $0.16 / $0.80 | $0.07 / $0.30 | $0.05 / $0.20 |
| Qwen/Qwen3-VL-235B-A22B-Instruct-FP8 | $0.60 / $1.20 | $0.15 / $0.55 | $0.10 / $0.40 |
| Qwen/Qwen3.5-397B-A17B | $0.60 / $3.60 | $0.30 / $1.80 | $0.15 / $1.20 |
| nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 | $0.30 / $0.75 | $0.23 / $0.56 | $0.15 / $0.38 |
| openai/gpt-oss-20b | $0.04 / $0.30 | $0.03 / $0.20 | $0.02 / $0.15 |

Prices per 1M tokens.

#### OCR Models

| Model | High 1h (in/out) | Standard 24h (in/out) |
|-------|-------------------|------------------------|
| allenai/olmOCR-2-7B-1025-FP8 | $0.15 / $0.15 | $0.10 / $0.10 |
| lightonai/LightOnOCR-2-1B-bbox-soup | $0.08 / $0.08 | $0.05 / $0.05 |

#### Embedding Model

| Model | Realtime (input) | High 1h (input) | Standard 24h (input) |
|-------|------------------|------------------|----------------------|
| Qwen/Qwen3-Embedding-8B | $0.04 | $0.03 | $0.02 |

### Limits
- Max file size: 200MB
- Max requests per file: 50,000

## Realtime Inference

Standard request-response, identical to OpenAI's API. Use the OpenAI SDK pointed at Doubleword:

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.doubleword.ai/v1"
)

response = client.chat.completions.create(
    model="Qwen/Qwen3.5-35B-A3B-FP8",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

Or use the CLI for quick testing:

```bash
dw realtime Qwen/Qwen3.5-35B-A3B-FP8 "Explain batch inference in one paragraph"

# With system message
dw realtime Qwen/Qwen3.5-35B-A3B-FP8 "Summarize this" --system "You are a concise technical writer."

# Pipe input
cat document.txt | dw realtime Qwen/Qwen3.5-35B-A3B-FP8 --system "Summarize this"
```

## Async Inference (autobatcher)

Drop-in replacement for `AsyncOpenAI` that transparently batches requests. Works with both OpenAI (50% savings) and Doubleword (80%+ savings).

GitHub: https://github.com/doublewordai/autobatcher

```bash
pip install autobatcher
```

### How It Works

1. Requests accumulate over a configurable time window (default: 10 seconds)
2. When the window closes or batch size limit is reached, requests submit as a batch
3. Results are polled and returned to waiting callers
4. Code receives standard response objects (ChatCompletion, CreateEmbeddingResponse, Response)

### Configuration

| Parameter | Default | Purpose |
|-----------|---------|---------|
| `api_key` | None | API key (falls back to `OPENAI_API_KEY` env var) |
| `batch_size` | 1000 | Submit when this many requests queue |
| `batch_window_seconds` | 10.0 | Submit after this many seconds |
| `poll_interval_seconds` | 5.0 | Polling frequency for batch completion |
| `completion_window` | `"24h"` | Batch completion SLA (`"24h"` or `"1h"`) |

### Supported Endpoints

- **Chat Completions**: `client.chat.completions.create()` → `ChatCompletion`
- **Embeddings**: `client.embeddings.create()` → `CreateEmbeddingResponse`
- **Responses API**: `client.responses.create()` → `Response`

### Usage

```python
import asyncio
from autobatcher import BatchOpenAI

async def main():
    client = BatchOpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.doubleword.ai/v1",
    )

    response = await client.chat.completions.create(
        model="Qwen/Qwen3.5-35B-A3B-FP8",
        messages=[{"role": "user", "content": "Hello!"}],
    )
    print(response.choices[0].message.content)
    await client.close()

asyncio.run(main())
```

### Parallel Processing with Context Manager

```python
async def process_many(prompts: list[str]) -> list[str]:
    async with BatchOpenAI(base_url="https://api.doubleword.ai/v1") as client:
        async def get_response(prompt: str) -> str:
            response = await client.chat.completions.create(
                model="Qwen/Qwen3.5-35B-A3B-FP8",
                messages=[{"role": "user", "content": prompt}],
            )
            return response.choices[0].message.content

        return await asyncio.gather(*[get_response(p) for p in prompts])
```

### Embeddings

```python
async def embed(client: BatchOpenAI):
    response = await client.embeddings.create(
        model="Qwen/Qwen3-Embedding-8B",
        input="Hello, world!",
    )
    print(response.data[0].embedding[:5])
```

## Batch Inference

Upload JSONL files for large-scale processing at the lowest cost. Fully compatible with OpenAI's Batch API.

### Batch File Format (.jsonl)

Each line contains a single request:

```json
{"custom_id": "req-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "Qwen/Qwen3.5-35B-A3B-FP8", "messages": [{"role": "user", "content": "Hello"}]}}
```

Required fields:
- `custom_id`: Your unique identifier (max 64 chars)
- `method`: Always `"POST"`
- `url`: `"/v1/chat/completions"` or `"/v1/embeddings"`
- `body`: Standard request parameters

### API Operations

#### 1. Upload Batch File

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.doubleword.ai/v1"
)

batch_file = client.files.create(
    file=open("batch.jsonl", "rb"),
    purpose="batch"
)
```

#### 2. Create Batch

```python
batch = client.batches.create(
    input_file_id=batch_file.id,
    endpoint="/v1/chat/completions",
    completion_window="24h",  # or "1h"
    metadata={"description": "my batch job"}
)
```

#### 3. Check Status

```python
status = client.batches.retrieve(batch.id)
print(status.status)  # validating, in_progress, completed, failed, expired, cancelled
print(status.request_counts)  # {"total": 100, "completed": 50, "failed": 0}
```

#### 4. Download Results

Results available immediately as they complete (unlike OpenAI):

```python
import requests

response = requests.get(
    f"https://api.doubleword.ai/v1/files/{batch.output_file_id}/content",
    headers={"Authorization": f"Bearer YOUR_API_KEY"}
)

# Check if batch still running
is_incomplete = response.headers.get("X-Incomplete") == "true"
last_line = response.headers.get("X-Last-Line")

with open("results.jsonl", "wb") as f:
    f.write(response.content)

# Resume partial download with ?offset=<last_line>
```

#### 5. Cancel Batch

```python
client.batches.cancel(batch.id)
```

#### 6. List Batches

```python
batches = client.batches.list(limit=10)
```

## `dw` CLI

The Doubleword CLI handles batch inference workflows, realtime requests, and local file operations from the terminal.

GitHub: https://github.com/doublewordai/dw

### Installation

```bash
# Recommended
curl -fsSL https://raw.githubusercontent.com/doublewordai/dw/main/install.sh | sh

# Or via pip
pip install --user dw-cli

# Verify
dw --version
```

### Authentication

```bash
# Browser login (recommended)
dw login

# Organization-scoped
dw login --org my-org

# Headless (CI/CD, SSH)
dw login --api-key YOUR_INFERENCE_KEY

# Verify
dw whoami
```

Credentials stored in `~/.dw/credentials.toml`.

### `dw stream` — One-Liner Batch Workflow

Uploads, creates a batch, watches progress, and pipes results to stdout:

```bash
dw stream batch.jsonl > results.jsonl

# Override model
dw stream batch.jsonl --model Qwen/Qwen3.5-397B-A17B > results.jsonl

# Priority processing
dw stream batch.jsonl --completion-window 1h > results.jsonl

# Process all files in a directory
dw stream input_dir/ > results.jsonl
```

### `dw batches` — Batch Management

```bash
# Upload and create batch
dw batches run batch.jsonl --watch

# Step-by-step
dw files upload batch.jsonl
dw batches create --file file-abc123 --completion-window 1h

# Monitor
dw batches watch batch-abc123
dw batches get batch-abc123
dw batches list

# Results
dw batches results batch-abc123 -o results.jsonl
dw batches analytics batch-abc123

# Cancel / retry
dw batches cancel batch-abc123
dw batches retry batch-abc123
```

### `dw realtime` — Quick Testing

```bash
dw realtime Qwen/Qwen3.5-35B-A3B-FP8 "What is batch inference?"

# Options: --system, --max-tokens, --temperature, --no-stream, --usage
dw realtime Qwen/Qwen3.5-35B-A3B-FP8 "Summarize" --system "Be concise" --usage
```

### Local File Tools

All operations run locally without authentication:

```bash
dw files validate batch.jsonl          # Check format
dw files stats batch.jsonl             # Line count, models, token estimates
dw files prepare batch.jsonl --model Qwen/Qwen3.5-35B-A3B-FP8  # Transform JSONL
dw files sample batch.jsonl -n 10      # Random sample
dw files merge a.jsonl b.jsonl -o combined.jsonl
dw files split large.jsonl -n 5000     # Split into chunks
dw files diff results_a.jsonl results_b.jsonl  # Compare by custom_id
```

### Project System

Define multi-step workflows via `dw.toml`:

```bash
dw project init my-project     # Create from template
dw project run prepare         # Run a single step
dw project run-all             # Run full workflow
dw project run-all --continue  # Resume after failure
dw project status              # Check progress
dw project clean               # Remove artifacts
```

## Tool Calling & Structured Outputs

Fully compatible with OpenAI's function calling and structured outputs:

```python
response = client.chat.completions.create(
    model="Qwen/Qwen3.5-35B-A3B-FP8",
    messages=[{"role": "user", "content": "What's the weather in SF?"}],
    tools=[{
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "City name"}
                },
                "required": ["location"]
            }
        }
    }],
    tool_choice="auto"
)
```

For structured outputs, use `response_format` with JSON Schema:

```python
response = client.chat.completions.create(
    model="Qwen/Qwen3.5-35B-A3B-FP8",
    messages=[{"role": "user", "content": "Extract contact info from: John Doe, john@example.com, 555-1234"}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "contact_info",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "email": {"type": "string"},
                    "phone": {"type": "string"}
                },
                "required": ["name", "email"],
                "additionalProperties": False
            }
        }
    }
)
```

## Key Differences from OpenAI

1. **Partial results**: Download results as they complete, don't wait for entire batch
2. **Resumable downloads**: Use `X-Last-Line` header with `?offset=` to resume
3. **Output file created immediately**: `output_file_id` available right after batch creation
4. **Three service tiers**: Realtime (immediate), High/1h (priority batch), Standard/24h (cheapest batch)
5. **Cost estimation**: Upload files to the Console for pre-submission cost estimates, or use `dw files cost-estimate`

## Security & Data Privacy

- **Data transmission**: Any data in `.jsonl` batch files or API requests is transmitted to `https://api.doubleword.ai` for processing
- **Avoid PII and secrets**: Do not include Personally Identifiable Information, passwords, API keys, or private database URIs in batch requests
- **Use scoped API keys**: Generate a limited-privilege API key dedicated to batch processing rather than using your master account key

## Console

Web interface at https://app.doubleword.ai for:
- Managing API keys (https://app.doubleword.ai/api-keys)
- Uploading files and creating batches
- Monitoring real-time progress
- Viewing usage and cost analytics

## Support

- Documentation: https://docs.doubleword.ai/inference-api
- CLI docs: https://docs.doubleword.ai/dw-cli
- GitHub: https://github.com/doublewordai
- Contact: support@doubleword.ai
