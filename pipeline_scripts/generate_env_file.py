import yaml
import os

CONFIG_PATH = "config/environment.yaml"
OUTPUT_ENV_FILE = "env.auto"

# 🔁 ENV_MODE takes priority over config file, else fallback
ENV_MODE = os.environ.get("ENV_MODE")

with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

# Use ENV_MODE if set, else use env_mode from config file
mode = ENV_MODE or config.get("env_mode", "dev")

if mode not in config:
    raise ValueError(f"❌ Environment '{mode}' not found in config.")

env_vars = config[mode]

with open(OUTPUT_ENV_FILE, "w") as out:
    for key, value in env_vars.items():
        out.write(f"{key}={value}\n")

print(f"✅ ENV_MODE={mode} →", " ".join(f"{k}={v}" for k, v in env_vars.items()))
