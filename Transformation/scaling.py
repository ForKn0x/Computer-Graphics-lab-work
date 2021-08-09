from Transformation import scaling
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
    pygame.display.set_caption("Scaling")
    return screen

screen = prepare_screen()
a=(20,30)
b = (100,200)
c = (300,150)
gfxdraw.polygon(screen, [a,b,c], RED)
a = scaling(a[0],a[1], 2, 2)
b = scaling(b[0],b[1], 2, 2)
c = scaling(c[0],c[1], 2, 2)

gfxdraw.polygon(screen, [a,b,c], BLUE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()