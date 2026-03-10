ENV_RUN = set -a; . ./.env; set +a;
.PHONY: help dev-install up status down reset psql

# discovery
help:
	@echo "Targets:"
	@echo "  help         - show available commands"
	@echo "  dev-install  - install Python development dependencies"
	@echo "  up           - start local platform"
	@echo "  status       - check container status"
	@echo "  down         - stop local platform"
	@echo "  reset        - wipe and rebuild platform"
	@echo "  psql         - open database shell"

# environment / setup
dev-install:
	@echo "==> Installing Python development dependencies"
	python3 -m pip install -e ".[dev]"

# platform lifecycle
up:
	@echo "==> Starting local platform"
	docker compose up -d

status:
	@echo "==> Checking container status"
	docker compose ps

down:
	@echo "==> Stopping local platform"
	docker compose down

reset:
	@echo "==> Resetting local platform"
	docker compose down -v
	docker compose up -d

# database / data workflow
psql:
	@echo "==> Opening database shell"
	$(ENV_RUN) psql -h "$$POSTGRES_HOST" -p "$$POSTGRES_PORT" -U "$$POSTGRES_USER" -d "$$POSTGRES_DB"