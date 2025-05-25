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
        self.growth_speed = random.randint(20, 50)
        self.power = random.randint(1, 10)
        self.world_grid = world_grid

    def increase_power_for_size(self):
        self.power += .0005

    def add_to_list_and_grid(self, new_slime, position):
        x, y = position
        self.world_grid[y][x].slime_tile(new_slime)
        self.slime_list.append(new_slime)
        self.increase_power_for_size()

    def create_initial_slime(self):
        col = random.randint(0, GRID_WIDTH - 1)
        row = random.randint(0, GRID_HEIGHT - 1)

        new_slime = Slime(self.id, self.identifier, (col, row),
                          self.world_grid, self.growth_speed, self.power)

        self.add_to_list_and_grid(new_slime, (col, row))
        return

    def create_new_slime(self, position):
        new_slime = Slime(self.id, self.identifier, position, self.world_grid,
                          self.growth_speed, self.power)

        self.add_to_list_and_grid(new_slime, position)
        return

    def get_slime_at_position(self, position):
        x, y = position
        return self.world_grid[y][x].slime

    def replace_slime_after_battle(self, attacking_slime, defending_slime):
        x, y = defending_slime.position
        defending_tile = self.world_grid[y][x]

        self.add_to_list_and_grid(attacking_slime, (x, y))
        defending_slime.marked_for_deletion = True

    def handle_slime_battle(self, attacking_slime, defending_slime):
        power_differential = attacking_slime.power - defending_slime.power
        if power_differential > 0:
            if random.uniform(0, 1) <= power_differential:
                self.replace_slime_after_battle(attacking_slime,
                                                defending_slime)

    def call_update(self, time):
        current_slimes = self.slime_list.copy()
        for slime in current_slimes:

            if slime.marked_for_deletion:
                self.slime_list.remove(slime)
                continue

            new_pos, new_tile_type = slime.update(time)
            if not new_pos:
                continue

            if new_tile_type == 'empty':
                self.create_new_slime(new_pos)

            elif new_tile_type == 'enemy':
                defending_slime = self.get_slime_at_position(new_pos)
                self.handle_slime_battle(slime, defending_slime)

                if defending_slime.marked_for_deletion:
                    self.create_new_slime(new_pos)
