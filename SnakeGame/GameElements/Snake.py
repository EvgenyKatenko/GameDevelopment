from GameElements.SnakeBlock import SnakeBlock
from GameElements.Direction import Direction
from dataclasses import dataclass

@dataclass
class Snake:
    blocks: list[SnakeBlock]
    direction: Direction

    def __post_init__(self):
        assert self.direction in Direction
        assert len(self.blocks) > 0
        #validating the structure of the body
        #TODO: create specific exception for this
        if self.hasTail():
            for idx in range(1,len(self.blocks)):
                assert abs(self.blocks[idx].x - self.blocks[idx - 1].x) + abs(self.blocks[idx].y - self.blocks[idx - 1].y) == 1

    def move(self) -> None:
        # first move the body
        for idx in range(self.length-1,0,-1):
            self.blocks[idx].resetPosition(self.blocks[idx-1].x, self.blocks[idx-1].y)
        # finally move the head
        self.blocks[0].move(self.direction)
    
    def hasTail(self) -> bool:
        return len(self.blocks) > 0
    
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

    def extend(self) -> None:
        newBlock = SnakeBlock(x = 0, y = 0, color = "green")
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
        
        