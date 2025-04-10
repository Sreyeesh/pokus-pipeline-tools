#!/bin/bash
set -e
set -o pipefail

PROJECT_PATH="/studio/project"
CMD="$1"

# 📁 Ensure the project folder exists
if [ ! -d "$PROJECT_PATH" ]; then
  echo "📁 Creating project folder at $PROJECT_PATH..."
  mkdir -p "$PROJECT_PATH"
fi

# 🚀 Handle commands
case "$CMD" in
  init)
    echo "📦 Initializing project structure..."
    python3 pipeline_scripts/generate_structure.py
    ;;
  validate)
    echo "🧪 Validating project structure and naming..."
    python3 pipeline_scripts/validate_pipeline.py
    ;;
  init-db)
    echo "💾 Setting up pipeline database..."
    python3 pipeline_scripts/setup_database.py
    ;;
  register)
    echo "🗃️ Registering assets and shots into database..."
    python3 pipeline_scripts/register_from_structure.py
    ;;
  bash)
    exec bash
    ;;
  help|--help|-h|"")
    echo "🛠️  Available commands:"
    echo "  init        - Generate project folder structure"
    echo "  validate    - Validate naming conventions and structure"
    echo "  init-db     - Create SQLite pipeline database"
    echo "  register    - Register assets/shots into the database"
    echo "  bash        - Open interactive container shell"
    echo "  help        - Show this help message"
    ;;
  *)
    echo "⚙️  Running custom command: $@"
    exec "$@"
    ;;
esac
