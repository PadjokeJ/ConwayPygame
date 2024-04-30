import json

def save (list):
    with open("pattern.json", "w") as f:
        json.dump(list, f)
def load():
    with open("pattern.json") as f:
        list = json.load(f)
    return list