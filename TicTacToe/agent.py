from typing import Tuple
import board

class Agent:
    def __init__(self, x_or_o: int):
        self.x_or_o = x_or_o

    def choose(self, board: board.Board) -> Tuple[int, int]:
        for i in range(board.width):
            for j in range(board.height):
                if board.spaceValue(i, j) == ' ':
                    return (i, j)
        raise ValueError("The agent could not find an empty space.")
