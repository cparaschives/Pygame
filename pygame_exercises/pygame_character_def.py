#!/usr/bin/env python
import pygame
pygame.init()

width=1400
height=1000

screen=pygame.display.set_mode((width, height))
#pygame.display.set_caption('Microbial Mayhem")

black_colour=(0,0,0)

dead=False

player=pygame.image.load("/Users/pfb23/Desktop/bacterium_images/Player1.png").convert_alpha()
w = player.get_width()
h = player.get_height()

player_size=pygame.transform.scale(player, (w*0.4, h*0.4))
player_rotate=pygame.transform.rotate(player_size, -20)

#player_rotate_move_amount=10
#y_change=0

def add_player_at_location(x,y):
 screen.blit(player_object, (70,70))

#x=(width*0.5)
#y=(height*0.5)

while not dead:
 for event in pygame.event.get(): 
   if event.type==pygame.QUIT:
      dead=True 
#   if event.type==pygame.KEYDOWN:
#      if event.key==pygame.K_UP:
 #        y_change= -player_rotate_move_amount
  #    elif event.key==pygame.K_DOWN:
   #      y_change= player_rotate_move_amount 
 #  if event.type==pygame.KEYUP:
    #  if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
     #    y_change=0
  
 #y +=y_change


add_player_at_location(player_rotate(x,y))
pygame.display.update()
 

pygame.quit()


