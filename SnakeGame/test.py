import pytest

import GameElements as GE

def test_snake_creation() -> None:
    snake = GE.Snake()

def test_snake_move() -> None:
    snake = GE.Snake()
    snake.move()

def test_snake_say() -> None:
    snake = GE.Snake()
    snake.saySmth("I'm the best snake in the world!")

if __name__ == "__main__":
    test_snake_say()