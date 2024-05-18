import pygame
import math
from copy import copy, deepcopy
from rendering import render
from screenUpdater import updateScreen
from saver import save, load, readRLES
from screenshotter import screenshot
import decodeRLE

# --init--
pygame.init()
scr = (width, height) = (960, 960)
screen = pygame.display.set_mode((width, height))
game = True
clock = pygame.time.Clock()
RLE_list = readRLES()

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
def initRLE(rle):
    cells = initGrid()
    rleCells = decodeRLE.openRLE("rle/"+ rle)
    size = rleCells["size"]
    print(size)
    for i in range(0, size[1]):
        for j in range(0, size[0]):
            try: 
                cells[str(i)][j] = rleCells[str(i)][j]
            except:
                a = 0
    return cells
# -- pre launch --
cells = initGrid()
empty_grid = initGrid()
paused = True
ticker = 0
speed = 60
i = 0
font = pygame.font.SysFont('Comic Sans MS',  10)
# -- loop --
state = False
isTicking = True
toScreenshot = False
x = 0
y = 0
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
            if event.key == pygame.K_LSHIFT:
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
                cells = load(i)
            if event.key == pygame.K_F7:
                while True:
                    if i > len(RLE_list): i -= 1
                    else : break
                cells = initRLE(RLE_list[i])
            if event.key == pygame.K_F2:
                toScreenshot = True
        if event.type == pygame.MOUSEWHEEL:
            i += int(event.y)
            if i < 0:
                i = 0
        if pygame.mouse.get_pressed(num_buttons=3)[0] == True:
            if not clicked:
                state = not cells[str(pixSel[0])][pixSel[1]]
            try: 
                cells[str(pixSel[0])][pixSel[1]] = state
            except:
                print("Clicked out of bounds")
            clicked = True
        else:
            clicked = False
    keys = pygame.key.get_pressed()  
    if keys[pygame.K_UP]:
        y += 1
    if keys[pygame.K_DOWN]:
        y -= 1
    if keys[pygame.K_LEFT]:
        x += 1
    if keys[pygame.K_RIGHT]:
        x -= 1
    # -- Render logic --
    screen.fill((255, 255, 255))
    render(cells, gridSize, scr, screen, x, y)
    if(toScreenshot):
        screenshot(screen)
        toScreenshot = False
    pygame.draw.rect(screen, (120, 120, 120), (pixSel[0] * pixSize[0], pixSel[1] * pixSize[1], pixSize[0], pixSize[1]))
    txt = font.render(str(i), False, (0, 0, 0))
    screen.blit(txt, (0, 0))
    pygame.display.flip()
pygame.quit()
