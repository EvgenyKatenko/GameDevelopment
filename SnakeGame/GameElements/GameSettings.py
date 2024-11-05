from dataclasses import dataclass

@dataclass
class GameSettings:
    fieldWidth : int 
    fieldHeight : int
    speed : int
    snakeColor : str
    foodColor : str