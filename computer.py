import random
from player_base import PlayerBase

class Computer(PlayerBase):
    def __init__(self, size=10):
        super().__init__(size)
        self.hits = []
        
    def return_hits(self):
        return self.hits
    
    def random_arrange(self):
        while self.availableShips:
            selected_ship = random.choice(self.availableShips)
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            horizontal = random.choice([True, False])
            if self.check_move(selected_ship, row, col, horizontal):
                self.place_ship(selected_ship, row, col, horizontal)
                self.availableShips.remove(selected_ship)
                
    
        
