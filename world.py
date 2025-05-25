import random, os
from slime_manager import SlimeManager
from tile import Tile


class World:

    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.grid = self.init_grid()
        self.SM = SlimeManager(self.grid)
        self.create_initial_slimes()

    def init_grid(self):
        matrix = [[Tile(col, row) for col in range(self.columns)]
                  for row in range(self.rows)]
        return matrix

    def create_initial_slimes(self):
        self.SM.call_initialization()

    def update_all(self, time):
        winner = self.SM.call_update(time)
        self.cls()
        self.print_grid()
        return winner

    def print_grid(self):
        for row in self.grid:
            print(" ".join(tile.print_output() for tile in row))

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')
