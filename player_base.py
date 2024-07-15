import random
from board import Board
from ship import Ship

class PlayerBase:
    def __init__(self, size=10):
        self.board = Board(size)
        self.ships = []
        self.availableShips = self.make_ships()
    
    def make_ships(self):
        defaultShips = {
            "Carrier": 5,
            "Battleship": 4,
            # "Cruiser": 3, "Submarine": 3, "Destroyer": 2
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
    
    def random_arrange(self):
        while self.availableShips:
            selected_ship = random.choice(self.availableShips)
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            horizontal = random.choice([True, False])
            if self.check_move(selected_ship, row, col, horizontal):
                self.place_ship(selected_ship, row, col, horizontal)
                print(f"placed: {selected_ship.name}")
                self.availableShips.remove(selected_ship)
                self.board.print_board()

    def board_set_up(self):
        while self.availableShips:
            print(f"Here are your available ships: ")
            print(f"Name ----- Size:")
            for ship in self.availableShips:
                print(ship.return_name(), "-", ship.return_size())
            user_input = input("Enter the name of the ship you want to place (or 'quit' to exit): ").strip()
            if user_input.lower() == 'quit':
                print(f"Goodbye.")
                break
            selected_ship = next((ship for ship in self.availableShips if ship.return_name().lower() == user_input.lower()), None)
            if selected_ship:
                print(f"You selected {selected_ship.return_name()} with size {selected_ship.return_size()}.")
                quard = input(f"Where would you like to place the ship? (format: row,col)").strip()
                response = input(f"Would you like the ship horizontal or vertical? (h/v)").strip()
                res = response.lower() == "h"
                start_row, start_col = map(int, quard.split(","))
                if self.check_move(selected_ship, start_row, start_col, res):
                    self.place_ship(selected_ship, start_row, start_col, res)
                    self.board.print_board()  
                    self.availableShips.remove(selected_ship)  
                else:
                    print(f"Invalid move. Try again")
                    self.board.print_board()  
            else:
                print("Invalid ship name. Please try again.")
        return
