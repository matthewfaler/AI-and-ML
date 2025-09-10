import agents
import board

class Game:
    def __init__(self, userPlayer: int, agentPlayer: int):
        self.board = board.Board()
        self.agent = agents.SimpleAgent(agentPlayer)
        self.userPlayer = userPlayer
        self.finished = False

    def promptUser(self):
        col = input(f"Please enter the column of your move (1, 2, 3): ")
        row = input(f"Please enter the row of your move (1, 2, 3)(0 to escape): ")
        if col not in ('1', '2', '3') or row not in ('0', '1', '2', '3'):
            raise ValueError("Please enter a valid space.")
        col = int(col)
        row = int(row)
        if row == 0:
            return
        self.turn((col - 1, row - 1), self.userPlayer)

    def turn(self, move: tuple[int, int], player: int):
        col, row = move
        status = self.board.put(col, row, player)
        if status == 2:
            self.board.out()
            print(f"\033[32mPlayer {self.board.x_or_o[player]} wins!\033[0m")
            self.finished = True
        elif status == 1:
            self.board.out()
            print("Board full. Game ends in a tie.")
            self.finished = True

if __name__=="__main__":
    g = Game(0, 1) # Game always has user go first. Fix to be more general
    g.board.out()
    while(not g.finished):
        try:
            g.promptUser()
        except ValueError as e:
            print(f"\033[31m{e}\033[0m")
            g.board.out()
            continue
        if(g.finished): break
        g.board.out()
        print("Agent move:")
        try:
            g.turn(g.agent.choose(g.board), g.agent.x_or_o)
        except ValueError as e:
            print(f"\033[31m{e}\033[0m")
            g.finished = True
        g.board.out()
