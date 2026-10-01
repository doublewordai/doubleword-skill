---
name: doubleword
description: Route Doubleword LLM inference and data-processing jobs across realtime, async, and batch tiers using the dw CLI or OpenAI-compatible API.
version: 3.0.0
platforms: [linux, macos]
metadata:
  hermes:
    tags: [llm, inference, batch, data-processing, ocr, embeddings]
    category: ai
    requires_toolsets: [terminal]
    config:
      - key: doubleword.api_key
        description: Doubleword API key exposed to the shell as DOUBLEWORD_API_KEY.
        prompt: Enter your Doubleword API key.
---

# Doubleword Inference

## When to Use

Use this skill when a user asks to run generation, extraction, classification,
OCR, embeddings, evals, or dataset processing through Doubleword
(`https://api.doubleword.ai/v1`).

Prefer the native `dw` CLI for file, async, and batch workflows. Use the
OpenAI-compatible SDK or Autobatcher only when programmatic request construction
is clearer than CLI execution.

Load references only when needed:

- `references/models-and-pricing.md` for selection heuristics and a pricing
  snapshot (not the live model catalogue).
- `references/cli-recipes.md` for exact validation, submission, status,
  retrieval, resume, SDK/Autobatcher fallback commands, and the official
  Doubleword command reference link.

## Live documentation

Fetch live product and docs indexes before inventing model IDs, pricing, or
API details this skill does not embed:

- Product / company / models overview: `https://doubleword.ai/llms.txt`
- Docs index (CLI, prompt caching, API, models, integrations):
  `https://docs.doubleword.ai/llms.txt`

Most docs pages have a markdown counterpart: append `.md` to the URL and fetch
that instead of scraping HTML. This applies across the docs site, including
integrations and overview pages. Examples:

- `https://docs.doubleword.ai/inference-api/intro-to-doubleword-inference`
  → `https://docs.doubleword.ai/inference-api/intro-to-doubleword-inference.md`
- `https://docs.doubleword.ai/inference-api/autobatcher`
  → `https://docs.doubleword.ai/inference-api/autobatcher.md`
- `https://docs.doubleword.ai/inference-api/prompt-caching`
  → `https://docs.doubleword.ai/inference-api/prompt-caching.md`

Use these indexes and `.md` pages for topics the skill does not embed,
especially prompt caching, CLI details, Autobatcher, integrations, and newly
listed models.

## Autobatcher (Python)

When the user wants OpenAI-SDK-shaped Python code that transparently uses async
or batch pricing (without hand-writing JSONL), use Autobatcher:

- Package: `pip install autobatcher` (`https://pypi.org/project/autobatcher/`)
- Source: `https://github.com/doublewordai/autobatcher`
- Live docs: fetch `https://docs.doubleword.ai/inference-api/autobatcher.md`
  before inventing APIs or options

Prefer `AsyncOpenAI` from `autobatcher` for same-session async work, and
`BatchOpenAI` for bulk lowest-cost jobs. Point `base_url` at
`https://api.doubleword.ai/v1`. See `references/cli-recipes.md` for a minimal
Python pattern. Keep preferring `dw` for explicit JSONL file/batch workflows.

## Prompt caching

When many requests share a large stable prefix (system prompt, tools, schemas,
documents, or codebase context), use prompt caching to cut repeated input cost.
Fetch the live guide before inventing markers or pricing:

`https://docs.doubleword.ai/inference-api/prompt-caching.md`

Key agent rules:

- Implicit caching is on by default for cache-supported models. It needs no
  code changes, is best-effort, and never bills cache writes. A request with no
  `cache_control` markers gets implicit caching.
- Explicit caching is the opt-in upgrade for a stable prefix you control: add
  `cache_control: { "type": "ephemeral", "ttl": "5m" | "1h" }` at the end of
  each segment that changes on its own cadence (up to 4 breakpoints). Reads are
  then guaranteed for the TTL. Cache writes are billed at a premium (1.25x for
  5m, 2x for 1h), so skip markers for prefixes shorter than the minimum (often
  1,024 tokens) and let implicit caching handle them.
- Supported on OpenAI Chat Completions (`/v1/chat/completions`) and Anthropic
  Messages (`/v1/messages`) with block markers. The Responses API
  (`/v1/responses`) supports implicit caching and automatic marker placement
  only, because its input shape has no per-block markers.
- Not every model supports caching. Confirm via the model catalog
  (`cache_pricing.enabled: true`) rather than assuming it is available.
  Markers sent to a model without caching are ignored.
