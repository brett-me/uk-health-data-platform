import psycopg2
from uk_health_platform.config import DatabaseConfig
from uk_health_platform.db import get_connection


def check_database_reachable(config: DatabaseConfig) -> None:
    """Verify the database is reachable."""
    try:
        conn = get_connection(config)
        conn.close()
        print("  [ok] database reachable")
    except psycopg2.OperationalError as e:
        raise RuntimeError(f"  [fail] database not reachable: {e}")


def run_all(config: DatabaseConfig) -> None:
    """Run all smoke checks."""
    check_database_reachable(config)
    print("All checks passed.")