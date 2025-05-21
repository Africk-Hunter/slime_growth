import random, os

from tile import Tile

class World:

    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.grid = self.init_grid()

    def init_grid(self):
        matrix = [[Tile() for _ in range(self.columns)] for _ in range(self.rows)]
        return matrix
        
    def print_grid(self):
        for row in self.grid:
            print(" ".join(tile.print_output() for tile in row))
            
    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def slime_random_tile(self):
        col = random.randint(0, self.columns - 1)
        row = random.randint(0, self.rows - 1)

        self.cls()
        self.grid[row][col].slime_tile()
        self.print_grid()