from enum import Enum, unique, auto
from collections import namedtuple

MoveXY = namedtuple("MoveXY", ["x", "y"])

@unique
class Direction(Enum):
    UP = MoveXY(0,1)
    DOWN = MoveXY(0,-1)
    LEFT = MoveXY(-1,0)
    RIGHT = MoveXY(1,0)
