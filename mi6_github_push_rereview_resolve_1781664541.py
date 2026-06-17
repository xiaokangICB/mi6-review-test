"""GitHub E2E target module."""

import sqlite3
from typing import Any


def get_user(user_id: int) -> tuple[Any, ...] | None:
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return cursor.fetchone()


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("divisor must not be zero")
    return a / b
