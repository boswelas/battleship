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
        header = '  ' + ' '.join('ABCDEFGH'[:self.size])
        print(header)
        
        for i, row in enumerate(self.board):
            print(f"{i} {' '.join(row)}")
