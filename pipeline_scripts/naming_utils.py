import re
import yaml
import os
from typing import Optional


def load_config(path: str) -> dict:
    """Load the YAML config from a specified path and extract the 'naming' section."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"[ERROR] Naming config not found at: {path}")
    with open(path, "r") as f:
        raw = yaml.safe_load(f)
        # Handle top-level or nested under 'naming'
        if "naming" in raw:
            return raw["naming"]
        return raw


def is_valid_asset_name(name: str, asset_type: str, config: dict) -> bool:
    """Validate asset name against its expected prefix."""
    prefix = config.get("asset_prefixes", {}).get(asset_type)
    return name.startswith(prefix) if prefix else False


def is_valid_shot_name(name: str, config: dict) -> bool:
    """Validate shot name using the configured format (e.g., sh{num:03d})."""
    pattern = config.get("shot_format", "")
    pattern = pattern.replace("{num:03d}", r"\d{3}")
    return re.fullmatch(pattern, name) is not None


def is_valid_version(name: str, config: dict) -> bool:
    """Validate version strings like v001 or v001_final."""
    base_pattern = config.get("version_format", "").replace("{num:03d}", r"\d{3}")
    tags = config.get("allowed_version_tags", [])
    if tags:
        pattern = f"{base_pattern}(_({'|'.join(tags)}))?$"
    else:
        pattern = base_pattern
    return re.fullmatch(pattern, name) is not None


def is_valid_export_name(filename: str, config: dict) -> bool:
    """Validate exported filename pattern like asset_v001.png or asset_v001_final.png."""
    name, _ = os.path.splitext(filename)
    parts = name.split("_")

    if len(parts) < 2:
        return False

    # Determine if last part is a tag
    last = parts[-1]
    if last in config.get("allowed_version_tags", []):
        version = "_".join(parts[-2:])
    else:
        version = parts[-1]

    return is_valid_version(version, config)


def bump_version(version: str) -> str:
    """Increment a version string like v001 → v002."""
    match = re.match(r"v(\d{3})", version)
    if match:
        next_num = int(match.group(1)) + 1
        return f"v{next_num:03d}"
    return version
