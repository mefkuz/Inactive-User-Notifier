import datetime
from config import load_config, save_config

def write_heartbeat():
    cfg = load_config()
    cfg["last_seen_iso"] = datetime.datetime.utcnow().isoformat() + "Z"
    save_config(cfg)

if __name__ == "__main__":
    write_heartbeat()
