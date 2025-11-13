import board
import agents

class Game:
    def __init__(self):
        self.board = board.Board()
        self.finished = False
        self.userPlayer = '●'
        self.agentPlayer = agents.simple_agent('○')

    def promptPlayer(self) -> None:
        inp = input("Choose which column to play (A-G): ").upper().strip()
        colmap = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6}

        # Check if column is a valid option.
        if inp not in colmap:
            raise ValueError("\033[31mError: Please choose a valid column.\033[0m")
        
        if self.board.nextSpots[colmap[inp]] == self.board.above:
            raise ValueError("\033[31mError: Column is full.\033[0m")

        self.turn(colmap[inp], self.userPlayer)

    def turn(self, move: int, player: str) -> None:
        status = self.board.put(move, player)
        if status in ('●', '○'):
            self.board.out()
            print(f"Player {status} wins!")
            self.finished = True
        elif status == ' ':
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
            continue
        g.board.out()
        try:
            g.turn(g.agentPlayer.choose(g.board), g.agentPlayer.player)
        except ValueError as e:
            print(e)
