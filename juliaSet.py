import pygame
import math as m
import random
import numpy as np
import time
import cmath
import colorsys
pygame.init()
 
displayInfo = pygame.display.Info()
width = displayInfo.current_w#1920 
height = displayInfo.current_h#1080
hWidth = width//2
hHeight = height//2
screen = pygame.display.set_mode([width,height])


def hsv2rgb(h,s,v):
	return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))
	

def coordToColour(x,y):
	
	iteration = 0
	z = complex((x/width+xMove)*res/zoom,(y/height +yMove)*res/zoom)
	
	while iteration < 100 and abs(z) < escape:	
		z = z**2 + c
		iteration += 1
	
	colour = hsv2rgb(iteration/100,1,1)
	pygame.draw.rect(screen,colour,(x*res,y*res,res,res))
	
	
def keyListen():
	global res
	global c
	global zoom 
	global xMove
	global yMove
	
	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_RIGHT]:
		res += 1
	if keys[pygame.K_LEFT]:
		res -= 1
	if keys[pygame.K_UP]:
		c += 0.001
	if keys[pygame.K_DOWN]:
		c -= 0.001
	if keys[pygame.K_w]:
		yMove -= 0.01
	if keys[pygame.K_s]:
		yMove += 0.01
	if keys[pygame.K_a]:
		xMove -= 0.01
	if keys[pygame.K_d]:
		xMove += 0.01
	if keys[pygame.K_SPACE]:
		zoom += 0.01
	if keys[pygame.K_LCTRL]:
		zoom += 0.01



def main():
	
	
	running = True
	while running:
		
		#pygame events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
		
		#other
		c = complex (h,j)
		keyListen()
		
		for x in range (width//res):
			for y in range (height//res):
				coordToColour(x,y)
		pygame.display.update()
		
		
	
h
#variables
escape = 100
#c = complex (-0.5264529058,0.5199837174)
c = complex (0.355,0.355)
res = 15
h = 0.355
j = 0.355
zoom = 10
xMove = 0.5
yMove = 0.5

#main loop
main()
