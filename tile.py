from slime import Slime


class Tile:

    def __init__(self, x_location, y_location):
        self.x = x_location
        self.y = y_location
        self.has_slime = False
        self.slime = None
        self.has_fruit = False
        self.fruit = None

    def slime_tile(self, slime):
        self.has_slime = True
        self.slime = slime

    def add_fruit(self, fruit):
        self.has_fruit = True
        self.fruit = fruit

    def fruit_eaten(self, colony_id):
        pass

    def print_output(self):
        return f'[{self.slime.identifier}]' if self.has_slime else '[ ]'
