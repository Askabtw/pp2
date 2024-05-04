import pygame
import datetime

pygame.init()

HEIGHT, WIDHT = 600, 600
screen = pygame.display.set_mode(size = (HEIGHT, WIDHT))
clock = pygame.time.Clock()
pygame.display.set_caption('redball')

RED = (255, 0, 0)
y, x =HEIGHT //2, WIDHT //2
rad = 25
speed = 20
running = True
while running:
    screen.fill((155, 155, 155))
    keys = pygame.key.get_pressed()

    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if keys[pygame.K_LEFT] and x >= rad:
        x -= speed
    if keys[pygame.K_RIGHT] and x<= WIDHT - rad:
        x += speed
    if keys[pygame.K_UP] and y >= rad:
        y -= speed
    if keys[pygame.K_DOWN] and y <= HEIGHT - rad:
        y += speed

    

    pygame.draw.circle(screen, RED, (x, y), rad)

    pygame.display.flip()

    clock.tick(60)