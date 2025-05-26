import os
from slime_manager import SlimeManager
from tile import Tile
from render_helpers import RenderHelpers


class World:

    def __init__(self, columns, rows, screen):
        self.columns = columns
        self.rows = rows
        self.grid = self.init_grid()
        self.SM = SlimeManager(self.grid)
        self.create_initial_slimes()
        self.RH = RenderHelpers(screen, self.grid, self.rows, self.columns)

    def init_grid(self):
        matrix = [[Tile(col, row) for col in range(self.columns)]
                  for row in range(self.rows)]
        return matrix

    def create_initial_slimes(self):
        self.SM.call_initialization()

    def update_all(self, time):
        winner = self.SM.call_update(time)
        self.cls()
        return winner

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')
