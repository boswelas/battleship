class Ship:    
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = []

    def return_name(self):
        return self.name
        
    def return_size(self):
        return self.size
