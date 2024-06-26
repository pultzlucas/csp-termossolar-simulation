from simulation_entities.linearfx_class import LinearFx

def get_linear_intersection(f1: LinearFx, f2: LinearFx):
    intersection_x = (f2.c - f1.c) / (f1.m - f2.m)
    intersection_y = f1.m * intersection_x + f1.c
    if int(intersection_x) in f2.interval:
        return intersection_x, intersection_y

def get_linear_from_points(point1: tuple[int, int], point2: tuple[int, int]) -> LinearFx:
    x1, y1 = point1
    x2, y2 = point2
    m = (y2 - y1) / (x2 - x1)
    c = y1 - m * x1
    return LinearFx(m, c)
