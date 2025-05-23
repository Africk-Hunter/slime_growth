import random
from settings import GRID_HEIGHT, GRID_WIDTH

class Slime:

    def __init__(self, colony_id, colony_color, slime_position):
        self.colony_id = colony_id
        self.color = colony_color
        self.position = slime_position
        self.canidates = self.get_adjacent_positions()
        self.landlocked = False
        self.power = random.uniform(1, 10)
        self.growth_speed = random.uniform(1, 10)
        self.marked_for_deletion = False
        ## Power, growth speed

    def get_adjacent_positions(self):
        x, y = self.position
        candidates = [
            (x, y - 1),  # north
            (x + 1, y),  # east
            (x, y + 1),  # south
            (x - 1, y),  # west
        ]

        valid_candiates = [
            (nx, ny) for nx, ny in candidates
            if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT
        ]

        return valid_candiates

    def get_random_adjacent_tile(self):
        return random.choice(self.canidates) if self.canidates else None

    def spread_to_adjacent_tile(self):
        return self.get_random_adjacent_tile()

    def update(self):
        self.spread_to_adjacent_tile()