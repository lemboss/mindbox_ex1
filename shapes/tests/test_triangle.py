import pytest
from ..shapes.triangle import Triangle

@pytest.mark.parametrize(
    "a, b, c, expected_area",
    [
        (3, 4, 5, 6.0),
        (5, 12, 13, 30.0),
        (7, 24, 25, 84.0),
    ]
)
def test_triangle_area_parametrized(a, b, c, expected_area):
    t = Triangle(a, b, c)
    assert round(t.area(), 2) == expected_area
    
@pytest.mark.parametrize(
    "a, b, c",
    [
        (0, 4, 5), 
        (3, -4, 5), 
        (1, 2, 10), 
    ]
)
def test_triangle_area_invalid_values(a, b, c):
    with pytest.raises(ValueError):
        Triangle(a, b, c).area()