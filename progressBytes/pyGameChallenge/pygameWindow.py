'''Write a program to create a Pygame window of size 800x600 pixels with the title 'My First Game'. 
Close the window when the user clicks the close button.
'''

import pygame
pygame.init()
 
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('My first game')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
