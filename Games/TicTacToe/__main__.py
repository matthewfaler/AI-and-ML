from game import Game

if __name__=="__main__":
    while True:
        choice1 = input("Please enter X or O for which symbol you want to play as: ").strip().upper()
        if choice1 in ('X', 'O'):
            break
        print("\033[31mInvalid choice. Please enter X or O.\033[0m")

    while True:
        choice2 = int(input("Please enter which gaming agent you would like to play against (1: Simple, 2: Minimax): ").strip())
        if choice2 in (1, 2):
            break
        print("\033[31mInvalid choice. Please enter 1 or 2.\033[0m")

    # Map choice to player order
    if choice1 == "X":
        user_player = 0  # User goes first as X
        agent_player = 1
    else:
        user_player = 1  # User goes second as O
        agent_player = 0
    g = Game(user_player, agent_player, choice2)
    g.play()
