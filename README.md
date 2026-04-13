# Doubleword Inference Skill

A skill for AI coding agents that teaches them how to work with the Doubleword platform for high-performance LLM inference and CLI tooling.

## What is a Skill?

Skills are reusable capabilities for AI agents. They provide procedural knowledge that helps agents accomplish specific tasks more effectively.

This skill covers:

- Three inference modes: realtime, async (autobatcher), and batch
- 12 models across text generation, vision, OCR, and embeddings
- The `dw` CLI for batch workflows, streaming, and local file tools
- Tool calling and structured outputs
- Model pricing across realtime, async, and batch tiers

## Installation

```bash tabs=install name=Skills sync=method
npx skills add https://github.com/doublewordai/doubleword-skill
```

```bash tabs=install name=Git sync=method
git clone https://github.com/doublewordai/doubleword-skill
```

## Supported Agents

This skill works with AI coding agents including:

- Claude Code
- Cursor
- Windsurf
- Codex
- Other agents that support the skills format

## Using the Skill

Once installed, you can ask your AI agent questions like:

- "How do I use Doubleword for realtime inference?"
- "Set up autobatcher to batch my API calls automatically"
- "Help me submit a batch job and download results"
- "What models are available and what do they cost?"
- "Show me how to use the dw CLI to process a JSONL file"
- "How do I use structured outputs with Doubleword?"

## Updating

```bash tabs=update name=Skills sync=method
npx skills update doubleword
```

```bash tabs=update name=Git sync=method
cd ~/.claude/skills/doubleword-skill && git pull
```

## Links

- [GitHub Repository](https://github.com/doublewordai/doubleword-skill)
- [Doubleword Inference API Docs](https://docs.doubleword.ai/inference-api)
- [Doubleword CLI Docs](https://docs.doubleword.ai/dw-cli)
- [Doubleword Console](https://app.doubleword.ai)
- [Skills CLI](https://github.com/skills-sh/skills)

## License

MIT
