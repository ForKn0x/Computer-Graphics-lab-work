from Transformation import reflection
import pygame
from pygame import gfxdraw


HEIGHT = 700
WIDTH = 700

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
    pygame.display.set_caption("Reflection")
    return screen

screen = prepare_screen()
gfxdraw.line(screen,0,0,1000,1000, WHITE)
a = (180,320)
b = (210,430)
c = (120,360)
gfxdraw.filled_polygon(screen, [a,b,c], RED)
a = reflection(a[0],a[1])
b = reflection(b[0],b[1])
c = reflection(c[0],c[1])
gfxdraw.filled_polygon(screen, [a,b,c], BLUE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()