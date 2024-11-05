from dataclasses import dataclass
from GameElements.Direction import Direction
from GameElements.Direction import MoveXY

@dataclass
class SnakeBlock:
    x: int
    y: int

    def move_x(self, v: int) -> None:
        self.x += v

    def move_y(self, v: int) -> None:
        self.y += v

    def move(self, direction: Direction) -> None:
        self.move_x(direction.value.x)
        self.move_y(direction.value.y)
    
    def resetPosition(self, x : int, y: int) -> None:
        self.x = x
        self.y = y

