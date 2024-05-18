from copy import copy
from copy import deepcopy
def warp(n, min, max):
    if n < min: n = max
    if n > max: n = min
    return n
def updateScreen(c, _gridSize, _neighbors, surviveRule, lifeRule):
    deltaCells = deepcopy(c)
    originalCells = deepcopy(c)
    for i in range(0, _gridSize[1]):
        for j in range(0, _gridSize[0]):
            c_x = i
            c_y = j
            aliveNeighbors = 0
            for n in range(8):
                x = warp(_neighbors[n][0] + c_x, 0, _gridSize[0] - 1)
                y = warp(_neighbors[n][1] + c_y, 0, _gridSize[1] - 1)
                cell = originalCells[str(x)][y]
                if cell: aliveNeighbors += 1
            if aliveNeighbors in lifeRule: deltaCells[str(c_x)][c_y] = True
            elif not aliveNeighbors in surviveRule: deltaCells[str(c_x)][c_y] = False
    return deltaCells
