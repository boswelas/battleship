from player_base import PlayerBase

class Player(PlayerBase):
    def __init__(self, size=10):
        super().__init__(size)
    
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
                coord = input(f"Where would you like to place the ship? (format: row,col)").strip()
                response = input(f"Would you like the ship horizontal or vertical? (h/v)").strip()
                res = response.lower() == "h"
                start_row, start_col = map(int, coord.split(","))
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

       

