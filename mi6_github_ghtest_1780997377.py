"""GitHub E2E target module."""

import sqlite3
from typing import Any


def get_user(user_id: int) -> tuple[Any, ...] | None:
    conn = sqlite3.connect("users.db")
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return cursor.fetchone()
    finally:
        conn.close()


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("divisor must not be zero")
    return a / b
