import pygame
def render(c, _gridSize, _scr, _screen, _x, _y):
    pixWidth = _scr[0] / _gridSize[0]
    pixHeight = _scr[1] / _gridSize[1]
    for i in range(_gridSize[0]):
        for j in range(_gridSize[1]):
            if(c[str(i)][j]):
                x = i * pixWidth + _x * pixWidth
                if (x > _scr[0]): x -= _scr[0] - 1
                elif (x < 0): x += _scr[0] - 1

                y = j * pixHeight - _y * pixHeight
                if (y > _scr[1]): y -= _scr[1] - 1
                elif (y < 0): y += _scr[1] - 1

                p = pygame.Rect(x, y, pixWidth, pixHeight)
                
                pygame.draw.rect(_screen, "#4b475c", p)