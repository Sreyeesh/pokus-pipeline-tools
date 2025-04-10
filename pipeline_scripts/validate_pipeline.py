import os
from naming_utils import (
    load_config,
    is_valid_asset_name,
    is_valid_shot_name,
    is_valid_version,
    is_valid_export_name
)

def validate_structure(project_root: str, config_path: str):
    errors = []
    config = load_config(config_path)

    # Validate shots
    shots_path = os.path.join(project_root, "production", "shots")
    if os.path.exists(shots_path):
        for folder in os.listdir(shots_path):
            if not is_valid_shot_name(folder, config):
                errors.append(f"❌ Invalid shot folder name: {folder}")

    # Validate assets
    asset_types = config["asset_prefixes"].keys()
    for asset_type in asset_types:
        plural = asset_type + "s"
        asset_path = os.path.join(project_root, "production", "assets", plural)
        if os.path.exists(asset_path):
            for asset in os.listdir(asset_path):
                if not is_valid_asset_name(asset, asset_type, config):
                    errors.append(f"❌ Invalid {asset_type} name: {asset}")

    # Validate design exports
    export_path = os.path.join(project_root, "preproduction", "designs", "characters", "poku", "exports")
    if os.path.exists(export_path):
        for file in os.listdir(export_path):
            if not is_valid_export_name(file, config):
                errors.append(f"❌ Invalid export file: {file}")

    # Summary
    if errors:
        print("\n".join(errors))
        print(f"🚫 Validation failed with {len(errors)} issue(s).")
    else:
        print("✅ All naming conventions validated successfully.")

if __name__ == "__main__":
    config_path = os.environ.get("NAMING_CONFIG_PATH", "config/naming.yaml")
    validate_structure("/studio/project", config_path)
