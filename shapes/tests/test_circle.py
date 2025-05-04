import pytest
import math
from ..shapes.circle import Circle

@pytest.mark.parametrize(
    "radius, expected_area",
    [
        (1, math.pi),
        (2, math.pi * 4),
        (0.5, math.pi * 0.25),
    ]
)
def test_circle_area_valid(radius, expected_area):
    circle = Circle(radius)
    assert circle.area() == expected_area

@pytest.mark.parametrize(
    "radius",
    [-1, 0, -5.5]
)
def test_circle_area_invalid(radius):
    with pytest.raises(ValueError):
        Circle(radius).area()