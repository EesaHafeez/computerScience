#Using Pygame, draw a red circle with a radius of 50 pixels in the center of the window.

import pygame
pygame.init()
 
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('My first game')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.draw.circle(screen, 'red',[300,300], 50, 0)
        pygame.display.update()

