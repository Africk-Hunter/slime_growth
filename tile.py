from slime import Slime

class Tile:

    def __init__(self, x_location, y_location):
        self.x = x_location
        self.y = y_location
        self.has_slime = False
        self.slime = None

    def slime_tile(self, slime):
        self.has_slime = True
        self.slime = slime

    def print_output(self):
        return f'[{self.slime.color}]' if self.has_slime else '[ ]'
