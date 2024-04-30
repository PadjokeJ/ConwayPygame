import json

def save (list):
    objects = 0
    with open("patterns.json") as f:
        objects = json.load(f)
    objects += 1
    with open("patterns.json", "w") as f:
        json.dump(objects, f)
    
    with open("pattern" + str(objects) + ".json", "w") as f:
        json.dump(list, f)

def load(i):
    with open("pattern" + i + ".json") as f:
        list = json.load(f)
    return list