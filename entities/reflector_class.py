from simulation_entities.angles_class import Angles

class Reflector:
    def __init__(self, tower_pos_angles: Angles) -> None:
        self.tower_pos_angles = tower_pos_angles
        self.axis_x = 90
        self.axis_y = float()

    def set_axes_angles(self, sun_angles: Angles):
        # self.axis_x = - (sun_angles.x + self.tower_pos_angles.x - 180) / 2
        self.axis_y = (sun_angles.y - self.tower_pos_angles.y ) / 2 + 90
        