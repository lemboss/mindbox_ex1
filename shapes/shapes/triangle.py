from math import sqrt
from .base import Shape
from .registry import register_shape

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def _compute_area(self):
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def _is_valid(self):
        return all(side > 0 for side in (self.a, self.b, self.c))
    
register_shape("triangle", Triangle)