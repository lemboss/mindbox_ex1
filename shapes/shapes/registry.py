from typing import Type, Dict
from .base import Shape

_shape_registry: Dict[str, Type[Shape]] = {}

def register_shape(name: str, cls: Type[Shape]):
    _shape_registry[name] = cls

def create_shape(name: str, **kwargs) -> Shape:
    cls = _shape_registry.get(name)
    if not cls:
        raise ValueError(f"Unknown shape: {name}")
    return cls(**kwargs)

def list_shapes() -> list[str]:
    return list(_shape_registry.keys())