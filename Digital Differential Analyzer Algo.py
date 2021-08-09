import pygame
from pygame import gfxdraw
import pygame.gfxdraw

# Screen Dimensions
HEIGHT = 300
WIDTH = 300

WHITE = (255, 255, 255)
RED = (220, 20, 60)
BLUE = (0, 56, 147)

def prepare_screen():
    """
    Create the initial screen.
    """
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(WHITE)
    pygame.display.set_caption("DDA")
    return screen

def ROUND(a):

  return int(a + 0.5)

def drawDDA(x1,y1,x2,y2):
  x,y = x1,y1
  length = (x2-x1) if (x2-x1) > (y2-y1) else (y2-y1)
  dx = (x2-x1)/float(length)
  dy = (y2-y1)/float(length)
  gfxdraw.pixel(screen,ROUND(x),ROUND(y),RED)
  for i in range(length):
    x += dx
    y += dy
    gfxdraw.pixel(screen,ROUND(x),ROUND(y),RED)


screen = prepare_screen()
drawDDA(0,0,100,200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()