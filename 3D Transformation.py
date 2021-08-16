import pygame,math
from pygame.locals import *
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *


def translate():
    pygame.display.set_caption("3D Translation")
    tx,ty,tz = (10,40,20)
    x1,y1,z1 = (-10,16,20)
    x2,y2,z2 = (5,40,10)
    x3,y3,z3 = (40,39,30)
    t_matrix = [[1,0,0,tx],[0,1,0,ty],[0,0,1,tz],[0,0,0,1]]

    h_coordinate = [[x1,x2,x3],[y1,y2,y3],[z1,z2,z3],[1,1,1]]
    #initial triangle
    glBegin(GL_TRIANGLES)

    glColor3f(255.0, 0, 0)
    glVertex3fv((x1,y1,z1))
    glVertex3fv((x2,y2,z2))
    glVertex3fv((x3,y3,z3))	
    glEnd()


    ans = np.dot(t_matrix, h_coordinate)
    #translated triangle
    t_x1,t_y1,t_z1 = (ans[0][0], ans[1][0], ans[2][0])
    t_x2,t_y2,t_z2= (ans[0][1], ans[1][1], ans[2][1])
    t_x3,t_y3,t_z3= (ans[0][2], ans[1][2], ans[2][2])
    
    glBegin(GL_TRIANGLES)

    glColor3fv((0, 0, 1))
    glVertex3fv((t_x1,t_y1,t_z1))
    glVertex3fv((t_x2,t_y2, t_z2))
    glVertex3fv((t_x3,t_y3, t_z3))
    glEnd()

   
 
def scaling():
    pygame.display.set_caption("3D Scaling")
    sx,sy,sz = (2,2,2)
    x1,y1,z1 = (-5,10,16)
    x2,y2,z2 = (20,6,14)
    x3,y3,z3 = (36,37,29)
    s_matrix = [[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0,0,0,1]]

    h_coordinate = [[x1,x2,x3],[y1,y2,y3],[z1,z2,z3],[1,1,1]]
    #initial triangle
    glBegin(GL_TRIANGLES)

    glColor3f(255.0, 0, 0)
    glVertex3fv((x1,y1,z1))
    glVertex3fv((x2,y2,z2))
    glVertex3fv((x3,y3,z3))	
    glEnd()
    
   


    ans = np.dot(s_matrix, h_coordinate)
    #Scaled triangle
    s_x1,s_y1,s_z1 = (ans[0][0], ans[1][0], ans[2][0])
    s_x2,s_y2,s_z2= (ans[0][1], ans[1][1], ans[2][1])
    s_x3,s_y3,s_z3= (ans[0][2], ans[1][2], ans[2][2])
    
    glBegin(GL_TRIANGLES)

    glColor3fv((0, 0, 1))
    glVertex3fv((s_x1,s_y1,s_z1))
    glVertex3fv((s_x2,s_y2, s_z2))
    glVertex3fv((s_x3,s_y3, s_z3))
    glEnd()

def rotation():
    pygame.display.set_caption("3D Rotation")
    angle = math.pi/4 
    x1,y1,z1 = (-10,17,20)
    x2,y2,z2 = (50,74,30)
    x3,y3,z3 = (10,20,30)

    #using x-axis rotation
    r_matrix = [[1,0,0,0],[0,math.cos(angle),-math.sin(angle),0],[0,math.sin(angle),math.cos(angle),0],[0,0,0,1]]
    #s_matrix = [[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0,0,0,1]]

    h_coordinate = [[x1,x2,x3],[y1,y2,y3],[z1,z2,z3],[1,1,1]]
    #initial triangle
    glBegin(GL_TRIANGLES)

    glColor3f(255.0, 0, 0)
    glVertex3fv((x1,y1,z1))
    glVertex3fv((x2,y2,z2))
    glVertex3fv((x3,y3,z3))	
    glEnd()


    ans = np.dot(r_matrix, h_coordinate)
    #Rotated triangle
    r_x1,r_y1,r_z1 = (ans[0][0], ans[1][0], ans[2][0])
    r_x2,r_y2,r_z2= (ans[0][1], ans[1][1], ans[2][1])
    r_x3,r_y3,r_z3= (ans[0][2], ans[1][2], ans[2][2])
    
    glBegin(GL_TRIANGLES)

    glColor3fv((0, 0, 1))
    glVertex3fv((r_x1,r_y1,r_z1))
    glVertex3fv((r_x2,r_y2, r_z2))
    glVertex3fv((r_x3,r_y3, r_z3))
    glEnd()




def main():
    pygame.init()
    display = (700,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(120, (display[0]/display[1]), 0.0, 200.0)

    glTranslatef(-20,-20,-100 )
    #glTranslatef(0,0,-200 )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    
    
        #uncomment this line to rotate the axes 
        # glRotatef(0.5, 0, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glBegin(GL_LINES)
        #draw line for x axis
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(200.0, 0.0, 0.0)
        # draw line for y axis
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 200.0, 0.0)
        # draw line for Z axis
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 200.0) 
        glEnd()


        #translate()
        #scaling()
        rotation()
        pygame.display.flip()
        pygame.time.wait(10)


main()


