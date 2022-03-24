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

sky_surface = pygame.image.load('../assets/graphics/Sky.png')
ground_surface = pygame.image.load('../assets/graphics/ground.png')
text_surface = test_font.render('My game', False, 'Black') # it creates a suface

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

    pygame.display.update() # updates that display surface
    clock.tick(60) # setting fps (update the display at most 60 times per second)