from Transformation import rotation
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
    pygame.display.set_caption("Rotation")
    return screen

screen = prepare_screen()
a=(200,300)
b = (500,200)
c = (300,150)
gfxdraw.filled_polygon(screen, [a,b,c], RED)
a = rotation(a[0],a[1], 30)
b = rotation(b[0],b[1], 30)
c = rotation(c[0],c[1], 30)

gfxdraw.filled_polygon(screen, [a,b,c], BLUE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()