
def updateScreen(c, _gridSize, _neighbors):
    deltaCells = c
    for i in range(1, _gridSize[1] - 1):
        if(i != 0 or i != _gridSize[1]):
            for j in range(1, _gridSize[0] - 1):
                if(j != 0 or j != _gridSize[0]):
                    c_x = i
                    c_y = j
                    aliveNeighbors = 0
                    for n in range(8):
                        x = _neighbors[n][0]
                        y = _neighbors[n][1]
                        # print(c_x, x)
                        cell = c[c_x + x][c_y + y]
                        if cell:
                            aliveNeighbors += 1
                    #check if cell is dead
                    if c[c_x][c_y] == False:
                        if aliveNeighbors == 3:
                            deltaCells[c_x][c_y] = True
                        else:
                            if aliveNeighbors <= 1:
                                deltaCells[c_x][c_y] = False
                            if aliveNeighbors >= 4:
                                deltaCells[c_x][c_y] = False
    return deltaCells