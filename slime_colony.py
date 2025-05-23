from slime import Slime
import random
from settings import GRID_HEIGHT, GRID_WIDTH, COLOR_CODES, RESET_CODE

class SlimeColony():

    def __init__(self, id, world_grid):
        self.id = id
        self.slime_list = []
        self.identifier_raw = random.choice(['x', 'o', '*', '#', '%', '+'])
        color = random.choice(COLOR_CODES)
        self.identifier = f"{color}{self.identifier_raw}{RESET_CODE}" 
        self.world_grid = world_grid
    
    def add_to_list_and_grid(self, new_slime, position):
        x, y = position        
        self.world_grid[y][x].slime_tile(new_slime)
        self.slime_list.append(new_slime)

    def create_initial_slime(self):
        col = random.randint(0, GRID_WIDTH - 1)
        row = random.randint(0, GRID_HEIGHT - 1)

        new_slime = Slime(self.id, self.identifier, (col, row))

        self.add_to_list_and_grid(new_slime, (col, row))
        return

    def create_new_slime(self, position):
        new_slime = Slime(self.id, self.identifier, position)

        self.add_to_list_and_grid(new_slime, position)
        return
    
    def does_tile_have_slime_already(self, position):
        x, y = position
        return self.world_grid[y][x].has_slime

    def is_slime_from_opposing_colony(self, new_position, new_slime):
        current_slime = self.get_slime_at_position(new_position)
        return (current_slime.colony_id != new_slime.colony_id)
    
    def get_slime_at_position(self, position):
        x, y = position
        return self.world_grid[y][x].slime

    def handle_slime_battle(self, attacking_slime, defending_slime):
        power_differential = attacking_slime.power - defending_slime.power 
        if power_differential > 0:
            if random.uniform(0, 1) <= power_differential:
                x, y = defending_slime.position
                self.world_grid[y][x].slime = attacking_slime
                defending_slime.marked_for_deletion = True

    def call_update(self, time):
        current_slimes = self.slime_list.copy()
        for slime in current_slimes:

            if slime.marked_for_deletion == True:
                self.slime_list.remove(slime)
                continue

            new_pos = slime.update(time)
            if not new_pos:
                continue

            if self.does_tile_have_slime_already(new_pos):
                if self.is_slime_from_opposing_colony(new_pos, slime):
                    self.handle_slime_battle(slime, self.get_slime_at_position(new_pos))
                    pass
                continue

            self.create_new_slime(new_pos)



