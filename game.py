from player import Player
from computer import Computer

class Game:
    def __init__(self, size=10):
        self.player = Player(size)
        self.computer = Computer(size)
        self.size = size
    
    def start(self):
        print("Starting game...")
        self.player.board_set_up()
        self.computer.random_arrange()
    
    def print_boards(self):
        print("Player's board:")
        self.player.board.print_board()
        print("Computer's board:")
        self.computer.board.print_board()


