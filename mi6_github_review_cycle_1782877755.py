"""Payload parsing helpers."""

from __future__ import annotations

import ast
from typing import Any


def parse_payload(data: str) -> Any:
    """Parse an untrusted user payload string without executing code."""
    try:
        return ast.literal_eval(data)
    except (ValueError, SyntaxError) as exc:
        raise ValueError("invalid payload literal") from exc


def describe(value: Any) -> str:
    """Return a short description for a parsed value."""
    return f"value of type {type(value).__name__}"
