from shapes.shapes import create_shape, list_shapes
from shapes.geometry.utils import is_right_angled

# использование
print(list_shapes()) # доступные для создания фигуры

circle = create_shape("circle", radius=5)
print("Площадь круга:", circle.area())

triangle = create_shape("triangle", a=3, b=4, c=5)
print("Площадь треугольника:", triangle.area())
print("Является ли треугольник прямоугольным:", is_right_angled(triangle))


# добавить фигуру 

from shapes.shapes.base import Shape
from shapes.shapes.registry import register_shape
class Rectangle(Shape):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d 
        
    def _compute_area(self):
        return self.a * self.b 
    
    def _is_valid(self):
        return all(side > 0 for side in (self.a, self.b, self.c, self.d))
    
register_shape("rectangle", Rectangle)

rect = Rectangle(4, 5, 6, 3)
print("Площадь прямоугольника:", rect.area())