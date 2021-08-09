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
    pygame.display.set_caption("BLA")
    return screen

def bresenham(x1,y1,x2, y2):

    slope = (y2-y1)/(x2-x1)

    # Slope is less than one
    if (slope < 1):
        del_x = 2 * (y2 - y1)
        # initial deciding factor
        p = del_x - (x2 - x1)
        y=y1
        for x in range(x1,x2+1):
        
            gfxdraw.pixel(screen,x,y,RED)
    
            p = p + del_x
           
            if (p >= 0):
                y=y+1
                p =p - 2 * (x2 - x1)
    # Slope is greater than one
    elif (slope >=1):
        del_x = 2 * (x2 - x1)
        #initial deciding factor
        p = del_x - (y2 - y1)
        x=x1
        for y in range(y1,y2+1):
        
            gfxdraw.pixel(screen,x,y,RED)
    
            p = p + del_x
            if (p >= 0):
                x=x+1
                p = p - 2 * (y2 - y1)
         
screen = prepare_screen()    
x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))
bresenham(x1,y1,x2,y2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()