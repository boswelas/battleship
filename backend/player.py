from player_base import PlayerBase

class Player(PlayerBase):
    def __init__(self, size=8):
        super().__init__(size)
    
    def board_set_up(self):
        while self.availableShips:
            print()
            print(f"Here are your available ships: ")
            print(f"Name ----- Size:")
            for ship in self.availableShips:
                print(ship.return_name(), "-", ship.return_size())
            print()
            user_input = input("Enter the name of the ship you want to place (or 'quit' to exit): ").strip()
            if user_input.lower() == 'quit':
                print(f"Goodbye.")
                break
            selected_ship = next((ship for ship in self.availableShips if ship.return_name().lower() == user_input.lower()), None)
            if selected_ship:
                print()
                print("Here's your board:")
                self.board.print_board()
                coord = input(f"Where would you like to place the {selected_ship.return_name()}? (format: letter+number, e.g., a0): ").strip().lower()
                if len(coord) != 2 or not coord[0].isalpha() or not coord[1].isdigit():
                    print("Invalid format. Please enter the coordinates in the format letter+number (e.g., a0).")
                    continue

                col, row = coord[0], coord[1]
                col = ord(col) - ord('a')
                row = int(row)

                if not (0 <= row < self.board.size and 0 <= col < self.board.size):
                    print("Coordinates out of bounds. Please enter values between A-H and 0-7.")
                    continue

                response = input(f"Would you like the ship horizontal or vertical? (h/v): ").strip().lower()
                res = response == "h"
                
                if self.check_move(selected_ship, row, col, res):
                    self.place_ship(selected_ship, row, col, res)
                    self.board.print_board()  
                    self.availableShips.remove(selected_ship)  
                else:
                    print(f"Invalid move. Try again")
                    self.board.print_board()  
            else:
                print("Invalid ship name. Please try again.")
        return

        

