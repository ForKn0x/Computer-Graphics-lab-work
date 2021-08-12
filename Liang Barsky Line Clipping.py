import pygame
from pygame import gfxdraw


HEIGHT = 500
WIDTH = 500

white = (255, 255, 255)
red = (220, 20, 60)
blue = (0, 56, 147)
  
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
    pygame.display.set_caption("Liang Barsky")
    return screen

screen = prepare_screen()

x_wmax = 380.0
y_wmax = 300.0
x_wmin = 140.0
y_wmin = 140.0

def line(x1, y1, x2, y2):
	pygame.draw.line(screen,white,(x1,y1),(x2,y2))

def liangBarsky():
    xmin=20
    xmax=300
    ymin=20
    ymax=300
    #our main clipping window 
    line(xmin,ymin, xmax,ymin)
    line(xmax,ymin, xmax,ymax)
    line(xmin,ymin, xmin,ymax)
    line(xmin,ymax, xmax,ymax)
 
    x1,y1 = (10,10)
    x2,y2 = (400,160)
   
    dx = x2 - x1
    dy = y2 - y1
    p = [ -dx, dx, -dy, dy]
    q = [x1-xmin, xmax-x1, y1 - ymin, ymax - y1]

    for i in range(4):
        if(p[i] == 0):
            print('line is parallel to ' + i + 'th boundary')
            if(q[i] >= 0 ):
                if(i <2):
                    if (y1 < ymin):
                        y1 = ymin
                    if(y2 > ymax):
                        y2 = ymax
                    line(x1,y1,x2,y2)
                if (i>1):
                    if (x1 < xmin):
                        x1 = xmin
                    if (x2 > xmax):
                        x2 = xmax
                    line(x1,y1,x2,y2)
    
    t1,t2 = (0,1)

    for i in range(4):
        t = q[i]/p[i]
        if(p[i] < 0):
            if (t1 <= t):
                t1 = t
        else:
            if(t2 > t):
                t2 = t
    
    if(t1 < t2):
        xx1 = x1 + t1 * p[1]
        xx2 = x1 + t2 * p[1]
        yy1 = y1 + t1 * p[3]
        yy2 = y1 + t2 * p[3]
        pygame.draw.line(screen,blue,(xx1,yy1),(xx2,yy2)) 
        
liangBarsky()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
