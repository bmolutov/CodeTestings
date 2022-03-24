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

sky_surface = pygame.image.load('../assets/graphics/Sky.png').convert() # convert() is used to optimize working with external images
ground_surface = pygame.image.load('../assets/graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'Black') # it creates a suface

snail_surface = pygame.image.load('../assets/graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(bottomright=(600, 300))

player_surface = pygame.image.load('../assets/graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(80, 300)) # it draws a rectangle around this surface

while True:
    # draw all our elements
    # update everything
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # pygame.QUIT stands for x button
            pygame.quit() # opposite to pygame.init()
            sys.exit() # preventing an error (after pygame.quit() main loop must also be closed)

    screen.blit(sky_surface, (0, 0)) # drawing the surface at the topside of its parent
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    snail_rectangle.x -= 4
    if snail_rectangle.right <= 0:
        snail_rectangle.left = 800

    screen.blit(snail_surface, snail_rectangle)
    screen.blit(player_surface, player_rectangle) # we are taking a surface and placing it on the position of rectangle

    pygame.display.update() # updates that display surface
    clock.tick(60) # setting fps (update the display at most 60 times per second)