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
    pygame.display.set_caption("Circle Using Mid Point Algorithm")
    return screen

def drawCircle(radius,x_centre, y_centre):
	x,y = 0,radius
	midPointAlgo(x,y,radius,x_centre, y_centre)

def symmetryPoints(x,y,x_centre, y_centre):
	gfxdraw.pixel(screen,x+x_centre,y+y_centre,RED)
	gfxdraw.pixel(screen,-x+x_centre,y+y_centre,RED)
	gfxdraw.pixel(screen,x+x_centre,-y+y_centre,RED)
	gfxdraw.pixel(screen,-x+x_centre,-y+y_centre,RED)
	gfxdraw.pixel(screen,y+x_centre,x+y_centre,RED)
	gfxdraw.pixel(screen,-y+x_centre,x+y_centre,RED)
	gfxdraw.pixel(screen,y+x_centre,-x+y_centre,RED)
	gfxdraw.pixel(screen,-y+x_centre,-x+y_centre,RED)


def midPointAlgo(x,y,radius,x_centre, y_centre):
	d = 5/4.0 - radius
	symmetryPoints(x,y,x_centre, y_centre)
	while x < y:
		if d < 0:
			x += 1
			d += 2*x + 1
		else:
			x += 1
			y -= 1
			d += 2*(x-y) + 1
		symmetryPoints(x,y,x_centre, y_centre)

screen = prepare_screen()
radius = int(input('Give Radius: '))
x = int(input('Give X coordinate of centre: '))
y = int(input('Give Y coordinate of centre: '))
drawCircle(radius,x,y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()