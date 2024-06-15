import pygame
from simulation_entities.angles_class import Angles

class TowerSimulation:
    def __init__(self, screen: pygame.Surface) -> None:
        self.tower_height = screen.get_height() - 300
        self.tower_width = 20
        self.base_height = screen.get_height() - 20
        self.base_width = 80
        self.receptor_height = 50
        self.receptor_width = 40
        self.center_x_pos = 50 + (self.tower_width / 2)
        self.receptor_pos = (self.center_x_pos + 200, self.tower_height - ((self.receptor_height) / 2))
     
    def draw(self, screen: pygame.Surface):
        # pygame.draw.rect(screen, 'gray', (50, self.tower_height, self.tower_width, self.tower_height))
        # pygame.draw.rect(screen, 'gray', (50 + (self.tower_width / 2) - (self.base_width / 2), self.base_height, self.base_width, self.base_height))
        # pygame.draw.rect(screen, 'black', (self.receptor_pos[0], self.receptor_pos[1], self.receptor_width, self.receptor_height))
        pygame.draw.circle(screen, 'black', self.receptor_pos, 10)