import random
from time import sleep
from player import Player
from computer import Computer

class Game:
    def __init__(self, size=8):
        self.player = Player(size)
        self.computer = Computer(size)
        self.size = size
    
    def start(self):
        print("Starting game...")
        print()
        self.player.board.print_board()
        self.player.board_set_up()
        self.computer.random_arrange()
    

    def player_move(self):
        print()
        while True:
            sleep(1)
            print("Here's your opponent's board:")
            self.player.hits_board.print_board()
            coord = input("Where would you like to attack? (format: letter+number, e.g., a0): ").strip().lower()
            print()
            if len(coord) != 2 or not coord[0].isalpha() or not coord[1].isdigit():
                print("Invalid format. Please enter the coordinates in the format letter+number (e.g., a0).")
                continue
            
            col, row = coord[0], coord[1]
            col = ord(col) - ord('a')
            row = int(row)
            
            if not (0 <= row < self.size and 0 <= col < self.size):
                print("Coordinates out of bounds. Please enter values between A-H and 0-7.")
                continue

            if self.player.hits_board.board[row][col] != "-":
                print("This position has already been attacked. Choose a different spot.")
                continue

            hit = False
            for ship in self.computer.ships:
                if (row, col) in ship.positions:
                    print("It's a hit!")
                    self.player.place_hit(row, col)
                    hit = True
                    ship.positions.remove((row, col))
                    if len(ship.positions) == 0:
                        print(ship.name, "has been sank!")
                        self.computer.ships.remove(ship)
                    self.player.hits_board.print_board()
                    break

            if not hit:
                print("Miss!")
                self.player.place_miss(row, col)
                self.player.hits_board.print_board()
            return

    
    def computer_move(self):
        print()
        sleep(1)
        hits = self.computer.return_hits()
        hits_len = len(hits)
        inTurn = True

        while inTurn:
            if hits_len == 0:
                # Random move
                while True:
                    row = random.randint(0, 7)
                    col = random.randint(0, 7)
                    if self.computer.hits_board.board[row][col] == "-":
                        break

                hit = False
                for ship in self.player.ships:
                    if (row, col) in ship.positions:
                        print("The computer made a hit!")
                        self.computer.place_hit(row, col)
                        hit = True
                        self.computer.add_to_hits(row, col, ship.name)
                        ship.positions.remove((row, col))
                        self.player.board.board[row][col] = "H"
                        if len(ship.positions) == 0:
                            print(ship.name, "has been sank!")
                            self.player.ships.remove(ship)
                            # Remove hits of the sunk ship
                            self.computer.hits = [h for h in self.computer.hits if h[2] != ship.name]
                        self.player.board.print_board()
                        inTurn = False

                if not hit:
                    print("The computer missed!")
                    self.computer.place_miss(row, col)
                    self.player.board.print_board()

                return

            elif hits_len == 1:
                # One hit, attack adjacent squares
                existing_hit = hits[0]
                directions = ["u", "d", "l", "r"]
                while True:
                    selected = random.choice(directions)
                    row, col = existing_hit[0], existing_hit[1]
                    if selected == "u":
                        row -= 1
                    elif selected == "d":
                        row += 1
                    elif selected == "l":
                        col -= 1
                    else:
                        col += 1

                    if 0 <= row <= 7 and 0 <= col <= 7 and self.computer.hits_board.board[row][col] == "-":
                        break

                hit = False
                for ship in self.player.ships:
                    if (row, col) in ship.positions:
                        print("The computer made a hit!")
                        self.computer.place_hit(row, col)
                        hit = True
                        self.computer.add_to_hits(row, col, ship.name)
                        ship.positions.remove((row, col))
                        self.player.board.board[row][col] = "H"
                        

                        if len(ship.positions) == 0:
                            print(ship.name, "has been sank!")
                            self.player.ships.remove(ship)
                            # Remove hits of the sunk ship
                            self.computer.hits = [h for h in self.computer.hits if h[2] != ship.name]
                        self.player.board.print_board()
                        inTurn = False

                if not hit:
                    print("The computer missed!")
                    self.computer.place_miss(row, col)
                    self.player.board.print_board()
                return

            else:
                # Multiple hits, continue in the same direction
                first_hit = hits[0]
                last_hit = hits[-1]

                if last_hit[0] == first_hit[0]:
                    # Horizontal direction
                    if last_hit[1] > first_hit[1]:
                        row, col = last_hit[0], last_hit[1] + 1
                        direction = "r"
                    else:
                        row, col = last_hit[0], last_hit[1] - 1
                        direction = "l"
                else:
                    # Vertical direction
                    if last_hit[0] > first_hit[0]:
                        row, col = last_hit[0] + 1, last_hit[1]
                        direction = "d"
                    else:
                        row, col = last_hit[0] - 1, last_hit[1]
                        direction = "u"

                if not (0 <= row <= 7 and 0 <= col <= 7) or self.computer.hits_board.board[row][col] != "-":
                    # Reverse direction if boundary is reached or spot is already hit
                    if direction == "u":
                        row, col = first_hit[0] + 1, first_hit[1]
                    elif direction == "d":
                        row, col = first_hit[0] - 1, first_hit[1]
                    elif direction == "l":
                        row, col = first_hit[0], first_hit[1] + 1
                    else:
                        row, col = first_hit[0], first_hit[1] - 1

                if 0 <= row <= 7 and 0 <= col <= 7 and self.computer.hits_board.board[row][col] == "-":
                    hit = False
                    for ship in self.player.ships:
                        if (row, col) in ship.positions:
                            print("The computer made a hit!")
                            self.computer.place_hit(row, col)
                            hit = True
                            self.computer.add_to_hits(row, col, ship.name)
                            ship.positions.remove((row, col))
                            self.player.board.board[row][col] = "H"

                            if len(ship.positions) == 0:
                                print(ship.name, "has been sank!")
                                self.player.ships.remove(ship)
                                # Remove hits of the sunk ship
                                self.computer.hits = [h for h in self.computer.hits if h[2] != ship.name]
                            self.player.board.print_board()
                            inTurn = False

                    if not hit:
                        print("The computer missed!")
                        self.computer.place_miss(row, col)
                        self.player.board.print_board()
                    return
            
    def play_game(self):
        #need to handle case for player wins after move
        while len(self.computer.ships) > 0 and len(self.player.ships) > 0:
            self.player_move()
            self.computer_move()
        
        if self.player.ships:
            return print(f"Player wins!")
        else:
            return print(f"Computer wins!")
