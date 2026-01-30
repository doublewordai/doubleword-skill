#!/usr/bin/env python3
"""Example scripts for using the Doubleword Batch API."""

import json
import time
import requests

API_BASE = "https://api.doubleword.ai"
API_KEY = "YOUR_API_KEY"  # Replace with your actual API key


def submit_batch(requests_data: list, completion_window: str = "24h") -> dict:
    """Submit a batch job."""
    response = requests.post(
        f"{API_BASE}/v1/batches",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "requests": requests_data,
            "completion_window": completion_window,
        },
    )
    response.raise_for_status()
    return response.json()


def get_batch_status(batch_id: str) -> dict:
    """Get the status of a batch job."""
    response = requests.get(
        f"{API_BASE}/v1/batches/{batch_id}",
        headers={"Authorization": f"Bearer {API_KEY}"},
    )
    response.raise_for_status()
    return response.json()


def get_batch_results(batch_id: str) -> list:
    """Retrieve results from a completed batch."""
    response = requests.get(
        f"{API_BASE}/v1/batches/{batch_id}/results",
        headers={"Authorization": f"Bearer {API_KEY}"},
    )
    response.raise_for_status()
    # Results are JSONL format
    results = []
    for line in response.text.strip().split("\n"):
        if line:
            results.append(json.loads(line))
    return results


def wait_for_completion(batch_id: str, poll_interval: int = 30) -> dict:
    """Poll until batch completes or fails."""
    while True:
        status = get_batch_status(batch_id)
        if status["status"] in ["completed", "failed", "expired", "canceled"]:
            return status
        print(f"Status: {status['status']}, completed: {status['request_counts']['completed']}")
        time.sleep(poll_interval)


if __name__ == "__main__":
    # Example: Submit a batch of summarization requests
    texts = [
        "The quick brown fox jumps over the lazy dog.",
        "To be or not to be, that is the question.",
        "All happy families are alike; each unhappy family is unhappy in its own way.",
    ]

    batch_requests = [
        {
            "custom_id": f"summary-{i}",
            "method": "POST",
            "url": "/v1/messages",
            "body": {
                "model": "claude-sonnet-4-20250514",
                "max_tokens": 256,
                "messages": [
                    {"role": "user", "content": f"Summarize in one sentence: {text}"}
                ],
            },
        }
        for i, text in enumerate(texts)
    ]

    print("Submitting batch...")
    batch = submit_batch(batch_requests, completion_window="24h")
    print(f"Batch ID: {batch['id']}")

    print("Waiting for completion...")
    final_status = wait_for_completion(batch["id"])
    print(f"Final status: {final_status['status']}")

    if final_status["status"] == "completed":
        print("\nResults:")
        results = get_batch_results(batch["id"])
        for result in results:
            print(f"  {result['custom_id']}: {result['response']['body']['content'][0]['text']}")
