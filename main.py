""" 

THE ASSETS FOR THIS GAME OR ARE IN ORIGNAL COURSE PROJECT GITHUB 
here 

https://github.com/clear-code-projects/UltimatePygameIntro

"""




"""
git init
git status
git add (Branch name/ files?)
git add . 
git rm
git commit -m ""
git commit -am ""
git branch
git checkout [commit id], [branch id]
git log 

"""

import pygame
from sys import exit
from random import randint, choice


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1,player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()


        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.5)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()
    
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom  >= 300:
            self.rect.bottom = 300
    
    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        
        if type == 'fly':
            fly_frame1 = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
            fly_frame2 = pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
            self.frames = [fly_frame1, fly_frame2]
            y_pos = 150

        else:
            snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_frame_1, snail_frame_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

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

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
        obstacle_group.empty()
        return False
    else: return True


def player_animation ():
    global player_surface, player_index

    if player_rect.bottom < 300:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):player_index = 0
        player_surface = player_walk[int(player_index)]

    #play walking animation if player is on floor
    #display the jump surface when player is not on floor



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

bg_music = pygame.mixer.Sound('audio/music.wav')

bg_music.play(loops = -1)

#class stuff
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()


#Background surfaces
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
display_score()
#Text surface

# score_surface = test_font.render('My game', False, (64,64,64)).convert()
# score_rect = score_surface.get_rect(center = (400, 50))


#Snail
snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]

#Fly
fly_frame1 = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
fly_frame2 = pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
fly_frames = [fly_frame1, fly_frame2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

obstacle_rect_list = {}


#Player Surface & stuff
player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1,player_walk_2]
player_index = 0
player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()

player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0   


#intro Screen 
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400,200))

#Game Message
game_message = test_font.render('Press space to run', False, 'White')
game_message_rect = game_message.get_rect(center = (400, 350))


#timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1800)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

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
    
        
        if game_active:
            if event.type == obstacle_timer :
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
                #     obstacle_rect_list.append(snail_surface.get_rect(midbottom = 
                # (randint(900, 1100), 300)))
                # else:
                #     obstacle_rect_list.append(fly_surface.get_rect(midbottom = 
                # (randint(900, 1100), 150)))
            
            if event.type == snail_animation_timer:
                if snail_frame_index == 0: snail_frame_index = 1
                else: snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]
            
            if event.type == fly_animation_timer:
                if fly_frame_index == 0: fly_frame_index = 1
                else: fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]
        
        

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
        # player_gravity += 1
        # player_rect.y += player_gravity
        # if player_rect.bottom >= 300: player_rect.bottom = 300
        # player_animation()
        # screen.blit(player_surface, player_rect)
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        #Obstacle movement
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        #Collision
        game_active = collision_sprite()
        # game_active = collisions(player_rect,obstacle_rect_list)

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