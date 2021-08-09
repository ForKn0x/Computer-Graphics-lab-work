import pygame
from pygame import gfxdraw


HEIGHT = 1000
WIDTH = 1000

WHITE = (255, 255, 255)
RED = (220, 20, 60)
BLUE = (0, 56, 147)
  
isp = False
x1 = y1 = x2 = y2 = 0
ps = (x1, y1)
pe = (x2, y2)

def prepare_screen():
    """
    Create the initial screen.
    """
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill((0,0,0))
    pygame.display.set_caption("MLA")
    return screen

def swap(a, b):
    return b, a

def MidPointLine(x1, y1, x2, y2):
    tag = 0
    dx = x2 - x1
    dy = y2 - y1
    if (abs(dx) < abs(dy)):  # If |k| >1, coordinate swap
        x1, y1 = swap(x1, y1)
        x2, y2 = swap(x2, y2)
        tag = 1
    if (x1 > x2):  # Make sure x1 <x2
        x1, x2 = swap(x1, x2)
        y1, y2 = swap(y1, y2)
    a = y1 - y2
    b = x2 - x1
    d = a + (b / 2)
    if (y1 < y2):  # Slope> 0
        x = x1
        y = y1
        while (x < x2):
            if (d < 0):
                y = y + 1
                x = x + 1
                d = d + a + b
            else:
                d = d + a
                x = x + 1
            if (tag):  # Slope> 1
                gfxdraw.pixel(screen,y,x, (255, 255, 255))  # Swap
            else:
                gfxdraw.pixel(screen,x,y, (255, 255, 255))
    else:  # Slope <= 0
        x = x2
        y = y2
        while (x > x1):
            if (d < 0):
                y = y + 1
                x = x - 1
                d = d - a + b
            else:
                x = x - 1
                d = d - a
            if (tag):
                gfxdraw.pixel(screen,y,x, (255, 255, 255))
            else:
                gfxdraw.pixel(screen,x,y, (255, 255, 255))


screen = prepare_screen()    
x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))
MidPointLine(x1,y1,x2,y2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()