import pygame
from copy import copy
gridSize = (10, 10)
cells = {}
def initGrid():
    newCells = {}
    for i in range(gridSize[1]):
        newCells[i] = [copy(False) for i in range(gridSize[1])]
    return newCells

def checkNeighbors(c):
    deltaCells = c
    for i in range(gridSize[1] - 2):
        for j in range(gridSize[0] - 2):
            c_x = i + 1
            c_y = j + 1
            aliveNeighbors = 0
            for n in range(8):
                x = neighbors[n][0]
                y = neighbors[n][1]
                cell = cells[c_x + x][c_y + y]
                if cell:
                    aliveNeighbors += 1
            #check if cell is dead
            if cells[c_x][c_y] == False:
                if aliveNeighbors == 3:
                    deltaCells[c_x][c_y] = True
            else:
                if aliveNeighbors <= 1:
                    deltaCells[c_x][c_y] = False
                if aliveNeighbors >= 4:
                    deltaCells[c_x][c_y] = False
    return deltaCells

neighbors = (
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, 1),
    (0, -1),
    (1, 1),
    (1, 0),
    (1, -1)
    )
cells = initGrid()

while True:
    cells = checkNeighbors(cells)
    print(cells)