"""B：SQLite 存储与哈希链日志，待实现。"""
"""B: SQLite storage and audit events."""

import sqlite3
from contextlib import closing
from pathlib import Path


# Keep the database location independent of the working directory.
DB_PATH = Path(__file__).resolve().parents[1] / "loopledger.db"


def init_db() -> None:
    """Create the required tables without clearing existing data."""

    with closing(sqlite3.connect(DB_PATH)) as conn:
        with conn:
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ts TEXT NOT NULL,
                    event_type TEXT NOT NULL,
                    case_id TEXT,
                    payload TEXT NOT NULL,
                    prev_hash TEXT NOT NULL,
                    hash TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS cases (
                    case_id TEXT PRIMARY KEY,
                    prediction TEXT NOT NULL,
                    status TEXT NOT NULL
                        CHECK (status IN ('auto', 'pending', 'reviewed'))
                );
            """)


if __name__ == "__main__":
    init_db()
    print(f"Database ready: {DB_PATH}")
