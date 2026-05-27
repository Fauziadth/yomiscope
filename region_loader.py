import json
import os

SETTINGS_FILE = "settings.json"

def load_region():

    if not os.path.exists(SETTINGS_FILE):
        return None

    with open(SETTINGS_FILE, "r") as f:
        data = json.load(f)

    return data.get("region")

def save_region(region):

    with open(SETTINGS_FILE, "w") as f:
        json.dump({"region": region}, f, indent=4)