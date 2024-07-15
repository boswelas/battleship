class Board:   
    def __init__(self, size):
        self.size = size
        self.board = self.generate_board()
        
    def generate_board(self):
        board = []
        for row in range(self.size):
            a = []
            for column in range(self.size):
                a.append("-")
            board.append(a)
        return board    
    
    def print_board(self):
        for row in self.board:
            print(" ".join(row))
