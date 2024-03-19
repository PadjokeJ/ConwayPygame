import pygame
gridSize = (100, 100)
cells = {0 : [True, False, True], 1:[True, True, True]}
cellsNext = {}

neighbors =
(
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
cellsNext.clear()
for x in range(gridSize[0]) :
    xNeighbors = []
    yNeighbors = []
    for y in range(gridSize[1]) :
        numNeighbors = 0
        for i in neighbors:
            if cells[(y + i[1])[(x + i[0])]]:
                numNeighbors += 1
        
