#1 import packages
import pygame
from pygame.locals import *
import sys
import random

#2 defines constants
black=(0,0,0)
window_width=640
window_height=480
frames_per_second=45
ball_width_heidth=100
max_width=window_width - ball_width_heidth
max_height=window_height- ball_width_heidth

#3 initialize the word
pygame.init()
window=pygame.display.set_mode(window_width,window_height)
clock=pygame.time.Clock()

#4 load assets: images,sounds etc
ballimage=pygame.image.load('C:\m PYTHON\Highresolutionimage.jpg')

#5 initialize variables
ballx=random.randomrange(max_width)
bally=random.randomrange(max_height)
ballrect=pygame.Rect(ballx,bally,ball_width_heidth,ball_width_heidth)

#6 loop forver
while True:
    #7 check for and handle events
    for event in pygame.eventget():
        #8 clicked the close button? quit pygame and and the programe
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        # see if user clicked
        if event.type==pygame.MOUSEBUTTONUP:        
        # mouseX, mouseY = event.pos # Could do this if we needed it
   
        # check if the click was in the rect of the ball
        # if so, choose a random location
            if ballrect.collidpoint(event.pos):
                ballx=random.range(max_width)    
                bally=random.range(max_height)
                ballrect=pygame.Rect(ballx,bally,ball_width_heidth,ball_width_heidth)

    #9 Do any pre-frame actions
    
    #10 Clear the window
    window.fill(black)

    #draw all window element
    window.blit(ballimage, (ballx,bally)) 
   
    #11 Update the window 
    pygame.display.update()

    #12 slow things down a bit
    clock.tick(frames_per_second)
