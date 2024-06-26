import pygame
from simulation_entities.reflector_class import ReflectorSimulation
from simulation_entities.sun_class import SunSimulation
from simulation_entities.tower_class import TowerSimulation
from simulation_entities.focuspoint_class import FocusPoint
from math import *
from simulation_entities.angles_class import Angles
import sys
from typing import Callable
from simulation_entities.linearfx_class import LinearFx
from algebra_functions import get_linear_intersection, get_linear_from_points
from pygame.math import Vector2
from screen import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
pygame.font.init()

font = pygame.font.SysFont('Comic Sans MS', 14)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_color = (234, 245, 255)

clock = pygame.time.Clock()

tower_simulation = TowerSimulation(screen)
focus_point = FocusPoint((200, 200))

sun_simulation = SunSimulation(scale=3)
sun_simulation.angle_y = 30
sun_simulation.distance = SCREEN_WIDTH / 1.8

def is_day():
    return sun_simulation.angle_y > 0 and sun_simulation.angle_y < 180

def create_reflectors(n: int, f: Callable[[int], int]):
    return list(map(lambda item: ReflectorSimulation(axis_pos=(f(item), SCREEN_HEIGHT - 20)), range(n)))

def reflectors_distribution_func(x: int):
    return (screen.get_width() / 2 - 400) + 50 * x #** (1/1.09)

def get_alpha_angle(coordenate_x: int, coordenate_y: int):
    ref_point_sun_distance_y = sun_simulation.distance * sin(radians(sun_simulation.angle_y))
    ref_point_sun_distance_x = sun_simulation.distance * cos(radians(sun_simulation.angle_y))
    diff_distance_x = (SCREEN_WIDTH / 2) - coordenate_x
    diff_distance_y = (SCREEN_WIDTH / 2) - coordenate_y
    alpha_angle = degrees(atan((ref_point_sun_distance_y - diff_distance_y) / (ref_point_sun_distance_x + diff_distance_x)))
    return alpha_angle if alpha_angle > 0 else 180 + alpha_angle

simulation_reflectors = create_reflectors(20, reflectors_distribution_func)

def create_caption(surface, list_caption: list):
    line_spacing = 20
    margin_top = 10
    for index, caption in enumerate(list_caption):
        text, color = caption
        pygame.draw.circle(surface, color, (10, index * line_spacing + 10 + margin_top), 5)
        surface.blit(font.render(text, 0, '#111111'), (20, index * line_spacing + margin_top))

def draw_fx(fx: LinearFx):
    for i in fx.interval:
        pygame.draw.circle(screen, 'red', (i, fx.calc(i)), 1)

dragging = False
running = True
while running:
    light_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()

    if event.type == pygame.MOUSEBUTTONDOWN:
        dragging = True
    if event.type == pygame.MOUSEBUTTONUP:
        dragging = False

    if dragging:
        pos = pygame.mouse.get_pos()
        focus_point.set_position(pos)

    if pressed[pygame.K_UP]:
       sun_simulation.angle_y += 1
    if pressed[pygame.K_DOWN]:
       sun_simulation.angle_y -= 1

    if pressed[pygame.K_LEFT]:
        for r in simulation_reflectors:
            r.mirror_angles.y += 1
    if pressed[pygame.K_RIGHT]:
        for r in simulation_reflectors:
            r.mirror_angles.y -= 1

    screen.fill(background_color)

    # tower_simulation.draw(screen)
    sun_simulation.update_pos(screen)
    sun_simulation.draw(screen)
    focus_point.draw(screen)

    # line_width = 2
    # area_width = 1600
    # for point in range(int(area_width / line_width)):
    #     end_light_point = ((SCREEN_WIDTH / 2 - (area_width / 2)) + point * line_width, SCREEN_HEIGHT)
    #     linearfx = get_linear_from_points(sun_simulation.center, end_light_point)

    #     for reflector in simulation_reflectors:
    #         intersection = get_linear_intersection(linearfx, reflector.axis_fx)
    #         if intersection:
    #             end_light_point = intersection
    #             break

    #     pygame.draw.line(light_surface, '#F7C50188', sun_simulation.center, end_light_point if not intersection else intersection, line_width)

    # screen.blit(light_surface, (0,0))

    # Drawing all reflectors
    for reflector in simulation_reflectors:
        reflector.draw(screen)
        draw_fx(reflector.axis_fx) 


    # if is_day():
        # Setting reflectors mirror angles
    for reflector in simulation_reflectors:
        focus_distance_x = reflector.axis_pos[0] - focus_point.pos[0]
        focus_distance_y = reflector.axis_pos[1] - focus_point.pos[1] + 18
        angle_y = degrees(atan( focus_distance_y / focus_distance_x)) if focus_distance_x != 0 else 90
        angle_y = angle_y if angle_y > 0 else angle_y + 180
        focus_angle = Angles(180, angle_y)
        alpha_angle = get_alpha_angle(reflector.axis_pos[0], reflector.axis_pos[1])
        reflector.set_mirror_angles(focus_angle, Angles(0, alpha_angle))

    # # Drawing light propagation
    # for reflector in simulation_reflectors:
    #     alpha_angle = get_alpha_angle(reflector.axis_pos[0], reflector.axis_pos[1])
    #     alpha_angle -= reflector.mirror_angles.y * 2

    #     end_reflection_width = (reflector.axis_pos[0] if alpha_angle < 90 else SCREEN_WIDTH - reflector.axis_pos[0])
    #     end_reflection_height = end_reflection_width * tan(radians(alpha_angle))

    #     end_reflection_pos_y = SCREEN_HEIGHT + (-end_reflection_height if alpha_angle < 90 else end_reflection_height)
    #     end_reflection_pos_x = 0 if alpha_angle < 90 else SCREEN_WIDTH
    #     end_reflection_pos = (end_reflection_pos_x, end_reflection_pos_y)

    #     pygame.draw.line(screen, '#F7C501', sun_simulation.center, reflector.axis_pos, 3) # incident
    #     pygame.draw.line(screen, '#F7C501', reflector.axis_pos, end_reflection_pos, 3) # reflection


    # Display Information
    create_caption(screen, [
        (f'SUN ANGLE = {sun_simulation.angle_y}', '#F7900B'),
    ])


    pygame.display.flip()
    clock.tick(60)

pygame.quit()