import pygame
def render(c, _gridSize, _scr, _screen):
    pixWidth = _scr[0] / _gridSize[0]
    pixHeight = _scr[1] / _gridSize[1]
    for i in range(_gridSize[0]):
        for j in range(_gridSize[1]):
            if(c[i][j]):
                p = pygame.Rect(i * pixWidth, j * pixHeight, pixWidth, pixHeight)
                pygame.draw.rect(_screen, (0, 0, 0), p)