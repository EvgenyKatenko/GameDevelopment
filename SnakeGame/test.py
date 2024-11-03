
from GameElements.Snake import Snake

def test_snake_creation() -> None:
    snake = Snake()

def test_snake_move() -> None:
    snake = Snake()
    snake.move()

def test_snake_say() -> None:
    snake = Snake()
    snake.saySmth("I'm the best snake in the world!")

if __name__ == "__main__":
    test_snake_say()