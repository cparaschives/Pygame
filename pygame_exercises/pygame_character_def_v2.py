import pygame
pygame.init()

SCREEN_WIDTH=800
SCREEN_HEIGHT=600
  
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.image.load("/Users/pfb23/Desktop/bacterium_images/Player1.png")
background = screen.fill((0,0,0))
playerx = 0
playery = 0

while True:
    display.blit(background,(0,0))
    display.blit(player,(playerx,playery))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_a:
                playerx -= 2
            if event.key == K_d:
                playerx += 2
            if event.key == K_w:
                playery -= 2
            if event.key == K_s:
                playery += 2
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
