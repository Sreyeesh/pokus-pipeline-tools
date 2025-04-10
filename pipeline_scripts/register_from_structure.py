import os
import sqlite3
from naming_utils import load_config, is_valid_asset_name, is_valid_shot_name

CONFIG_PATH = "config/naming.yaml"
DB_PATH = "/studio/project/database/pipeline.db"
PROJECT_ROOT = "/studio/project"

def register_assets(cursor, config):
    asset_base = os.path.join(PROJECT_ROOT, "production", "assets")
    for asset_type, prefix in config["asset_prefixes"].items():
        asset_dir = os.path.join(asset_base, asset_type + "s")
        if not os.path.exists(asset_dir):
            continue
        for name in os.listdir(asset_dir):
            if is_valid_asset_name(name, asset_type, config):
                cursor.execute("""
                    INSERT INTO assets (name, type, path, status)
                    VALUES (?, ?, ?, ?)
                """, (name, asset_type, os.path.join(asset_dir, name), "registered"))

def register_shots(cursor, config):
    shot_dir = os.path.join(PROJECT_ROOT, "production", "shots")
    if not os.path.exists(shot_dir):
        return
    for name in os.listdir(shot_dir):
        if is_valid_shot_name(name, config):
            cursor.execute("""
                INSERT INTO shots (code, folder, status)
                VALUES (?, ?, ?)
            """, (name, os.path.join(shot_dir, name), "registered"))

def main():
    config = load_config(CONFIG_PATH)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    register_assets(cursor, config)
    register_shots(cursor, config)

    conn.commit()
    conn.close()
    print("✅ Assets and shots registered in the pipeline database.")

if __name__ == "__main__":
    main()
