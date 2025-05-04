from math import pi
from .base import Shape
from .registry import register_shape

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius ** 2
    
register_shape("circle", Circle)