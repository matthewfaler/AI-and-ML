from abc import ABC, abstractmethod
import board

class agent(ABC):
    def __init__(self, player: int):
        self.player = player

    @abstractmethod
    def choose(self, board: board.Board) -> int:
        """Return the col of the agent's chosen move."""
        pass
