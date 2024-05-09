import json

############################################################################ - Save
def save (list):
    
    objects = [0]
    
    with open("patterns.json") as f:
        objects = json.load(f)
        
    objects.append(objects[-1] + 1)
    
    with open("patterns.json", "w") as f:
        json.dump(objects, f)
    
    with open("pattern" + str(objects[-1]) + ".json", "w") as f:
        json.dump(list, f)

############################################################################ - Load
def load(i):
    with open("patterns.json") as f:
        objects = json.load(f)
        
    while(objects[-1] -1 < i):
        i = i - len(objects) + 1
        
    with open("pattern" + str(i) + ".json") as f:
        list = json.load(f)
        
    return list
