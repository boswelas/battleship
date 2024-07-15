from game import Game
from ship import Ship

def make_ships():
    defaultShips = {"Carrier": 5, "Battleship": 4, 
                    # "Cruiser": 3, "Submarine": 3, "Destroyer": 2
                    }
    ships = []
    
    for key, value in defaultShips.items():
        ships.append(Ship(key, value))
     
    return ships

def board_set_up(availableShips, game):
    game.print_board()
    while availableShips:
            print(f"Here are your available ships: ")
            print(f"Name ----- Size:")
            for ship in availableShips:
                print(ship.return_name(), "-", ship.return_size())
            user_input = input("Enter the name of the ship you want to place (or 'quit' to exit): ").strip()
            if user_input.lower() == 'quit':
                print(f"Goodbye.")
                break
            selected_ship = next((ship for ship in availableShips if ship.return_name().lower() == user_input.lower()), None)
            if selected_ship:
                print(f"You selected {selected_ship.return_name()} with size {selected_ship.return_size()}.")
                quard = input(f"Where would you like to place the ship?").strip()
                response = input(f"Would you like the ship horizontal or vertical?")
                if response.lower() == "horizontal":
                    res = True
                else:
                    res = False
                if game.check_move(selected_ship, int(quard[0]), int(quard[2]), res):
                    game.place_ship(selected_ship, int(quard[0]), int(quard[2]), res)
                    game.print_board()
                    availableShips.remove(selected_ship)
                else:
                    print(f"Invalid move. Try again")
                    game.print_board()
            else:
                print("Invalid ship name. Please try again.")
    return
    

def play_game():
    availableShips = make_ships()
    game = Game()
    board_set_up(availableShips, game)
    print("here's your setup: ")
    game.print_board()

          
    
                
if __name__ == "__main__":
    play_game()
