from GameElements.SnakeBlock import SnakeBlock
from GameElements.Direction import Direction
from dataclasses import dataclass

@dataclass
class Snake:
    blocks: list[SnakeBlock]
    direction: Direction

    def __post_init__(self):
        if self.direction not in Direction: 
            raise ValueError("Provide the acceptable direction!")
        if self.length == 0: 
            raise ValueError("Snake can't be empty")
        #validating the structure of the body
        #TODO: create specific exception for this
        if self.hasTail():
            for idx in range(1,len(self.blocks)):
                blocksDiff = abs(self.blocks[idx].x - self.blocks[idx - 1].x) + abs(self.blocks[idx].y - self.blocks[idx - 1].y) 
                if blocksDiff > 1:
                    raise ValueError("Block structure is wrong!!!")

    def move(self) -> None:
        # first move the body
        for idx in range(self.length-1,0,-1):
            self.blocks[idx].resetPosition(self.blocks[idx-1].x, self.blocks[idx-1].y)
        # finally move the head
        self.blocks[0].move(self.direction)
    
    def hasTail(self) -> bool:
        return len(self.blocks) > 0
    
    def isHeadBodyCrossing(self) -> bool:
        if self.length > 1:
            return self.head in self.body
        return False
    
    @property
    def head(self) -> SnakeBlock:
        return self.blocks[0]
    
    @property
    def body(self) -> list[SnakeBlock]:
        if self.hasTail():
            return self.blocks[1:]
        else:
            return []
    
    @property
    def length(self) -> int:
        return len(self.blocks)
    
    def changeDirection(self, newDirection : Direction) -> bool:
        if (self.direction.value.x + newDirection.value.x == 0) and (self.direction.value.y + newDirection.value.y == 0):
            return False
        self.direction = newDirection
        return True 
    
    def extend(self) -> None:
        newBlock = SnakeBlock(x = 0, y = 0)
        self.blocks.append(newBlock)

    def printSnake(self) -> None:
        print("--------------------------------")
        #print gen info
        print(f"Snake: {len(self.blocks)} elements")
        #print head info
        print(f"Head at {self.head.x}, {self.head.y}")
        #print body info
        if self.body:
            print("Body:")
            for block in self.body:
                print(f"{block.x}, {block.y}")
        print("--------------------------------")
        
        