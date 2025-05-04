from shapes.shapes.base import Shape
from shapes.shapes.registry import register_shape, list_shapes

def test_user_defined_shape():

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
    
    assert "rectangle" in list_shapes()
    rect = Rectangle(4, 5, 6, 3)
    assert rect.area() == 20