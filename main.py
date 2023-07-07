# at 18:45 framerate can change notes
# at 1:40:40 follow along documentation reference draw line - (already done but good practice)

"""
git init
git status
git add
git rm
git commit -m ""

"""

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
score_surface = test_font.render('My game', False, (64,64,64)).convert()
score_rect = score_surface.get_rect(center = (400, 50))

#Snail Surface
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600, 300))


#Player Surface & stuff
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0


#Game/event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #Keyboard stuff
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('jump')

        if event.type == pygame.KEYUP:
            print("key up")
        
    #Mouse stuff

        # if event.type == pygame.MOUSEMOTION:
        #   if player_rect.collidepoint(event.pos): print('collision')

    #Background
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    
    #text/score
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 20)
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    

    screen.blit(score_surface, score_rect)

    #snail animation 
    snail_rect.x -=4

    if snail_rect.x < -100:
        snail_rect.x = 880

    #Snail
    screen.blit(snail_surface, snail_rect)
    
    #Player & input
    player_gravity +=1
    player_rect.y += player_gravity
    screen.blit(player_surface, player_rect)
    
    
    
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump')
 
    #Collision detection
    """if player_rect.colliderect(snail_rect):
        print('collision')"""
    """
    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint((mouse_pos)):
        print(pygame.mouse.get_pressed())
    """
    pygame.display.update()
    clock.tick(60)