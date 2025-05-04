from abc import ABC, abstractmethod

class Shape(ABC):
    def area(self):
        if not self._is_valid():
            raise ValueError(f"Неправильные значения аргументов: {self.__dict__}")
        return self._compute_area()

    @abstractmethod
    def _compute_area(self):
        pass

    @abstractmethod
    def _is_valid(self):
        pass