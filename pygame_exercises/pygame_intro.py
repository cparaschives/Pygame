#!/usr/bin/env python
import pygame
pygame.init()

SCREEN_WIDTH=1400
SCREEN_HEIGHT=1000

screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player=pygame.Rect((300,250,50,50))

run=True
while run:

 screen.fill((0,0,0))

 pygame.draw.rect(screen, (255, 0,0), player)

 key=pygame.key.get_pressed()
 if key[pygame.K_a]==True:
  player.move_ip(-1,0)
 elif key[pygame.K_d]==True:
  player.move_ip(1,0)
 elif key[pygame.K_w]==True:
  player.move_ip(0,-1)
 elif key[pygame.K_x]==True:
  player.move_ip(0,1)


 for event in pygame.event.get():
  if event.type==pygame.QUIT:
   run=False

 pygame.display.update()

pygame.quit()
