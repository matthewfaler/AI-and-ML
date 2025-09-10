from game import Game

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
