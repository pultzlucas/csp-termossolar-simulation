import pygame
from math import *

class SunSimulation:
    def __init__(self, screen: pygame.Surface) -> None:
        self.radius = 50
        self.distance = 500
        self.center = (0, 0)
        self.angle_y = float()

    def update_pos(self, screen: pygame.Surface):
        self.center = (
            (screen.get_width() / 2) + self.distance * cos(radians(self.angle_y)),
            screen.get_height() - self.distance * sin(radians(self.angle_y)),
        )

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "#F7900B", self.center, self.radius + 10)
        pygame.draw.circle(screen, "#F7C501", self.center, self.radius)