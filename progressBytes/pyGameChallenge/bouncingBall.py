
import pygame
pygame.init()
 
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption('My first game')
x = 575
y = 25
dx= 5
dy = 5

running = True
while running:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x -= dx
    y += dy
    if x <= 25 or x >= 575:
        dx = -dx
    if y <= 25 or y >= 475:
        dy = -dy
    screen.fill('black')
    pygame.draw.circle(screen, 'red' ,([x,y]), 25)
    pygame.display.update()

