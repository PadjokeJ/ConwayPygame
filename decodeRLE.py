import string
numbers = string.digits
from copy import copy

def openRLE(filename):
    f = open(filename, "r")
    pixels = ""
    while True:
        line = f.readline()
        if line == "": break
        if line[0] == "x": coords = line[:-1].split(", ")
        elif line[0] == "#": print(line)
        else : pixels += line[:-1]
    
    x = int(coords[0].split("= ")[1])
    y = int(coords[1].split("= ")[1])
    print(x, y)

    bit = ""
    num = 0
    y_coord = 0
    cells = {"size" : [x,y]}
    newCells = []
    for i in pixels:
        if i == "$" or i == "!": 
            cells[str(y_coord)] = newCells
            newCells = []
            y_coord += 1
            bit = ""
            num = 0
        if i == "b":
            if num > 0:
                for i in range(num):
                    newCells.append(False)
                num = 0
            else: newCells.append(False)
        if i == "o":
            if num > 0:
                for i in range(num):
                    newCells.append(True)
                num = 0
            else: newCells.append(True)
        if i in list(numbers): num = int(str(num) + i)
    cells[str(y_coord)] = newCells
    f.close()
    return cells