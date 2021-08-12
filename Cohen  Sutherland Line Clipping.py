import pygame
from pygame import gfxdraw


HEIGHT = 500
WIDTH = 500

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
    pygame.display.set_caption("Cohen Sutherland")
    return screen

screen = prepare_screen()


INSIDE = 0 
LEFT = 1 
RIGHT = 2 
BOTTOM = 4 
TOP = 8	 

x_max = 400.0
y_max = 320.0
x_min = 160.0
y_min = 160.0

gfxdraw.polygon(screen, [(x_min,y_min),(x_max, y_min),(x_max,y_max),(x_min,y_max)], WHITE)

def computeCode(x, y):
	code = INSIDE
	if x < x_min:	 
		code |= LEFT
	elif x > x_max: 
		code |= RIGHT
	if y < y_min:	 
		code |= BOTTOM
	elif y > y_max: 
		code |= TOP

	return code



def cohenSutherlandClip(x1, y1, x2, y2):

    gfxdraw.line(screen, x1, y1, x2, y2, RED)

    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif (code1 & code2) != 0:
            break
        else:
            x = 1.0
            y = 1.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2
            if code_out & TOP:
                x = x1 + (x2 - x1) * \
                                (y_max - y1) / (y2 - y1)
                y = y_max
            elif code_out & BOTTOM:          
                x = x1 + (x2 - x1) * \
                                (y_min - y1) / (y2 - y1)
                y = y_min
            elif code_out & RIGHT:              
                y = y1 + (y2 - y1) * \
                                (x_max - x1) / (x2 - x1)
                x = x_max
            elif code_out & LEFT:               
                y = y1 + (y2 - y1) * \
                                (x_min - x1) / (x2 - x1)
                x = x_min
            if code_out == code1:
                x1 = x
                y1 = y
                code1 = computeCode(x1, y1)
            else:
                x2 = x
                y2 = y
                code2 = computeCode(x2, y2)
    if accept:
        print ("Line accepted from %.2f, %.2f to %.2f, %.2f" % (x1, y1, x2, y2))
        gfxdraw.line(screen, int(x1), int(y1), int(x2), int(y2), BLUE)
    else:
        print("Line rejected")
        


cohenSutherlandClip(100, 100, 400, 400)
cohenSutherlandClip(20, 50, 400, 20)
cohenSutherlandClip(170,300,250,170)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
