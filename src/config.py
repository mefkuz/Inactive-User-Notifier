import os, json
from pathlib import Path

CONFIG_PATH = Path.home() / ".inactive_user_config.json"

DEFAULT = {
    "threshold_days": 40,
    "message": "Hello, I haven’t logged in for a while.",
    "contacts": [],
    "smtp": {"host": "smtp.example.com", "port": 587, "user": "", "password": ""},
    "last_seen_iso": None,
}

def load_config():
    if not CONFIG_PATH.exists():
        save_config(DEFAULT)
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_config(cfg):
    tmp = CONFIG_PATH.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)
    tmp.replace(CONFIG_PATH)
    try:
        os.chmod(CONFIG_PATH, 0o600)
    except Exception:
        pass
