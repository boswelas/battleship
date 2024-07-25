import random
from player_base import PlayerBase

class Computer(PlayerBase):
    def __init__(self, size=8):
        super().__init__(size)
        self.hits = []

    def return_hits(self):
        return self.hits

    def add_to_hits(self, row, col, ship_id):
        self.hits.append((row, col, ship_id))

    def random_arrange(self):
        while self.availableShips:
            selected_ship = random.choice(self.availableShips)
            row = random.randint(0, 7)
            col = random.randint(0, 7)
            horizontal = random.choice([True, False])
            if self.check_move(selected_ship, row, col, horizontal):
                self.place_ship(selected_ship, row, col, horizontal)
                self.availableShips.remove(selected_ship)
