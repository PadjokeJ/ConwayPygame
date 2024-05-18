#Conway project ver 2.0
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

def warp(x, min, max):
    if x < min: x = x + max
    if x > max: x = x - max
    return x
def initGrid():
    newCells = {}
    newCells["birthRules"] = [3]
    newCells["surviveRules"] = [2, 3]
    for i in range(gridSize[0]):
        newCells[str(i)] = [copy(False) for i in range(gridSize[1])]
    return newCells
def initRLE(rle):
    cells = initGrid()
    rleCells = decodeRLE.openRLE("rle/"+ rle)
    size = rleCells["size"]
    cells["birthRules"] = rleCells["birthRule"]
    cells["surviveRules"] = rleCells["surviveRule"]
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
speed = 120
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
       cells = updateScreen(cells, gridSize, neighbors, cells["surviveRules"], cells["birthRules"])
    elif paused == False:
        ticker += 1
        if ticker >= 12:
            cells = updateScreen(cells, gridSize, neighbors, cells["surviveRules"], cells["birthRules"])
            ticker = 0
    # -- Inputs --
    pixSel = (math.floor(pygame.mouse.get_pos()[0] / pixSize[0]), math.floor(pygame.mouse.get_pos()[1] / pixSize[1]))
    realPos = pixSel
    pixSel = (warp(pixSel[0] - x, 0, gridSize[0]), warp(pixSel[1] + y, 0, gridSize[1]))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
            if event.key == pygame.K_LSHIFT:
                cells = updateScreen(cells, gridSize, neighbors, cells["surviveRules"], cells["birthRules"])
            if event.key == pygame.K_f:
                isTicking = False
            if event.key == pygame.K_s:
                isTicking = True
            if event.key == pygame.K_F4:
                cells = initGrid()
            if event.key == pygame.K_F5:
                save(cells, gridSize[0], gridSize[1])
            if event.key == pygame.K_F6:
                cells = load(i)
            if event.key == pygame.K_F7:
                cells = initRLE(RLE_list[i])
            if event.key == pygame.K_F2:
                toScreenshot = True
        if event.type == pygame.MOUSEWHEEL:
            i += int(event.y)
            if i < 0:
                i = 0
            while True:
                if i > len(RLE_list) - 1: i -= 1
                else : break
        if pygame.mouse.get_pressed(num_buttons=3)[0] == True:
            if not clicked:
                try:
                    state = not cells[str(pixSel[0])][pixSel[1]]
                except:
                    print("pixel is out of bounds", str(pixSel[0]), str(pixSel[1]))
            try: 
                cells[str(pixSel[0])][pixSel[1]] = state
            except:
                print("Clicked out of bounds", str(pixSel[0]), str(pixSel[1]))
            clicked = True
        else:
            clicked = False
    keys = pygame.key.get_pressed()  
    if keys[pygame.K_UP]: y += 1
    if keys[pygame.K_DOWN]: y -= 1
    if keys[pygame.K_LEFT]: x -= 1
    if keys[pygame.K_RIGHT]: x += 1
    x = warp(x, 0, gridSize[0])
    y = warp(y, 0, gridSize[1] - 1)
    # -- Render logic --
    screen.fill("#d7dedc")
    render(cells, gridSize, scr, screen, x, y)
    if(toScreenshot):
        screenshot(screen)
        toScreenshot = False
    pygame.draw.rect(screen, (120, 120, 120), (realPos[0] * pixSize[0], realPos[1] * pixSize[1], pixSize[0], pixSize[1]))
    txt = font.render(str(i) + " : "+ RLE_list[i], False, (0, 0, 0))
    fps = font.render("fps: " + str(math.floor(pygame.time.Clock.get_fps(clock))), False, (0, 0, 0))
    screen.blit(txt, (0, 0))
    screen.blit( fps, (920, 0))
    pygame.display.flip()
pygame.quit()
