import pygame
from simulation_entities.angles_class import Angles

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 8)

class ReflectorSimulation:
    def __init__(self, axis_pos: tuple[int, int]) -> None:
        self.mirror_width = 20
        self.mirror_angles = Angles(0, 90)
        self.base_width = 6
        self.axis_pos = axis_pos

    def set_mirror_angles(self, focus_angles: Angles, sun_angles: Angles):
        self.mirror_angles.y = (sun_angles.y - focus_angles.y ) / 2 + 90

    def draw(self, screen: pygame.Surface):
        pygame.draw.line(screen, "black", (self.axis_pos[0], screen.get_height()), self.axis_pos, self.base_width)
        axis_x, axis_y = self.axis_pos
        line_vector = pygame.math.Vector2(self.mirror_width, 0)

        rot_vector = line_vector.rotate(-self.mirror_angles.y + 90)
        start = round(axis_x + rot_vector.x), round(axis_y + rot_vector.y)
        end = round(axis_x - rot_vector.x), round(axis_y - rot_vector.y)

        pygame.draw.line(screen, 'black', start, end, 4)

        # Angle Display
        text_pos = (self.axis_pos[0] - 20, self.axis_pos[1] + 5)
        pygame.draw.rect(screen, (220, 220, 220), (text_pos[0], text_pos[1], 10, 5))
        screen.blit(font.render(str(int(self.mirror_angles.y)) + '°', 0, '#111111'), text_pos)