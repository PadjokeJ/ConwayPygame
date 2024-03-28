import pygame
from copy import copy
gridSize = (10, 10)
cells = []
cellsNext = {}
def initGrid():
    newCells = {}
    for i in range(gridSize[1]):
        newCells[i] = [copy(False) for i in range(gridSize[1])]
    cells.append(newCells)

def checkNeighbors():
    for i in range(gridSize[1] - 1):
        for j in range(gridSize[0] - 1):
            print(i)
            print(cells[i])

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
initGrid()
checkNeighbors()
cellsNext.clear()

