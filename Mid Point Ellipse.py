import pygame
from pygame import gfxdraw
import pygame.gfxdraw

# Screen Dimensions
HEIGHT = 720
WIDTH = 1000

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
    pygame.display.set_caption("Ellipse Using Mid Point Algorithm")
    return screen

def symmetryPoints(x,y,x_centre, y_centre):
	gfxdraw.pixel(screen,x+x_centre,y+y_centre,RED)
	gfxdraw.pixel(screen,-x+x_centre,y+y_centre,RED)
	gfxdraw.pixel(screen,x+x_centre,-y+y_centre,RED)
	gfxdraw.pixel(screen,-x+x_centre,-y+y_centre,RED)

def drawEllpise(rx, ry, xc, yc):
	x,y = 0,ry
	midpointEllipse(rx, ry, x, y, xc, yc)

def midpointEllipse(rx, ry, x, y, xc, yc):
    d1 = ((ry * ry) - (rx * rx * ry) + (0.25 * rx * rx))
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y
    while (dx < dy):
        symmetryPoints(x,y,xc,yc)
        if (d1 < 0):
            x += 1
            dx = dx + (2 * ry * ry)
            d1 = d1 + dx + (ry * ry)
        else:
            x += 1
            y -= 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d1 = d1 + dx - dy + (ry * ry)
    d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) +
          ((rx * rx) * ((y - 1) * (y - 1))) -
           (rx * rx * ry * ry))
    while (y >= 0):
        symmetryPoints(x,y,xc,yc)
        if (d2 > 0):
            y -= 1
            dy = dy - (2 * rx * rx)
            d2 = d2 + (rx * rx) - dy
        else:
            y -= 1
            x += 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d2 = d2 + dx - dy + (rx * rx)
 
screen = prepare_screen()
rx = int(input('Radius of x: '))
ry = int(input('Radius of y: '))
x = int(input('Give X coordinate of centre: '))
y = int(input('Give Y coordinate of centre: '))
drawEllpise(rx, ry, x, y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()