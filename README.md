# Doubleword Batch API Skill

A skill for AI coding agents that teaches them how to work with the Doubleword Batch API.

## What is a Skill?

Skills are reusable capabilities for AI agents. They provide procedural knowledge that helps agents accomplish specific tasks more effectively. This skill teaches your AI agent how to submit and manage batch inference jobs via the Doubleword API.

The Batch API skill covers:

- Submitting batch jobs via the Doubleword API
- Monitoring batch status and handling completion
- Processing results efficiently
- Error handling and retries
- Using the autobatcher Python client

## Installation

```bash tabs=install name=Skills sync=method
npx skills add https://github.com/doublewordai/batch-skill
```

```bash tabs=install name=Git sync=method
git clone https://github.com/doublewordai/batch-skill ~/.claude/skills/batch-skill
```

## Supported Agents

This skill works with popular AI coding agents including:

- Claude Code
- Cursor
- Windsurf
- Codex
- Other agents that support the skills format

## What's Included

| File | Description |
|------|-------------|
| `SKILL.md` | Main skill file with API documentation and usage instructions |
| `examples.py` | Python examples for submitting and monitoring batch jobs |

## Using the Skill

Once installed, you can ask your AI agent questions like:

- "How do I submit a batch job to Doubleword?"
- "Show me how to monitor batch status"
- "Help me process batch results"
- "What's the best batch size for my workload?"

Your agent will reference the skill to provide accurate, up-to-date information about the Batch API.

## Updating

```bash tabs=update name=Skills sync=method
npx skills update doubleword-batch
```

```bash tabs=update name=Git sync=method
cd ~/.claude/skills/batch-skill && git pull
```

## Documentation

- [Doubleword Batch API Docs](https://docs.doubleword.ai/batches)
- [Skills CLI](https://github.com/skills-sh/skills)

## License

MIT
