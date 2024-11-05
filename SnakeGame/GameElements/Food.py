from dataclasses import dataclass
from typing import Optional

@dataclass
class Food:
    x : int
    y : int
    weight : Optional[int] = 1

    def __post_init__(self):
        if not isinstance(self.x, int) or not isinstance(self.y, int):
            raise TypeError("x and y must be integers")
        if self.weight is not None and not isinstance(self.weight, int):
            raise TypeError("weight must be an integer or None")
        if self.weight is not None and self.weight < 0:
            raise ValueError("weight cannot be negative")