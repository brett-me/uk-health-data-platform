from uk_health_platform.config import get_db_config
from uk_health_platform.smoke_checks import run_all

if __name__ == "__main__":
    config = get_db_config()
    run_all(config)