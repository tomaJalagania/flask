import json

def load_json():
    with open("questions.json") as f:
        return json.load(f)

db = load_json()
