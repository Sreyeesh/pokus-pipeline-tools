import os
import yaml

def create_structure(base_path, structure):
    for item in structure:
        if isinstance(item, dict):
            for folder, subfolders in item.items():
                path = os.path.join(base_path, folder)
                os.makedirs(path, exist_ok=True)
                create_structure(path, subfolders)
        else:
            os.makedirs(os.path.join(base_path, item), exist_ok=True)

if __name__ == "__main__":
    # Allow override for local dev
    base = os.environ.get("PROJECT_PATH", "/studio/project")
    
    # Allow either .yaml or .yml
    config_path = os.environ.get("CONFIG_PATH", "")
    if not config_path:
        if os.path.exists("config/structure.yaml"):
            config_path = "config/structure.yaml"
        elif os.path.exists("config/structure.yml"):
            config_path = "config/structure.yml"
        else:
            raise FileNotFoundError("No structure.yaml or structure.yml found in config/")

    print(f"📁 Generating folder structure from: {config_path}")
    print(f"📦 Target base folder: {base}")

    with open(config_path, 'r') as file:
        data = yaml.safe_load(file)

    create_structure(base, data["project"])
    print(f"✅ Project structure created at: {base}")
