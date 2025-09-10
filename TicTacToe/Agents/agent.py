from abc import ABC, abstractmethod
import board

class Agent(ABC):
    def __init__(self, x_or_o: int):
        self.x_or_o = x_or_o

    @abstractmethod
    def choose(self, board: board.Board) -> tuple[int, int]:
        """Return the (col, row) of the agent's chosen move."""
        pass
