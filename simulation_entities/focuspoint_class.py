import pygame

class FocusPoint:
    def __init__(self, initial_pos: tuple[int, int]) -> None:
        self.pos = initial_pos
     
    def set_position(self, pos: tuple[int, int]):
        self.pos = pos

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, 'black', self.pos, 10)