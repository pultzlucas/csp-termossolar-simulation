import pygame
from simulation_entities.reflector_class import ReflectorSimulation
from simulation_entities.sun_class import SunSimulation
from simulation_entities.tower_class import TowerSimulation
from math import *
from simulation_entities.angles_class import Angles
import sys
from typing import Callable

pygame.init()
pygame.font.init()

font = pygame.font.SysFont('Comic Sans MS', 14)

SCREEN_WIDTH, SCREEN_HEIGHT = (1000, 700)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

tower_simulation = TowerSimulation(screen)

sun_simulation = SunSimulation(screen)
sun_simulation.angle_y = 30
sun_simulation.distance = SCREEN_WIDTH / 1.8

def create_reflectors(n: int, f: Callable[[int], int]):
    return list(map(lambda item: ReflectorSimulation(axis_pos=(f(item), SCREEN_HEIGHT - 20)), range(n)))

simulation_reflectors = create_reflectors(10, lambda x: (screen.get_width() / 2 - 100) + 60 * x)

def create_caption(surface, list_caption: list):
    line_spacing = 20
    margin_top = 10
    for index, caption in enumerate(list_caption):
        text, color = caption
        pygame.draw.circle(surface, color, (10, index * line_spacing + 10 + margin_top), 5)
        surface.blit(font.render(text, 0, '#111111'), (20, index * line_spacing + margin_top))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()


    if pressed[pygame.K_UP]:
       sun_simulation.angle_y += 1
    if pressed[pygame.K_DOWN]:
       sun_simulation.angle_y -= 1

    screen.fill((234, 245, 255))

    tower_simulation.draw(screen)
    sun_simulation.update_pos(screen)
    sun_simulation.draw(screen)

    # Drawing all reflectors
    for reflector in simulation_reflectors:
        reflector.draw(screen)

    # Setting reflectors mirror angles
    for reflector in simulation_reflectors:
        focus_distance = abs(tower_simulation.receptor_pos[0] + reflector.axis_pos[0])
        focus_angle = Angles(180, degrees(tower_simulation.receptor_pos[1] / focus_distance))
        reflector.set_mirror_angles(focus_angle, Angles(0, sun_simulation.angle_y))

    # Drawing light propagation
    for reflector in simulation_reflectors:
        alpha_angle = sun_simulation.angle_y - (reflector.mirror_angles.y - 90)
        reflection_angle = alpha_angle - (reflector.mirror_angles.y - 90)
        end_reflection_height = (reflector.axis_pos[0] * tan(radians(reflection_angle)))
        end_reflection_pos_y = SCREEN_HEIGHT - end_reflection_height if reflection_angle < 90 else SCREEN_HEIGHT + end_reflection_height
        end_reflection_pos_x = 0 if reflection_angle < 90 else SCREEN_WIDTH
        end_reflection_pos = (end_reflection_pos_x, end_reflection_pos_y)
        pygame.draw.line(screen, '#F7C501', sun_simulation.center, reflector.axis_pos, 3) # incident
        pygame.draw.line(screen, '#F7C501', reflector.axis_pos, end_reflection_pos, 3) # reflection


    # Display Information
    create_caption(screen, [
        (f'SUN ANGLE = {sun_simulation.angle_y}', '#F7900B'),
    ])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()