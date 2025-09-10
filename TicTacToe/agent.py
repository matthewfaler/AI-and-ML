import board

class Agent:
    def __init__(self, x_or_o: int):
        self.x_or_o = x_or_o

    def choose(self, board: board.Board):
        return (1, 1)
