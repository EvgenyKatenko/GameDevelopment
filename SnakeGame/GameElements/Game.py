from pydantic import BaseModel, Field, validator
from GameElements import GameSettings, Food, Snake, Direction

class Game(BaseModel):
    _gameSettings : GameSettings = Field(...)
    _snake : Snake = Field(...)
    _food : Food = Field(...)

    @validator("_gameSettings")
    def settings_all_present(cls, value : GameSettings):
        if value.fieldWidth < 0: 
            raise ValueError("Field width cannot be negative")
    
    def createFood(self) -> None:
        x = 1
        y = 1
        newFood = Food(x,y)
        while self.IsEventSnakeMeetFood(newFood):
            x = 1
            y = 1
            newFood = Food(x,y)
        self._food = newFood
    
    def isEventSnakeMeetFood(self) -> bool:
        return (self._snake.head.x == self._food.x) and (self._snake.head.y == self._food.y)
    
    def isEventSnakeCrossing(self) -> bool:
        return self._snake.isHeadBodyCrossing
    
    def isEventSnakeBeyondField(self) -> bool: 
        x = self._snake.head.x
        y = self._snake.head.y
        return False
    
    def run(self) -> None:
        # (1) check food event (2) may be extend (3) snake moves (4) check borders 
        activeGame : bool = True
        
        foodEvent: bool = self.isEventSnakeMeetFood()

        if foodEvent: 
            self._snake.extend()
        
        self._snake.move()

        if self.isEventSnakeCrossing:
            #TODO: game over
            pass

        if self.isEventSnakeBeyondField: 
            #TODO: game over
            activeGame = False

        if foodEvent:
            activeGame = False
        



