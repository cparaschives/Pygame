#!/usr/bin/env python
import pygame
pygame.init()

width=1400
height=1000

screen = pygame.display.set_mode((width,height))

pygame.display.set_caption("Microbial_Mayhem")

isRunning = True

#Loading microbe_1
player_1 = pygame.image.load("/Users/pfb23/Desktop/bacterium_images/cropped/M1.png").convert_alpha()
player_2 = pygame.image.load("/Users/pfb23/Desktop/bacterium_images/cropped/M2.png").    convert_alpha()
   
w = player_1.get_width()
h = player_1.get_height()

w = player_2.get_width()
h = player_2.get_height()

player_1_size=pygame.transform.scale(player_1, (w*0.4, h*0.4))
player_1_rotate=pygame.transform.rotate(player_1_size, -20)

player_2_size=pygame.transform.scale(player_2, (w*0.4, h*0.4))
player_2_rotate=pygame.transform.rotate(player_2_size, -20)

#Specifying the X and Y Coordinate
player1_X = 375 
player1_Y = 500 

player2_X = 700 
player2_Y = 650 

X_change = 0 
Y_change = 0 
while(isRunning ==True):
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Y_change-=0.5
            if(event.key == pygame.K_DOWN):
                Y_change+=0.5
            if event.key == pygame.K_LEFT:
                X_change-=0.5
            if event.key == pygame.K_RIGHT:
                X_change+=0.5
        if event.type == pygame.KEYUP:
# To stop the increase in X change and Ychange
            Y_change=0
            X_change=0
    player1_X+=X_change
    player1_Y+=Y_change
    player2_X+=X_change
    player2_Y+=Y_change

    screen.blit(player_1_rotate,(player1_X, player1_Y))
    screen.blit(player_2_rotate,(player2_X, player2_Y))
    pygame.display.update()

pygame.quit()
