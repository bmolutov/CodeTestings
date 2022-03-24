import pygame
import sys

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

sky_surf = pygame.image.load('../assets/graphics/Sky.png').convert() # convert() is used to optimize working with external images
ground_surf = pygame.image.load('../assets/graphics/ground.png').convert()
score_surf = test_font.render('My game', False, (64, 64, 64)) # it creates a suface
score_rect = score_surf.get_rect(center=(400, 50))

snail_surf = pygame.image.load('../assets/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright=(600, 300))

player_surf = pygame.image.load('../assets/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300)) # it draws a rectangle around this surface

while True:
    # draw all our elements
    # update everything
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # pygame.QUIT stands for x button
            pygame.quit() # opposite to pygame.init()
            sys.exit() # preventing an error (after pygame.quit() main loop must also be closed)
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                print("collision!")

    screen.blit(sky_surf, (0, 0)) # drawing the surface at the topside of its parent
    screen.blit(ground_surf, (0, 300))
    # pygame.draw.rect(screen, 'Pink', score_rect) # drawing a rectangle
    pygame.draw.rect(screen, '#c0e8ec', score_rect, border_radius=10) # drawing a border
    
    screen.blit(score_surf, score_rect)

    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800

    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect) # we are taking a surface and placing it on the position of rectangle
    
    pygame.display.update() # updates that display surface
    clock.tick(60) # setting fps (update the display at most 60 times per second)
    