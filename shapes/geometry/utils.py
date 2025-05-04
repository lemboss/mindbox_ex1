import math
from shapes.shapes.triangle import Triangle 

def is_right_angled(triangle: Triangle) -> bool:
    sides = sorted([triangle.a, triangle.b, triangle.c])
    return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)