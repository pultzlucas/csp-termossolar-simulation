import pygame
from pygame.locals import *
pygame.init()
 
# Game Setup
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
 
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    area = pygame.math.Vector2(0, -100)
    light = pygame.math.Vector2(200, -50)


    vec3 = -light.reflect(area)


    vecs = [
        (area, 'black'), 
        (light, 'yellow'), 
        (vec3, 'red'),
    ]

    for vec, color in vecs:
        pygame.draw.line(screen, color, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), (WINDOW_WIDTH / 2 + vec.x, WINDOW_HEIGHT / 2 + vec.y), 3)

    pygame.display.flip()