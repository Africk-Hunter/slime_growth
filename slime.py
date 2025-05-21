import random
from settings import GRID_HEIGHT, GRID_WIDTH

class Slime:

    def __init__(self, colony_id, colony_color, slime_position):
        self.colony_id = colony_id
        self.color = colony_color
        self.position = slime_position

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

        return random.choice(valid_candiates) if valid_candiates else None

    def spread_to_adjacent_tile(self):
        new_position = self.get_adjacent_positions()
        return new_position

    def update(self):
        self.spread_to_adjacent_tile()