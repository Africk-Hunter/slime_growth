import random
from settings import GRID_HEIGHT, GRID_WIDTH

class Slime:

    def __init__(self, colony_id, colony_color, slime_position):
        self.colony_id = colony_id
        self.color = colony_color
        self.position = slime_position
        self.canidates = self.get_adjacent_positions_on_map()
        self.power = random.uniform(1, 10)
        self.growth_speed = random.randint(2, 20)
        self.marked_for_deletion = False

    def get_adjacent_positions_on_map(self):
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
    
    def does_tile_have_slime_already(self, position, world_grid):
        x, y = position
        return world_grid[y][x].has_slime

    def is_slime_from_opposing_colony(self, new_position):
        current_slime = self.get_slime_at_position(new_position)
        return (current_slime.colony_id != self.colony_id)
    
    def get_slime_at_position(self, position, world_grid):
        x, y = position
        return world_grid[y][x].slime
    
    def handle_slime_battle(self, attacking_slime, defending_slime, world_grid):
        power_differential = attacking_slime.power - defending_slime.power 
        if power_differential > 0:
            if random.uniform(0, 1) <= power_differential:
                x, y = defending_slime.position
                world_grid[y][x].slime = attacking_slime
                defending_slime.marked_for_deletion = True

    def select_tile_to_grow_to(self, world_grid):
        random.shuffle(self.canidates)
        new_tile_type = None

        for canidate_tile_pos in self.canidates:
            if not self.does_tile_have_slime_already(canidate_tile_pos, world_grid):
                new_tile_type = 'empty'
                return canidate_tile_pos, new_tile_type
            
            if not self.is_slime_from_opposing_colony(canidate_tile_pos, world_grid):
                continue
        
            return canidate_tile_pos, 'enemy'
        
        return None, new_tile_type
        """ return random.choice(self.canidates) if self.canidates else None """

    def update(self, time, world_grid):
        if time % self.growth_speed == 0:
            return self.select_tile_to_grow_to(world_grid)
        return None, None

        