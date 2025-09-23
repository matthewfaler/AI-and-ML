import agents
import board

class Game:
    def __init__(self, userPlayer: int, agentPlayer: int):
        self.board = board.Board()
        self.agent = agents.SimpleAgent(agentPlayer)
        self.userPlayer = 'X' if userPlayer == 0 else 'O'
        self.finished = False

    # Prompts user for input on their turn, 
    # raises error if space is out of bounds
    def promptUser(self):
        col = input(f"Please enter the column of your move (1, 2, 3): ").strip()
        row = input(f"Please enter the row of your move (1, 2, 3)(0 to escape): ").strip()
        if col not in ('1', '2', '3') or row not in ('0', '1', '2', '3'):
            raise ValueError("Please enter a valid space.")
        col = int(col)
        row = int(row)
        if row == 0:
            return
        self.turn((col - 1, row - 1), self.userPlayer)

    # Implement turn-based tictactoe game logic.
    def turn(self, move: tuple[int, int], player: str):
        col, row = move
        
        # Reverse col and row to accomodate numpy indexing.
        status = self.board.put(col, row, player)
        # Check if the game has been won and output winner.
        if status in ('X', 'O'):
            self.board.out()
            print(f"\033[32mPlayer {status} wins!\033[0m")
            self.finished = True
        # Check if the board is full and a tie
        elif status == ' ':
            self.board.out()
            print("Board full. Game ends in a tie.")
            self.finished = True

    def play(self):
        user_turn = self.userPlayer == 0

        if self.userPlayer == 0: self.board.out()
        while not self.finished:
            if user_turn:
                print("Player move:")
                try:
                    self.promptUser()
                except ValueError as e:
                    print(f"\033[31m{e}\033[0m")
                    self.board.out()
                    continue
            else:
                print("Agent move:")
                try:
                    self.turn(self.agent.choose(self.board), self.agent.player)
                except ValueError as e:
                    print(f"\033[31m{e}\033[0m")
                    self.finished = True

            if self.finished:
                break
            self.board.out()
            user_turn = not user_turn
