import json
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
FILE_PATH = PROJECT_ROOT / "data" / "events.json"


def log_event(event_type, source_ip, details=""):

    # make sure folder exists
    FILE_PATH.parent.mkdir(parents=True, exist_ok=True)

    event = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": event_type,
        "source": source_ip,
        "details": details
    }

    # load existing data safely
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    # ensure it's a list
    if not isinstance(data, list):
        data = []

    data.append(event)

    # write back
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"[LOG] {event_type} from {source_ip}")