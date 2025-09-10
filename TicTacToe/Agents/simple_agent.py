from .agent import Agent
import board

class SimpleAgent(Agent):
    def choose(self, board: board.Board) -> tuple[int, int]:
        for i in range(board.width):
            for j in range(board.height):
                if board.spaceValue(i, j) == ' ':
                    return (i, j)
        raise ValueError("The agent could not find an empty space.")
