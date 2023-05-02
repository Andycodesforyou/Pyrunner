# at 18:45 framerate can change notes
# at 1:08:15 follow along (Maybe start a few minutes back)

import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Py Runner")

#clock
clock = pygame.time.Clock()

#Font test
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)


#Background surfaces
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

#Text surface
text_surface = test_font.render('My game', False, 'Black').convert()

#Snail Surface
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600, 300))


#Player Surface
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))

#Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #Background
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300,50))

    #snail animation 
    snail_rect.x -=4

    if snail_rect.x < -100:
        snail_rect.x = 880

    #Snail
    screen.blit(snail_surface, snail_rect)
    
    #Player 
    screen.blit(player_surface, player_rect)


    #Collision detection
    if player_rect.colliderect(snail_rect):
        print('collision')


    pygame.display.update()
    clock.tick(60)