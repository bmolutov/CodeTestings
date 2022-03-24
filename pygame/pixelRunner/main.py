import pygame
import sys
from random import randint

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = test_font.render(f'Score: {current_time // 1000}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time // 1000

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else: 
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if obstacle_rect.colliderect(player):
                return False
    return True

# starts pygame, and helps run our project
pygame.init()

width = 800
height = 400

# creating display surface
screen = pygame.display.set_mode((width, height))
# giving title to our project
pygame.display.set_caption('Runner')
# creating clock, or creating Clock object
clock = pygame.time.Clock()
# creating font
test_font = pygame.font.Font('../assets/font/Pixeltype.ttf', 50)
game_active = True
start_time = 0
score = 0

sky_surf = pygame.image.load('../assets/graphics/Sky.png').convert() # convert() is used to optimize working with external images
ground_surf = pygame.image.load('../assets/graphics/ground.png').convert()

# Obstacles
snail_surf = pygame.image.load('../assets/graphics/snail/snail1.png').convert_alpha()
fly_surf = pygame.image.load('../assets/graphics/Fly/Fly1.png').convert_alpha()

obstacle_rect_list = []

player_surf = pygame.image.load('../assets/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300)) # it draws a rectangle around this surface

player_gravity = 0

# Intro screen
player_stand = pygame.image.load('../assets/graphics/player/player_stand.png').convert_alpha() # importing image
player_stand = pygame.transform.rotozoom(player_stand, 0, 2) # taking the image and updating it
player_stand_rect = player_stand.get_rect(center = (400, 200)) # creating the rectangle

game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 80))

game_message = test_font.render('Press space to run', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (400, 340))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
    # draw all our elements
    # update everything
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # pygame.QUIT stands for x button
            pygame.quit() # opposite to pygame.init()
            sys.exit() # preventing an error (after pygame.quit() main loop must also be closed)

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(pygame.mouse.get_pos()) and player_rect.bottom >= 300:
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()
        
        if event.type == obstacle_timer and game_active:
            if randint(0, 2):
                obstacle_rect_list.append(snail_surf.get_rect(bottomright=(randint(900, 1100), 300)))
            else:
                obstacle_rect_list.append(fly_surf.get_rect(bottomright=(randint(900, 1100), 210)))

    if game_active:
        screen.blit(sky_surf, (0, 0)) # drawing the surface at the topside of its parent
        screen.blit(ground_surf, (0, 300))
        
        score = display_score()

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf, player_rect) # we are taking a surface and placing it on the position of rectangle

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # collision
        game_active = collisions(player_rect, obstacle_rect_list)

    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_name, game_name_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0
        
        score_message = test_font.render(f'Your score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 330))

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)
    
    pygame.display.update() # updates that display surface
    clock.tick(60) # setting fps (update the display at most 60 times per second)
    