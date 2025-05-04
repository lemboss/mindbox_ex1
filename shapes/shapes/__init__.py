from .base import Shape
from .registry import create_shape, list_shapes

from .circle import Circle
from .triangle import Triangle

__all__ = ["Shape", "create_shape", "list_shapes"]