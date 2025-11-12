import board

class Game:
    def __init__(self):
        self.board = board.Board()
        self.finished = False

    def promptPlayer(self) -> None:
        inp = input("Choose which column to play (A-G): ").upper().strip()
        colmap = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6}

        # Check if column is a valid option.
        if inp not in colmap:
            print("Please choose a valid option.")
            return
        
        if self.board.nextSpots[colmap[inp]] == self.board.above:
            print("\033[31mError: Column is full.\033[0m")
            return None;

        self.turn(colmap[inp])

    def turn(self, move) -> None:
        won = self.board.put(move)
        if won:
            self.board.out()
            print(f"Player {self.board.colors[self.board.player]} wins!")
            self.finished = True
        elif self.board.checkFull():
            self.board.out()
            print("It's a draw!")
            self.finished = True

if __name__ == "__main__":
    g = Game()
    while not g.finished:
        g.board.out()
        try:
            g.promptPlayer()
        except ValueError as e:
            print(e)
