from board import Board
from ship import Ship

class PlayerBase:
    def __init__(self, size=10):
        self.board = Board(size)
        self.hits_board = Board(size)
        self.ships = []
        self.availableShips = self.make_ships()

    def make_ships(self):
        defaultShips = {
            "Carrier": 5,
            "Battleship": 4,
            "Cruiser": 3, "Submarine": 3, "Destroyer": 2
        }
        ships = []
        
        for key, value in defaultShips.items():
            ships.append(Ship(key, value))
        return ships
       
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
        self.ships.append(ship)
            
    def place_hit(self, row, col):
        self.hits_board.board[row][col] = "H"
        
    def place_miss(self, row, col):
        self.hits_board.board[row][col] = "x"

    
