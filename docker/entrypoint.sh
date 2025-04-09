#!/bin/bash

set -e

PROJECT_PATH="/studio/project"
CMD="$1"

# 📁 Create the project directory if it doesn't exist
if [ ! -d "$PROJECT_PATH" ]; then
  echo "📁 Creating project folder at $PROJECT_PATH..."
  mkdir -p "$PROJECT_PATH"
fi

case "$CMD" in
  init)
    echo "📦 Initializing project structure..."
    python3 pipeline_scripts/generate_structure.py
    ;;
  validate)
    echo "🧪 Validating project structure..."
    python3 pipeline_scripts/validate_pipeline.py
    ;;
  help | --help | -h)
    echo "🛠️ Usage:"
    echo "  init       - Generate folder structure"
    echo "  validate   - Validate existing structure"
    echo "  bash       - Open container shell"
    echo "  help       - Show this help"
    ;;
  *)
    echo "⚙️ Running custom command: $@"
    exec "$@"
    ;;
esac
