from game import Game

def play_game():
    game = Game()
    game.start()
    game.print_boards()
    game.play_game()

if __name__ == "__main__":
    play_game()
