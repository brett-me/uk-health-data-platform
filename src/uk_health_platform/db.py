import psycopg2
from uk_health_platform.config import DatabaseConfig


def get_connection(config: DatabaseConfig):
    """Return a psycopg2 connection using validated config."""
    return psycopg2.connect(**config.connection_params)