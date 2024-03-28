import pygame
from copy import copy
gridSize = (100, 100)
cells = []
cellsNext = {}
def initGrid():
    newCells = {}
    for i in range(gridSize[1]):
        newCells[i] = [copy(False) for i in range(gridSize[1])]
    cells.append(newCells)
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
#check for neighbors:
initGrid()
cellsNext.clear()
print (cells)
#for x in range(gridSize[0]) :
#    xNeighbors = []
#    yNeighbors = []
#    for y in range(gridSize[1]) :
#        numNeighbors = 0
#        for i in neighbors:
#            if cells[y][x]:
#                numNeighbors += 1
        
