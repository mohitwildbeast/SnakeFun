'''
Snake Game- Settings and Configuration File
Author - Mohit Singh (@MohitWildBeast)
'''

import random
import pygame
import sys
from pygame.locals import *

FPS = 5 
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
assert WINDOWHEIGHT % CELLSIZE == 0, "Window Height must be a multiple of Cell Size"
assert WINDOWWIDTH % CELLSIZE == 0, "Window Width must be a multiple of Cell Size"
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

#Colour Codes
#			 R    G    B
WHITE    = (255, 255, 255)
BLACK    = (0,   0,     0)
RED      = (255,   0,   0)
GREEN    = (0,   255,   0)
DARKGREEN= (0,   155,   0)
YELLOW   = (40,   40,  40)

BGCOLOR = BLACK

#Control Keys
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0 #Index of the snake's head

def levelSelect():
	global FPS
	if level == "EASY":
		FPS = 4
	elif level == "MEDIUM":
		FPS = 7
	elif level == "HARD":
		FPS = 10