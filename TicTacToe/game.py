import board
import agent

class Game:
    def __init__(self, userPlayer: int, agentPlayer: int):
        self.board = board.Board()
        self.agent = agent.Agent(agentPlayer)
        self.userPlayer = userPlayer
        self.finished = False

    def promptUser(self):
        col = input(f"Please enter the column of your move (1, 2, 3): ")
        row = input(f"Please enter the row of your move (1, 2, 3)(0 to escape): ")
        if row == 0:
            return
        if col not in ('1', '2', '3') or row not in ('1', '2', '3'):
            print("\033[31mPlease enter a valid space.\033[0m")
            return
        col = int(col)
        row = int(row)
        self.turn((col - 1, row - 1), self.userPlayer)

    def turn(self, move: tuple[int, int], player: int):
        col, row = move
        status = self.board.put(col, row, player)
        if status == 2:
            self.board.out()
            print(f"Player {self.board.x_or_o[player]} wins!")
            self.finished = True
        elif status == 1:
            self.board.out()
            print("Board full. Game ends in a tie.")
            self.finished = True

if __name__=="__main__":
    g = Game(0, 1) # Game always has user go first. Fix to be more general
    while(not g.finished):
        g.board.out()
        g.promptUser()
        g.board.out()
        try:
            g.turn(g.agent.choose(g.board), g.agent.x_or_o)
        except ValueError as e:
            print(e)
            g.finished = True
