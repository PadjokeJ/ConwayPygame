import json
from os import listdir
def save (list, g_x, g_y):
    objects = [0]
    f = open("cgol/pattern.cgol", "w")
    for x in list["surviveRules"]:
        f.write(str(x))
    f.write("/")
    for x in list["birthRules"]:
        f.write(str(x))
    f.write("!")
    for i in range(g_x):
        line = ""
        for j in range(g_y):
            if list[str(i)][j]: line += "1"
            else: line += "0"
        f.write(line + "$")
    f.close()

def load():
    f = open("cgol/pattern.cgol", "r")
    s = f.readline()
    rows = s.split("!")
    rules = rows[0].split("/")
    bits = rows[1].split("$")
    y = 0
    cells = {"surviveRules": list(int(x) for x in rules[0]), "birthRules": list(int(x) for x in rules[1])}
    
    for i in bits:
        line = []
        for j in i:
            if j == "1": line.append(True)
            else: line.append(False)
        cells[str(y)] = line
        y += 1
    print(cells)
    return cells

# down below is code if you decide to index any RLE file you add in the RLE folder

def updateRLES():
    list = listdir("enter path here (separators are forward slashes)")
    with open("RLES.json", "w") as f:
        json.dump(list, f)
    f.close()
def readRLES(): 
    with open("RLES.json") as f:
        objects = json.load(f)
    f.close()
    return objects
# updateRLES() #remove comment from this line