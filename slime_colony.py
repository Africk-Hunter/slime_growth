from slime import Slime
import random
from settings import GRID_HEIGHT, GRID_WIDTH

class SlimeColony():

    def __init__(self, id, world_grid):
        self.id = id
        self.slime_list = []
        self.identifier = random.choice(['x', 'o', '*', '#', '%', '+'])
        self.world_grid = world_grid
    
    def create_initial_slime(self):
        col = random.randint(0, GRID_WIDTH - 1)
        row = random.randint(0, GRID_HEIGHT - 1)

        new_slime = Slime(self.id, self.identifier, (col, row))
        self.world_grid[row][col].slime_tile(new_slime)
        self.slime_list.append(new_slime)

    def create_new_slime(self, position):
        x, y = position
        new_slime = Slime(self.id, self.identifier, position)
        self.world_grid[y][x].slime_tile(new_slime)
        self.slime_list.append(new_slime)
        return new_slime

    def call_update(self):
        current_slimes = self.slime_list.copy()
        for slime in current_slimes:
            new_pos = slime.spread_to_adjacent_tile()
            if new_pos:
                x, y = new_pos
                if not self.world_grid[y][x].has_slime:
                    new_slime = Slime(self.id, self.identifier, new_pos)
                    self.slime_list.append(new_slime)
                    self.world_grid[y][x].slime_tile(new_slime)


