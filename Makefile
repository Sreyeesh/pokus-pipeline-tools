# ✨ Default environment is dev, can be overridden via ENV_MODE=prod
ENV_MODE ?= dev

# 📥 Generate env.auto from config/environment.yaml
generate-env:
	@echo "🔁 Using ENV_MODE=$(ENV_MODE)"
	@ENV_MODE=$(ENV_MODE) python3 pipeline_scripts/generate_env_file.py

# 🔧 Build Docker image
build: generate-env
	docker-compose --env-file env.auto build

# 🔧 Rebuild without cache
build-nocache: generate-env
	docker-compose --env-file env.auto build --no-cache

# 📦 Generate folder structure
init: generate-env
	docker-compose --env-file env.auto run --rm pokus_pipeline init

# 🧪 Validate structure and naming
validate: generate-env
	docker-compose --env-file env.auto run --rm pokus_pipeline validate

# 💾 Initialize the SQLite database
init-db: generate-env
	docker-compose --env-file env.auto run --rm pokus_pipeline init-db

# 🗃️ Register assets and shots into DB
register: generate-env
	docker-compose --env-file env.auto run --rm pokus_pipeline register

# 🐚 Shell access inside container
bash: generate-env
	docker-compose --env-file env.auto run --rm pokus_pipeline bash

# 🧹 Stop all running containers
down:
	docker-compose down

# 🩺 Health check
doctor:
	@echo "✅ ENV File:"
	@cat env.auto
	@echo "✅ Verifying critical files..."
	@test -f config/environment.yaml || (echo "❌ Missing config/environment.yaml" && exit 1)
	@test -f docker/entrypoint.sh || (echo "❌ Missing docker/entrypoint.sh" && exit 1)
	@chmod +x docker/entrypoint.sh
	@echo "✅ Entrypoint permissions checked."

# ───────────────────────────────────────
# 🎯 Dev and Prod Shortcut Targets
# ───────────────────────────────────────

# 📦 Dev environment
dev-init:
	ENV_MODE=dev $(MAKE) init-db init

dev-validate:
	ENV_MODE=dev $(MAKE) validate

dev-register:
	ENV_MODE=dev $(MAKE) register

dev-build:
	ENV_MODE=dev $(MAKE) build

dev-bash:
	ENV_MODE=dev $(MAKE) bash

dev-down:
	ENV_MODE=dev $(MAKE) down

# 📦 Prod environment
prod-init:
	ENV_MODE=prod $(MAKE) init-db init

prod-validate:
	ENV_MODE=prod $(MAKE) validate

prod-register:
	ENV_MODE=prod $(MAKE) register

prod-build:
	ENV_MODE=prod $(MAKE) build

prod-bash:
	ENV_MODE=prod $(MAKE) bash

prod-down:
	ENV_MODE=prod $(MAKE) down

# 🛠️ Help menu
help:
	@echo ""
	@echo "🎬  Pipeline Makefile Commands"
	@echo "─────────────────────────────────────"
	@echo "🔧 make build           → Build Docker image"
	@echo "🔁 make build-nocache   → Force rebuild without cache"
	@echo "📦 make init            → Generate folder structure"
	@echo "💾 make init-db         → Setup pipeline database"
	@echo "🗃️  make register        → Register shots/assets in DB"
	@echo "🧪 make validate         → Validate structure and naming"
	@echo "🐚 make bash            → Open interactive container shell"
	@echo "🧹 make down            → Stop containers"
	@echo "🩺 make doctor          → Check health of environment"
	@echo ""
	@echo "🎯 Dev Targets:"
	@echo "  make dev-init         → Dev: Init DB + folder structure"
	@echo "  make dev-validate     → Dev: Validate naming"
	@echo "  make dev-register     → Dev: Register assets"
	@echo "  make dev-build        → Dev: Build image"
	@echo "  make dev-bash         → Dev: Open container shell"
	@echo "  make dev-down         → Dev: Stop containers"
	@echo ""
	@echo "🎯 Prod Targets:"
	@echo "  make prod-init        → Prod: Init DB + folder structure"
	@echo "  make prod-validate    → Prod: Validate naming"
	@echo "  make prod-register    → Prod: Register assets"
	@echo "  make prod-build       → Prod: Build image"
	@echo "  make prod-bash        → Prod: Open container shell"
	@echo "  make prod-down        → Prod: Stop containers"
