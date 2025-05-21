class Tile:

    def __init__(self):
        self.has_slime = False

    def slime_tile(self):
        self.has_slime = True

    def print_output(self):
        return '[x]' if self.has_slime else '[ ]'