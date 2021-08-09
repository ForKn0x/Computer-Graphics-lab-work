import numpy as np

def translation(x,y, tx, ty):
    mat =([x],
        [y],
        [1])

    transformMat = ([1,0,tx],[0,1,ty],[0,0,1])

    translatedPoints = np.dot(transformMat, mat)

    return translatedPoints[0],translatedPoints[1]

def rotation(x,y, angle):
    angle = np.math.radians(angle)
    mat =([x],
        [y],
        [1])

    transformMat = ([np.math.cos(angle),-np.math.sin(angle),0],[np.math.sin(angle),np.math.cos(angle),0],[0,0,1])

    translatedPoints = np.dot(transformMat, mat)

    return translatedPoints[0],translatedPoints[1]

def scaling(x,y,sx,sy):
    mat =([x],
        [y],
        [1])

    transformMat = ([sx,0,0],[0,sy,0],[0,0,1])

    translatedPoints = np.dot(transformMat, mat)

    return translatedPoints[0],translatedPoints[1]

def shearingX(x,y,shx):
    mat =([x],
        [y],
        [1])
    
    transformMat = ([1,shx,0],[0,1,0],[0,0,1])

    translatedPoints = np.dot(transformMat, mat)

    return translatedPoints[0],translatedPoints[1]

def shearingY(x,y,shy):
    mat =([x],
        [y],
        [1])
    
    transformMat = ([1,0,0],[shy,1,0],[0,0,1])

    translatedPoints = np.dot(transformMat, mat)

    return translatedPoints[0],translatedPoints[1]

def reflection(x,y):
    mat =([x],
        [y],
        [1])
    
    transformMat = ([0,1,0],[1,0,0],[0,0,1])

    translatedPoints = np.dot(transformMat, mat)

    return translatedPoints[0],translatedPoints[1]