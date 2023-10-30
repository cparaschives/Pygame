#!/usr/bin/env python
import pygame
pygame.init()

width=1400
height=1000

screen = pygame.display.set_mode((width,height))

pygame.display.set_caption("Microbial_Mayhem")

isRunning = True

background=pygame.image.load("/Users/pfb23/Desktop/bacterium_images/background2.png")
background=pygame.transform.scale(background,(width*1,height*1))

#Loading microbe_1
player_1 = pygame.image.load("/Users/pfb23/Desktop/bacterium_images/cropped/M3-transparent.png").convert_alpha()
player_2 = pygame.image.load("/Users/pfb23/Desktop/bacterium_images/cropped/M4-transparent.png").convert_alpha()
   
w = player_1.get_width()
h = player_1.get_height()

w = player_2.get_width()
h = player_2.get_height()

player_1_size=pygame.transform.scale(player_1, (w*0.5, h*0.5))
player_1_rotate=pygame.transform.rotate(player_1_size, -10)

player_2_size=pygame.transform.scale(player_2, (w*0.5, h*0.5))
player_2_rotate=pygame.transform.rotate(player_2_size, -10)

#Specifying the X and Y Coordinate
player1_X = 55 
player1_Y = 400 

player2_X = 700 
player2_Y = 400 

X1_change = 0 
Y1_change = 0 

X2_change = 0
Y2_change = 0 

while(isRunning ==True):
    screen.fill((0,0,0))
    screen.blit(background,(2.5,2))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Y2_change-=10
            if event.key == pygame.K_w:
                Y1_change-=10
           
            if(event.key == pygame.K_DOWN):
                Y2_change+=10
            if(event.key == pygame.K_x):
                Y1_change+=10

            if event.key == pygame.K_LEFT:
                X2_change-=10
            if event.key == pygame.K_a:
                X1_change-=10

            if event.key == pygame.K_RIGHT:
                X2_change+=10
            if event.key == pygame.K_d:
                X1_change+=10

        if event.type == pygame.KEYUP:

# To stop the increase in X change and Ychange
            Y2_change=0
            X2_change=0
            Y1_change=0
            X1_change=0

    player1_X+=X1_change
    player1_Y+=Y1_change
    player2_X+=X2_change
    player2_Y+=Y2_change

    screen.blit(player_1_rotate,(player1_X, player1_Y))
    screen.blit(player_2_rotate,(player2_X, player2_Y))
  
    pygame.display.update()

pygame.quit()

