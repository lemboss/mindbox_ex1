import pytest
from ..shapes.base import Shape

def test_shape_is_abs():
    with pytest.raises(TypeError):
        Shape()