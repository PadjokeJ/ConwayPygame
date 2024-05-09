from copy import copy
from copy import deepcopy

############################################################################ - Update Screen
def updateScreen(c, _gridSize, _neighbors):
    
    deltaCells = deepcopy(c)
    originalCells = deepcopy(c)
    
    for i in range(1, _gridSize[1] - 1):
        for j in range(1, _gridSize[0] - 1):
            
            c_x = i
            c_y = j
            aliveNeighbors = 0
            
            for n in range(8):
                x = _neighbors[n][0]
                y = _neighbors[n][1]
                # print(c_x, x)
                cell = originalCells[str(c_x + x)][c_y + y]
                
                if cell:
                    aliveNeighbors += 1


            #Conway's game of life rules
            if aliveNeighbors == 3:
                deltaCells[str(c_x)][c_y] = True
                
            if aliveNeighbors <= 1:
                deltaCells[str(c_x)][c_y] = False
                
            if aliveNeighbors >= 4:
                deltaCells[str(c_x)][c_y] = False
                
    return deltaCells
