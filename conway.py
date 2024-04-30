import pygame
import math
from copy import copy
from rendering import render
from screenUpdater import updateScreen
from saver import save
from saver import load

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
pixSize = (scr[0] / (gridSize[0]), scr[1] / (gridSize[1]))

def initGrid():
    newCells = {}
    for i in range(gridSize[0]):
        newCells[str(i)] = [copy(False) for i in range(gridSize[1])]
    return newCells

# -- pre launch --
cells = initGrid()
paused = True
ticker = 0
speed = 60
# -- loop --
state = False
isTicking = True
while game:
    # -- general init --
    clock.tick(speed)
    if(not isTicking and not paused):
       cells = updateScreen(cells, gridSize, neighbors)
    elif paused == False:
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
            if event.key == pygame.K_f:
                speed = 1000
                isTicking = False
            if event.key == pygame.K_s:
                isTicking = True
                speed = 60
            if event.key == pygame.K_F5:
                save(cells)
            if event.key == pygame.K_F6:
                cells = load()
        if pygame.mouse.get_pressed(num_buttons=3)[0] == True:
            if not clicked:
                state = not cells[str(pixSel[0])][pixSel[1]]
            cells[str(pixSel[0])][pixSel[1]] = state
            clicked = True
        else:
            clicked = False
    # -- Render logic --
    
    screen.fill((255, 255, 255))
    render(cells, gridSize, scr, screen)
    pygame.draw.rect(screen, (120, 120, 120), (pixSel[0] * pixSize[0], pixSel[1] * pixSize[1], pixSize[0], pixSize[1]))
    pygame.display.flip()
pygame.quit()
