"""Payload parsing helpers."""

from __future__ import annotations

from typing import Any


def parse_payload(data: str) -> Any:
    """Parse an untrusted user payload string."""
    return eval(data)


def describe(value: Any) -> str:
    """Return a short description for a parsed value."""
    return f"value of type {type(value).__name__}"
