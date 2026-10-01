# Doubleword Skill

The `doubleword` skill helps AI agents such as Claude Code, Cursor, Codex, Hermes and OpenClaw run cost-aware LLM
inference on Doubleword.ai. It gives agents a practical operating procedure for
choosing between realtime, async, and 24-hour batch inference, validating local
JSONL payloads, submitting jobs through the `dw` CLI, and retrieving results.

Doubleword.ai provides high-performance inference for generation, extraction,
classification, OCR, embeddings, evals, and large data-processing workflows.

## Installation

Install with the Skills CLI:

```bash
npx skills add https://github.com/doublewordai/doubleword-skill
```

Or clone into your agent skills directory:

```bash
git clone https://github.com/doublewordai/doubleword-skill
```

### Updating

```bash
npx skills update doubleword
```

Or, if you installed via git:

```bash
git pull
```

Some agents, like Hermes and OpenClaw, may use a different skills path than the
default Skills CLI targets. If the one-liner does not land where your harness
loads skills, clone or copy this repository into that harness skills directory
instead.

## Get a Doubleword.ai Account

You need a Doubleword.ai account and API key to use this skill.

If you do not already have an account, sign up at
[doubleword.ai](https://doubleword.ai/). Signup is free and includes free tokens
so you can try the platform before adding paid usage.

After creating an account, create or copy an API key and expose it to your agent
environment as:

```bash
export DOUBLEWORD_API_KEY="your_api_key_here"
```

The skill supports two authentication readiness paths. With browser login, it
verifies identity and organization with:

```bash
dw whoami
```

For headless/API-key login, `dw whoami` may fail because API-key credentials do
not include admin API access. In that mode, the skill validates JSONL payloads
locally and uses a non-interactive, token-limited realtime request, such as
`MODEL="${MODEL:-openai/gpt-oss-20b}"; dw realtime "$MODEL" "Reply with OK." --temperature 0 --max-tokens 2 --no-stream`,
as the inference-authentication probe before uploading or submitting jobs.

## What This Skill Does

- Routes small interactive prompts to realtime inference.
- Sends same-session background workflows to async inference.
- Uses 24-hour batch inference for large jobs when cost savings matter more than
  immediate completion.
- Validates JSONL payloads locally before upload.
- Encourages deterministic request IDs so batch results can be joined back to
  source data.
- Avoids long idle polling loops that are unsafe for agents like Hermes.
- Points agents to detailed command, model, and pricing references only when
  needed.

## Repository Layout

```text
SKILL.md
references/
  cli-recipes.md
  models-and-pricing.md
```

This repository is packaged as a single skill, so `SKILL.md` lives at the
repository root.

The skill uses progressive disclosure:

- **Level 0:** skill list metadata from `SKILL.md`
- **Level 1:** operating procedure in `SKILL.md`
- **Level 2:** detailed command and model references under `references/`

References are intentionally separate because command recipes, model tables, and
pricing notes are detail-heavy and may change more frequently than the core
skill procedure.

## Key Files

- [`SKILL.md`](./SKILL.md) - Main skill definition and agent procedure.
- [`references/cli-recipes.md`](./references/cli-recipes.md) - Doubleword CLI
  recipes, official command reference link, and non-blocking execution
  guardrails for agents like Hermes.
- [`references/models-and-pricing.md`](./references/models-and-pricing.md) -
  Model selection guidance, pricing tables, and batch limits.

## Requirements

- A Doubleword.ai account.
- `DOUBLEWORD_API_KEY` configured in the agent environment.
- The Doubleword `dw` CLI available wherever the agent runs Doubleword jobs.
- Terminal access for agent skill execution (for example Hermes or OpenClaw).

## Documentation

- Doubleword.ai: [https://doubleword.ai](https://doubleword.ai/)
- Doubleword API base URL: `https://api.doubleword.ai/v1`
- Live product / models index:
  [https://doubleword.ai/llms.txt](https://doubleword.ai/llms.txt)
- Live docs index (CLI, caching, API, models):
  [https://docs.doubleword.ai/llms.txt](https://docs.doubleword.ai/llms.txt)
- Most docs pages have a `.md` counterpart (append `.md` to the URL), for
  example
  [intro](https://docs.doubleword.ai/inference-api/intro-to-doubleword-inference.md)
  and
  [autobatcher](https://docs.doubleword.ai/inference-api/autobatcher.md).
- Prompt caching:
  [https://docs.doubleword.ai/inference-api/prompt-caching.md](https://docs.doubleword.ai/inference-api/prompt-caching.md)
- Autobatcher (Python):
  [docs](https://docs.doubleword.ai/inference-api/autobatcher.md),
  [GitHub](https://github.com/doublewordai/autobatcher),
  [PyPI](https://pypi.org/project/autobatcher/)
- List available models with `dw models list` when the CLI has full platform
  login (not API-key-only auth).
- `dw` CLI command reference:
  [https://doublewordai.github.io/dw/commands.html](https://doublewordai.github.io/dw/commands.html)

## License

See [`LICENSE`](./LICENSE).
