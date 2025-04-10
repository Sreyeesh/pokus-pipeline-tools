# 🔧 Build the Docker image
build:
	docker-compose build

# 📦 Generate the folder structure
init:
	docker-compose run --rm pokus_pipeline init

# 🧪 Validate naming and structure
validate:
	docker-compose run --rm pokus_pipeline validate

# 💾 Initialize SQLite pipeline database
init-db:
	docker-compose run --rm pokus_pipeline init-db

# 🗃️ Register assets and shots into DB
register:
	docker-compose run --rm pokus_pipeline register

# 🐚 Open an interactive shell inside the container
bash:
	docker-compose run --rm pokus_pipeline bash

# 🧹 Stop and clean up containers
down:
	docker-compose down

# 🛠️ Show available commands
help:
	@echo "🛠️  Pipeline CLI Commands:"
	@echo "  make build      - Build Docker image"
	@echo "  make init       - Generate folder structure"
	@echo "  make validate   - Validate pipeline structure and naming"
	@echo "  make init-db    - Create SQLite pipeline database"
	@echo "  make register   - Register assets and shots into DB"
	@echo "  make bash       - Open container shell"
	@echo "  make down       - Stop and remove container"
