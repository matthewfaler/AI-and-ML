import numpy
from typing import Optional

class Board:
    width = 3
    height = 3

    def __init__(self):
        self.board = numpy.full([self.height, self.width], ' ', dtype='U1')

    def put(self, x: int, y: int, player: str) -> Optional[str]:
        if self.board[y, x] != ' ':
            raise ValueError("Please select empty space.")
        self.board[y, x] = player
        if self.checkVictory(): return self.checkVictory()
        if self.checkFull(): return ' '
        return None

    def checkVictory(self) -> Optional[str]:
        if self.board[0, 0] == self.board[0, 1] == self.board[0, 2] and self.board[0, 1] != ' ': return self.board[0, 1]
        if self.board[1, 0] == self.board[1, 1] == self.board[1, 2] and self.board[1, 1] != ' ': return self.board[1, 1]
        if self.board[2, 0] == self.board[2, 1] == self.board[2, 2] and self.board[2, 1] != ' ': return self.board[2, 1]
        if self.board[0, 0] == self.board[1, 0] == self.board[2, 0] and self.board[1, 0] != ' ': return self.board[1, 0]
        if self.board[0, 1] == self.board[1, 1] == self.board[2, 1] and self.board[1, 1] != ' ': return self.board[1, 1]
        if self.board[0, 2] == self.board[1, 2] == self.board[2, 2] and self.board[1, 2] != ' ': return self.board[1, 2]
        if self.board[0, 0] == self.board[1, 1] == self.board[2, 2] and self.board[1, 1] != ' ': return self.board[1, 1]
        if self.board[0, 2] == self.board[1, 1] == self.board[2, 0] and self.board[1, 1] != ' ': return self.board[1, 1]
        return None

    def checkFull(self) -> bool:
        return not numpy.any(self.board == ' ')

    def togglePlayer(self) -> None:
        self.player = 1 - self.player

    def out(self) -> None:
        print("   1   2   3")
        print(f" 1 {self.board[0, 0]} | {self.board[0, 1]} | {self.board[0, 2]}")
        print("  -----------")
        print(f" 2 {self.board[1, 0]} | {self.board[1, 1]} | {self.board[1, 2]}")
        print("  -----------")
        print(f" 3 {self.board[2, 0]} | {self.board[2, 1]} | {self.board[2, 2]}")

    def spaceValue(self, x: int, y: int) -> str:
        return self.board[y, x]

    def undo(self, x: int, y: int) -> None:
        self.board[y, x] = ' '

if __name__ == "__main__":
    b = Board()
    b.out()
