import pygame
from copy import copy

# --init--
scr = (width, height) = (960, 960)
screen = pygame.display.set_mode((width, height))
game = True
clock = pygame.time.Clock()

gridSize = (10, 10)
cells = {}
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

def render(c, _gridSize, _scr, _screen):
    pixWidth = _scr[0] / _gridSize[0]
    pixHeight = _scr[1] / _gridSize[1]
    for i in range(gridSize[0]):
        for j in range(gridSize[1]):
            if(c[i][j]):
                p = pygame.Rect(i * pixWidth, j * pixHeight, pixWidth, pixHeight)
                pygame.draw.rect(_screen, (0, 0, 0), p)
# -- pre launch --
cells = initGrid()
# -- loop --
while game:
    # -- general init --
    clock.tick(60)

    cells = checkNeighbors(cells)

    # -- Inputs --
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            break
    # -- Render logic --
    screen.fill((255, 255, 255))
    render(cells, gridSize, scr, screen)
    pygame.display.flip()