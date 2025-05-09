
import pygame
pygame.init()
 
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('My first game')
x = 300
y = 300
running = True
while running:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5
     
    screen.fill('black')
    pygame.draw.rect(screen, 'blue' ,(x,y,120,70))
    pygame.display.update()

