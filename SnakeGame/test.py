
from GameElements.Snake import Snake
from GameElements.SnakeBlock import SnakeBlock
from GameElements.Direction import Direction
from GameElements.Food import Food

#TODO: need to create pyfixture for a default snake 
#1) small snake
#2) long snake for moving and printing

def test_snake_creation() -> None:
    head = SnakeBlock(x=1, y=1, color="red")
    snake = Snake(blocks=[head], direction= Direction.UP)

def test_snake_block() -> None:
    snkBlock = SnakeBlock(x=1, y=2)
    print(snkBlock)

def test_snake_block_move() -> None:
    snkBlock = SnakeBlock(x=1, y=2)
    snkBlock.move_x(1)
    snkBlock.move_y(1)
    assert snkBlock.x == 2
    assert snkBlock.y == 3

def test_snake_print():
    head = SnakeBlock(x=10, y=10)
    body = [SnakeBlock(x=10, y=9), SnakeBlock(x=10, y=8)]

    snake = Snake(blocks=[head] + body, direction=Direction.UP)
    snake.printSnake()

def test_snake_move():
    head = SnakeBlock(x=10, y=10)
    body = [SnakeBlock(x=10, y=9), SnakeBlock(x=10, y=8)]

    snake = Snake(blocks=[head] + body, direction=Direction.UP)
    print("Before move:")
    snake.printSnake()
    snake.move()
    print("After move:")
    snake.printSnake()

    #check if the head is in the correct position
    assert snake.head.x == 10
    assert snake.head.y == 11

def test_snake_extend_and_move():
    head = SnakeBlock(x=10, y=10)
    body = [SnakeBlock(x=10, y=9), SnakeBlock(x=10, y=8)]

    snake = Snake(blocks=[head] + body, direction=Direction.UP)
    print("Before move:")
    snake.printSnake()

    snake.extend()
    snake.move()
    print("After move")
    snake.printSnake()

def test_food_creation():
    food = Food(5,5)

def test_snake_crossing():
    head = SnakeBlock(x=10, y=10)
    body = [SnakeBlock(x=10, y=9), SnakeBlock(x=9, y=9),SnakeBlock(x=9, y=10)]
    snake = Snake(blocks=[head] + body, direction=Direction.UP)
    #TODO: special exception
    if snake.isHeadBodyCrossing():
        raise Exception("Snaked collapsed")


if __name__ == "__main__":
    #test_snake_creation()
    #test_snake_block()
    #test_snake_block_move()
    #test_snake_print()
    #test_snake_move()
    #test_snake_crossing()
    #test_food_creation()
    test_snake_extend_and_move()