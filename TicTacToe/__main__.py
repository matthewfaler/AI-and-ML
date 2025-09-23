from game import Game

if __name__=="__main__":
    while True:
        choice = input("Please enter X or O for which symbol you want to play as: ").strip().upper()
        if choice in ('X', 'O'):
            break
        print("\033[31mInvalid choice. Please enter X or O.\033[0m")
    
    # Map choice to player order
    if choice == "X":
        user_player = 0  # User goes first as X
        agent_player = 1
    else:
        user_player = 1  # User goes second as O
        agent_player = 0
    g = Game(user_player, agent_player)
    g.play()
