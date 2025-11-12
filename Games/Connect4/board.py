import numpy
from typing import Optional

class Board:
 
    colors = ('●', '○')
    below = 6
    right = 7
    left = -1
    above = -1
    
    def __init__(self):
        self.board = numpy.full([self.below, self.right], '·', dtype='U1')
        self.nextSpots = [5, 5, 5, 5, 5, 5, 5]

    def put(self, x: int, player: str) -> Optional[str]:
        if self.nextSpots[x] == self.above:
            raise ValueError("\033[31mError: Column is full.\033[0m")
        self.board[self.nextSpots[x]][x] = player
        if self.checkVictory(x, self.nextSpots[x], player):
            return self.checkVictory(x, self.nextSpots[x], player)
        if self.checkFull():
            return ' '
        self.nextSpots[x] -= 1
        return None

    def checkVictory(self, x: int, y: int, player: str) -> Optional[str]:
        hor, ver, diag, adiag = 1, 1, 1, 1
        connect = 4
        for i in range(1, connect):
            if y + i >= self.below or self.board[y + i][x] != player: break
            else: ver += 1
        if ver >= connect: return self.board[y][x]

        for i in range(1, connect):
            if x + i >= self.right or self.board[y][x + i] != player: break
            else: hor += 1
        if hor >= connect: return self.board[y][x]
        for i in range(1, connect):
            if x - i <= self.left or self.board[y][x - i] != player: break
            else: hor += 1
        if hor >= connect: return self.board[y][x]

        for i in range(1, connect):
            if x - i <= self.left or y - i <= self.above or self.board[y - i][x - i] != player: break
            else: diag += 1
        if diag >= connect: return self.board[y][x]
        for i in range(1, connect):
            if x + i >= self.right or y + i >= self.below or self.board[y + i][x + i] != player: break
            else: diag += 1
        if diag >= connect: return self.board[y][x]

        for i in range(1, connect):
            if x - i <= self.left or y + i >= self.below or self.board[y + i][x - i] != player: break
            else: adiag += 1
        if adiag >= connect: return self.board[y][x]
        for i in range(1, connect):
            if x + i >= self.right or y - i <= self.above or self.board[y - i][x + i] != player: break
            else: adiag += 1
        if adiag >= connect: return self.board[y][x]

        return None

    def checkFull(self) -> bool:
       return all(x == -1 for x in self.nextSpots)

    def out(self) -> None:
        print("  A  B  C  D  E  F  G")
        print(numpy.array2string(self.board, separator="  ", formatter={'all': lambda x: x}).replace("[", " ").replace("]", ""))     # type: ignore
