from math import pi
from .base import Shape
from .registry import register_shape

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def _compute_area(self):
        return pi * self.radius ** 2
    
    def _is_valid(self):
        return self.radius > 0
    
register_shape("circle", Circle)