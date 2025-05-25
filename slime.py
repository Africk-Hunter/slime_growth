import random
from settings import GRID_HEIGHT, GRID_WIDTH


class Slime:

    def __init__(self, colony_id, colony_color, slime_position, world_grid,
                 growth_speed, power):
        self.colony_id = colony_id
        self.color = colony_color
        self.position = slime_position
        self.canidates = self.get_adjacent_positions_on_map()
        self.power = random.uniform(power - 1, power + 1)
        self.growth_speed = random.randint(growth_speed - 1, growth_speed + 1)
        self.marked_for_deletion = False
        self.world_grid = world_grid

    def get_adjacent_positions_on_map(self):
        x, y = self.position
        candidates = [
            (x, y - 1),  # north
            (x + 1, y),  # east
            (x, y + 1),  # south
            (x - 1, y),  # west
        ]

        valid_candiates = [(nx, ny) for nx, ny in candidates
                           if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT]

        return valid_candiates

    def does_tile_have_slime_already(self, position):
        x, y = position
        return self.world_grid[y][x].has_slime

    def is_slime_from_opposing_colony(self, new_position):
        current_slime = self.get_slime_at_position(new_position)
        return (current_slime.colony_id != self.colony_id)

    def get_slime_at_position(self, position):
        x, y = position
        return self.world_grid[y][x].slime

    def select_tile_to_grow_to(self):
        random.shuffle(self.canidates)
        new_tile_type = None

        for canidate_tile_pos in self.canidates:
            if not self.does_tile_have_slime_already(canidate_tile_pos):
                new_tile_type = 'empty'
                return canidate_tile_pos, new_tile_type

            if not self.is_slime_from_opposing_colony(canidate_tile_pos):
                continue

            return canidate_tile_pos, 'enemy'

        return None, new_tile_type

    def update(self, time):
        if time % self.growth_speed == 0:
            return self.select_tile_to_grow_to()
        return None, None
