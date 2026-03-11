from pydantic_settings import BaseSettings


class DatabaseConfig(BaseSettings):
    """Database connection configuration loaded from environment."""

    postgres_host: str
    postgres_port: int
    postgres_db: str
    postgres_user: str
    postgres_password: str

    model_config = {"env_file": ".env", "extra": "ignore"}

    @property
    def connection_params(self) -> dict:
        """Return psycopg2-compatible connection parameters."""
        return {
            "host": self.postgres_host,
            "port": self.postgres_port,
            "dbname": self.postgres_db,
            "user": self.postgres_user,
            "password": self.postgres_password,
        }


def get_db_config() -> DatabaseConfig:
    """Return validated database configuration."""
    return DatabaseConfig()