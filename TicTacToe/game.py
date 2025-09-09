import board

class Game:
    def __init__(self):
        self.board = board.Board()
        self.finished = False

    def turn(self):
        pname = "X" if self.board.player==0 else "O"
        col = input(f"Player {pname}, please enter the column of your move (1, 2, 3): ")
        row = input(f"Player {pname}, please enter the row of your move (1, 2, 3)(0 to escape): ")
        if row == 0:
            return
        if col not in ('1', '2', '3') or row not in ('1', '2', '3'):
            print("\033[31mPlease enter a valid space.\033[0m")
            return
        col = int(col)
        row = int(row)
        status = self.board.put(col-1, row-1)
        if status == 2:
            self.board.out()
            print(f"Player {pname} wins!")
            self.finished = True
        elif status == 1:
            self.board.out()
            print("Board full. Game ends in a tie.")
            self.finished = True

if __name__=="__main__":
    g = Game()
    while(not g.finished):
        g.board.out()
        g.turn()
