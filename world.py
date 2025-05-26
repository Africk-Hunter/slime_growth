import os
import random
from slime_manager import SlimeManager
from tile import Tile
from render_helpers import RenderHelpers
from fruit import Fruit


class World:

    def __init__(self, columns, rows, screen):
        self.columns = columns
        self.rows = rows
        self.grid = self.init_grid()
        self.SM = SlimeManager(self.grid)
        self.create_initial_slimes()
        self.RH = RenderHelpers(screen, self.grid, self.rows, self.columns)
        self.populate_world()

    def init_grid(self):
        matrix = [[Tile(col, row) for col in range(self.columns)]
                  for row in range(self.rows)]
        return matrix

    def populate_world(self):

        fruit_amount = random.randint(1, 5)

        for fruit in range(fruit_amount):
            x_rand = random.randint(1, self.rows)
            y_rand = random.randint(1, self.columns)

            self.grid[x_rand][y_rand].add_fruit(Fruit())

    def create_initial_slimes(self):
        self.SM.call_initialization()

    def update_all(self, time):
        winner = self.SM.call_update(time)
        """self.cls()"""
        return winner

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')