- Matching is left-anchored and byte-identical: put stable content first and
  volatile content (questions, timestamps, IDs) last, and keep cached blocks in
  a consistent order. Confirm hits via `usage` fields such as
  `cache_read_input_tokens` and `cache_creation_input_tokens`.

See `references/cli-recipes.md` for a minimal Chat Completions marker example.

## Procedure

1. Check local readiness before remote work:
   - confirm `DOUBLEWORD_API_KEY` is set;
   - with browser login, run `dw whoami` before uploading any file and stop if
     identity or organization verification fails;
   - with headless/API-key login, `dw whoami` may fail because it requires the
     admin API; instead, run local file validation plus a non-interactive,
     token-limited realtime probe such as
     `MODEL="${MODEL:-openai/gpt-oss-20b}"; dw realtime "$MODEL" "Reply with OK." --temperature 0 --max-tokens 2 --no-stream`
     before upload and stop if the inference probe fails.
2. Classify the task:
   - Realtime: single prompt, interactive lookup, or explicit immediate result.
   - Async: background work needed in the current session, medium datasets, or
     roughly 100+ requests.
   - Batch: large datasets, evals, overnight jobs, or no stated deadline.
3. Choose the slowest tier that satisfies the user's urgency:
   - Realtime for immediate answers;
   - Async with a 1h completion window for same-session background work;
   - Batch with a 24h completion window for lowest-cost large jobs.
   - Async can also be requested straight from code with `service_tier: "flex"`
     and `background: true` on the Responses API, then polled. Fetch
     `https://docs.doubleword.ai/inference-api/async-inference.md` before
     writing that code.
4. Select a model:
   - respect explicit user choices unless incompatible with the task;
   - prefer live discovery: run `dw models list` (and `dw models get <id>` when
     detail is needed). See `references/cli-recipes.md` for filters and output
     formats;
   - `dw models list` / `dw models get` require full `dw login` (platform
     access). API-key login (`dw login --api-key`) does not enable models
     commands — if listing fails, treat it as an auth/scope issue, not as
     “no models exist”;
   - for headless/API-key agents, skip CLI listing and fetch the two `llms.txt`
     indexes (and the models pages they index) instead of inventing IDs from
     the snapshot table;
   - use specialized OCR or embedding models for those task types;
   - otherwise choose the cheapest capable model;
   - load `references/models-and-pricing.md` only as a selection heuristic /
     snapshot, never as the live catalogue.
5. Prepare JSONL input for multi-request jobs:
   - include stable per-row identifiers when possible;
   - keep each file under 200 MB and 50,000 requests;
   - split larger workloads into numbered shards.
6. Validate local payloads before upload:
   - run `dw files validate <path>`;
   - run `dw files stats <path>`;
   - fix validation errors locally before submitting.
7. Submit the job:
   - use realtime synchronously and return the output;
   - for Async or Batch, upload/create the job, capture the batch ID, and report
     it to the user.
8. For Async or Batch, do not idle in polling loops. Check status later with a
   discrete `dw batches get <batch_id>` command only when useful or requested.
9. Retrieve completed results with `dw batches results <batch_id> -o <file>` and
   validate the output shape before using it downstream.

## Pitfalls

- Do not run `while ... sleep ...` polling loops in agent harnesses such as
  Hermes or OpenClaw; idle loops may be terminated.
- Do not upload hidden files, `.env` files, credentials, unrelated repository
  files, or data outside the user's requested scope.
- Do not print API keys, authorization headers, or signed URLs.
- Do not upload invalid JSONL. Remote validation failures waste time and may
  obscure row-level formatting issues.
- Do not assume 24h Batch is acceptable when the user needs results during the
  current working session.
- Do not rely on embedded pricing as authoritative for high-cost decisions;
  verify current Doubleword pricing when exact cost matters.

## Verification

For realtime jobs:

- output is returned to the user;
- the response names the selected model.

For Async or Batch jobs:

- either `dw whoami` succeeded before upload, or a headless/API-key readiness
  path succeeded with local file validation and a non-interactive,
  token-limited realtime inference probe;
- `dw files validate` and `dw files stats` succeeded for every uploaded JSONL
  shard;
- the user receives the selected mode, selected model, batch ID, source file or
  shard count, completion window, status-check command, and intended results
  path;
- completed results are downloaded and checked with `dw files stats` before
  downstream processing.
