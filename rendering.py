import pygame
def render(c, _gridSize, _scr, _screen, _x, _y):
    pixWidth = _scr[0] / _gridSize[0]
    pixHeight = _scr[1] / _gridSize[1]
    for i in range(_gridSize[0]):
        for j in range(_gridSize[1]):
            if(c[str(i)][j]):
                p = pygame.Rect(i * pixWidth - (_x * pixWidth), j * pixHeight - (_y * pixHeight), pixWidth, pixHeight)
                pygame.draw.rect(_screen, (0, 0, 0), p)