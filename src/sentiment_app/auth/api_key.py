"""Checks a client's API key against the key configured in the environment."""

import hmac
import os


def is_valid_api_key(provided_key: str) -> bool:
    expected_key = os.environ.get("SENTIMENT_API_KEY")
    if not expected_key:
        return False
    return hmac.compare_digest(provided_key, expected_key)
