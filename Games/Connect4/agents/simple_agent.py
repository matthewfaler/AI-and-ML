from .agent import agent
import board

class simple_agent(agent):
    def choose(self, board: board.Board) -> int:
        for i in range(board.right):
            if board.nextSpots[i] > board.above:
                return i
        raise ValueError("The agent could not find an empty space.")
