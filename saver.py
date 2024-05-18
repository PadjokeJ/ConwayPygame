import json
from os import listdir
def save (list):
    objects = [0]
    with open("patterns.json") as f:
        objects = json.load(f)
    objects.append(objects[-1] + 1)
    with open("patterns.json", "w") as f:
        json.dump(objects, f)
    
    with open("pattern" + str(objects[-1]) + ".json", "w") as f:
        json.dump(list, f)
    f.close()

def load(i):
    with open("patterns.json") as f:
        objects = json.load(f)
    while(objects[-1] -1 < i):
        i = i - len(objects) + 1
    with open("pattern" + str(i) + ".json") as f:
        list = json.load(f)
    f.close()
    return list

# down below is code if you decide to index any RLE file you add in the RLE folder

def updateRLES():
    list = listdir("insert RLE path")
    with open("RLES.json", "w") as f:
        json.dump(list, f)
    f.close()
def readRLES(): 
    with open("RLES.json") as f:
        objects = json.load(f)
    f.close()
    return objects