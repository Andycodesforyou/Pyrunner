# at 18:45 framerate can change notes
# at 2:47:29


"""
git init
git status
git add
git rm
git commit -m ""

"""

import pygame
from sys import exit
from random import randint

#Display Score Function
def display_score():
    current_time = int((pygame.time.get_ticks() - start_time ) / 1000)
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf, score_rect)
    return current_time

#Title + Score + Instructions
def display_title():
    title_surf = test_font.render('Pyrunner', False, 'White')
    title_rect = title_surf.get_rect(center = (400,50))
    screen.blit(title_surf, title_rect)

#Obstacle movement
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False

    return True
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Py Runner")

#clock
clock = pygame.time.Clock()

#Font test
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

#game variables
game_active = False
start_time = 0 
score = 0

#Background surfaces
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
display_score()
#Text surface

# score_surface = test_font.render('My game', False, (64,64,64)).convert()
# score_rect = score_surface.get_rect(center = (400, 50))


#Obstacles
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
#snail_rect = snail_surface.get_rect(midbottom = (600, 300))

fly_surface = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()

obstacle_rect_list = {}


#Player Surface & stuff
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0   
#intro Screen 
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400,200))

#Game Message
game_message = test_font.render('Press space to run', False, 'White')
game_message_rect = game_message.get_rect(center = (400, 350))


#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1800)

#Game/event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #Keyboard & Mouse stuff
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos): 
                    if player_rect.bottom == 300:
                        player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20

        
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                     game_active = True
                    #  snail_rect.left = 800
                     start_time = pygame.time.get_ticks()
    
        

        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(snail_surface.get_rect(midbottom = 
            (randint(900, 1100), 300)))
            else:
                obstacle_rect_list.append(fly_surface.get_rect(midbottom = 
            (randint(900, 1100), 150)))
        

    if game_active:
        #Background
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        score = display_score()
        #text/score
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 20)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # screen.blit(score_surface, score_rect)
        #snail animation 
        # snail_rect.x -=4
        # if snail_rect.x < -100:
        #     snail_rect.x = 880
        #Snail
        # screen.blit(snail_surface, snail_rect)
        

        #Player & input
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surface, player_rect)
        #Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        #Collision
        game_active = collisions(player_rect,obstacle_rect_list)

        # if snail_rect.colliderect(player_rect):
        #     game_active = False
 
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        display_title()
        score_message = test_font.render(f'Your score: {score}', False, 'White')
        score_message_rect = score_message.get_rect(center = (400, 350))

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)
    
    
    pygame.display.update()
    clock.tick(60)