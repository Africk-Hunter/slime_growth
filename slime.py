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
        self.growth_speed = random.randint(2, 20)
        self.marked_for_deletion = False

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

    def update(self, time):
        if time % self.growth_speed == 0:
            return self.get_random_adjacent_tile()

        