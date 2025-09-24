from .agent import Agent
import board

class MinimaxAgent(Agent):
    def choose(self, board: board.Board) -> tuple[int, int]:
        move, _ = self.minimax(board, True)
        if not move:
            raise ValueError("The agent could not find an empty space.")
        return move

    def minimax(self, board: board.Board, maxPlayer: bool) -> tuple[tuple[int, int] | None, int]:
        # If the winning player is the same as that of the minimax agent, return 1 for victory
        # If the winning player is different from that of the minimax agent, return -1 for loss
        winner = board.checkVictory()
        if winner:
            return None, 1 if winner == self.player else -1

        # If board is full and already checked winner, return 0 for a tie
        if board.checkFull():
            return None, 0

        # Set the symbol of the player that is not the minimax agent
        min_play = 'X' if self.player == 'O' else 'O'

        # Declare bestMove variable that will hold optimal move
        bestMove: tuple[int, int] | None = None

        # Minimax agent evaluates its own moveset
        if maxPlayer:
            bestValue = -9999
            for i in range(board.width):
                for j in range(board.height):
                    if board.spaceValue(i, j) == ' ':
                        board.put(i, j, self.player)
                        _, val = self.minimax(board, not maxPlayer)
                        board.undo(i, j)
                        if val > bestValue:
                            bestMove = (i, j)
                            bestValue = val

        # Minimax agent evaluates its adversary's moveset
        else:
            bestValue = 9999
            for i in range(board.width):
                for j in range(board.height):
                    if board.spaceValue(i, j) == ' ':
                        board.put(i, j, min_play)
                        _, val = self.minimax(board, not maxPlayer)
                        board.undo(i, j)
                        if val < bestValue:
                            bestMove = (i, j)
                            bestValue = val
        return bestMove, bestValue
