---
name: doubleword-batch
description: Submit and manage batch inference jobs via Doubleword API
---

# Doubleword Batch API

This skill teaches you how to use the Doubleword Batch API for high-throughput inference workloads with up to 50% cost savings.

## Overview

The Batch API is designed for processing large volumes of requests asynchronously. Instead of waiting for each request to complete, you submit a batch job and retrieve results when processing finishes.

**Key benefits:**
- Up to 50% cost savings compared to real-time inference
- Higher throughput limits
- Automatic retries and error handling
- Results available for 7 days after completion

## API Endpoints

Base URL: `https://api.doubleword.ai`

### Submit a Batch Job

```bash
POST /v1/batches
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json

{
  "requests": [
    {
      "custom_id": "request-1",
      "method": "POST",
      "url": "/v1/messages",
      "body": {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 1024,
        "messages": [
          {"role": "user", "content": "Summarize this text: ..."}
        ]
      }
    }
  ],
  "completion_window": "24h"
}
```

Response:
```json
{
  "id": "batch_abc123",
  "status": "validating",
  "request_counts": {
    "total": 1,
    "completed": 0,
    "failed": 0
  },
  "created_at": "2025-01-15T10:00:00Z"
}
```

### Check Batch Status

```bash
GET /v1/batches/{batch_id}
Authorization: Bearer YOUR_API_KEY
```

Status values: `validating`, `in_progress`, `completed`, `failed`, `expired`, `canceling`, `canceled`

### Retrieve Results

Once status is `completed`:

```bash
GET /v1/batches/{batch_id}/results
Authorization: Bearer YOUR_API_KEY
```

Returns JSONL with one result per line:
```json
{"custom_id": "request-1", "response": {"status_code": 200, "body": {...}}}
```

### Cancel a Batch

```bash
POST /v1/batches/{batch_id}/cancel
Authorization: Bearer YOUR_API_KEY
```

### List Batches

```bash
GET /v1/batches
Authorization: Bearer YOUR_API_KEY
```

Query parameters: `limit`, `after`, `before`

## Completion Windows and Pricing

| Window | Discount | Use Case |
|--------|----------|----------|
| 24h | 50% off | Large batch jobs, overnight processing |
| 1h | 25% off | Faster turnaround, still cost-effective |

## Best Practices

1. **Use custom_ids**: Always include meaningful `custom_id` values to correlate results with your original requests.

2. **Batch size**: Submit batches of 1,000-10,000 requests for optimal throughput. The API accepts up to 50,000 requests per batch.

3. **Poll efficiently**: Check status every 30-60 seconds rather than constantly polling.

4. **Handle partial failures**: Some requests in a batch may fail while others succeed. Always check `request_counts` and process both successful and failed results.

5. **Idempotency**: Use the same batch ID for retries to avoid duplicate processing.

## Python Client (Autobatcher)

The `doubleword` Python package includes an autobatcher for easy batch processing:

```python
from doubleword import Doubleword

client = Doubleword(api_key="YOUR_API_KEY")

# Submit requests - automatically batched
results = client.batches.create_and_wait(
    requests=[
        {
            "custom_id": f"req-{i}",
            "params": {
                "model": "claude-sonnet-4-20250514",
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": text}]
            }
        }
        for i, text in enumerate(texts)
    ],
    completion_window="24h"
)

for result in results:
    print(result.custom_id, result.response.content)
```

## Error Handling

Common errors:

- `400 Bad Request`: Invalid request format or parameters
- `401 Unauthorized`: Invalid or missing API key
- `429 Too Many Requests`: Rate limit exceeded, retry with backoff
- `500 Internal Server Error`: Retry the request

For batch-level errors, check the `errors` field in the batch status response.

## Monitoring

Track batch progress via:
1. Status polling (recommended)
2. Webhook notifications (configure in dashboard)
3. Batch API list endpoint for overview

## Documentation

Full documentation: https://docs.doubleword.ai/batches
