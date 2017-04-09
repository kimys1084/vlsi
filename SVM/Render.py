import OpenGL.GL import *
import OpenGL.GLU import *
import OpenGL.GLUT import *

import numpy as np
import DataType as D

WIDTH = 1600
HEIGHT = 1200

Data = 0

def init(Data_):

	global Data = Data_

def reshape(new_width, new_height):
	global WIDTH, HEIGHT

	WIDTH, HEIGHT = new_width, new_height
	glViewport(0,0,WIDTH, HEIGHT)
	

def display():
	


def initializeWindow():

	glutInit(['viewer'])
	glutInitWindowPosition(100,100)
	glutInitWindowSize(WIDTH, HEIGHT)
	glutInitDisplayMode(GLUiT_DOUBLE | GLUT_RGB )
	glutCreateWindow('SVM- 2016-21191 yongsung kim')

	glutReshpaeFunc(reshape)
	glutDisPlayFunc(display)




if __name__ == "__main__":
	render()
