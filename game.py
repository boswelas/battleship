from board import Board

class Game:
    def __init__(self, size=10):
        self.board = Board(size)
        self.ships = []
        
    def add_ship(self, ship):
        self.ships.append(ship)
        
    def check_move(self, ship, start_row, start_col, horizontal=True):
        if horizontal:
            for i in range(ship.size):
                if not (0 <= start_row <= 9) or not (0 <= (start_col + i) <= 9):
                    return False
                if self.board.board[start_row][start_col + i] != "-":
                    return False
        else:
            for i in range(ship.size):
                if not (0 <= (start_row + i) <= 9) or not (0 <= start_col <= 9):
                    return False
                if self.board.board[start_row + i][start_col] != "-":
                    return False
        return True

        
    def place_ship(self, ship, start_row, start_col, horizontal=True):
        if horizontal:
            for i in range(ship.size):
                self.board.board[start_row][start_col + i] = "*"
                ship.positions.append((start_row, start_col + i))
        else:
            for i in range(ship.size):
                self.board.board[start_row + i][start_col] = "*"
                ship.positions.append((start_row + i, start_col))
                
    def print_board(self):
        self.board.print_board()


