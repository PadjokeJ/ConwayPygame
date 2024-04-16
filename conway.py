import pygame
import math
from copy import copy
from rendering import render
from screenUpdater import updateScreen

# --init--
scr = (width, height) = (960, 960)
screen = pygame.display.set_mode((width, height))
game = True
clock = pygame.time.Clock()

gridSize = (96, 96)
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
pixSize = (scr[0] / gridSize[0], scr[1] / gridSize[1])

def initGrid():
    newCells = {}
    for i in range(gridSize[1]):
        newCells[i] = [copy(False) for i in range(gridSize[1])]
    return newCells

# -- pre launch --
cells = initGrid()
paused = True
ticker = 0
# -- loop --
while game:
    # -- general init --
    clock.tick(60)

    if paused == False:
        ticker += 1
        if ticker >= 6:
            cells = updateScreen(cells, gridSize, neighbors)
            ticker = 0
    # -- Inputs --
    pixSel = (math.floor(pygame.mouse.get_pos()[0] / pixSize[0]), math.floor(pygame.mouse.get_pos()[1] / pixSize[1]))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
            if event.key == pygame.K_RIGHT:
                cells = updateScreen(cells, gridSize, neighbors)
        if pygame.mouse.get_pressed(num_buttons=3)[0] == True:
            cells[pixSel[0]][pixSel[1]] = not cells[pixSel[0]][pixSel[1]]
    # -- Render logic --
    
    screen.fill((255, 255, 255))
    render(cells, gridSize, scr, screen)
    pygame.draw.rect(screen, (120, 120, 120), (pixSel[0] * pixSize[0], pixSel[1] * pixSize[1], pixSize[0], pixSize[1]))
    pygame.display.flip()