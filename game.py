import random
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
        self.player.hits_board.print_board()
        print("real comp")
        self.computer.board.print_board()
        print("comp hits")
        self.computer.hits_board.print_board()

    def player_move(self):
        print("com len: ", len(self.computer.ships))
        print("comp ship: ")
        for ship in self.computer.ships:
            print(f"{ship.name}: {ship.positions}")
        coord = input(f"Where would you like to attack? (format: row,col)").strip()
        row, col = map(int, coord.split(","))
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
                break

        if not hit:
            print("Miss!")
            self.player.place_miss(row, col)

        return
            
        

    def computer_move(self):
        # check if any computer hits
        #if computer hits and len > 1, check pattern
        # if pattern, continue placing there
        #if == 1, randome move u, d, l, r
        #hit and add to hits
        #if ship sank, clear hits
        #no hits? just random move where spot equals '-'
        hits_len = len(self.computer.return_hits())
        inTurn = True
        while inTurn:
            if hits_len == 0:
                row = random.randint(0, 9)
                col = random.randint(0, 9)
                if self.computer.hits_board.board[row][col] == "-":
                    hit = False
                    for ship in self.player.ships:
                        if (row, col) in ship.positions:
                            print("It's a hit!")
                            self.computer.place_hit(row, col)
                            hit = True
                            ship.positions.remove((row, col))
                            if len(ship.positions) == 0:
                                print(ship.name, "has been sank!")
                                self.player.ships.remove(ship)
                            inTurn = False

                    if not hit:
                        print("Miss!")
                        self.computer.place_miss(row, col)                    
                return
            # elif hits_len == 1:
            #     directions = ["u", "d", "l", "r"]
            #     which_direction = random.randint(0, 3)
            #     selected = directions[which_direction]
            #     if selected == "u":
                    
            #     elif selected == "d":
            #     elif selected == "l":
            #     else:
            #     return
            # else:
                return
            
    def play_game(self):
        #need to handle case for player wins after move
        while len(self.computer.ships) > 0 and len(self.player.ships) > 0:
            self.player_move()
            self.computer_move()
            self.print_boards()
        
        if self.player.ships:
            return print(f"Player wins!")
        else:
            return print(f"Computer wins!")
