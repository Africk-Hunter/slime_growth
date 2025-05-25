from slime import Slime
import random
from settings import GRID_HEIGHT, GRID_WIDTH, COLOR_CODES, RESET_CODE
from slime_battle_manager import SlimeBattleManager


class SlimeColony():

    def __init__(self, id, world_grid):
        self.id = id
        self.slime_list = []
        self.identifier_raw = random.choice(['x', 'o', '*', '#', '%', '+'])
        self.color = self.create_random_color()
        self.identifier = f"{self.identifier_raw}{RESET_CODE}"
        self.growth_speed = random.randint(20, 50)
        self.power = random.randint(1, 10)
        self.world_grid = world_grid
        self.battler = SlimeBattleManager(self.world_grid)

    def increase_power_for_size(self):
        self.power += .0003

    def add_to_list_and_grid(self, new_slime, position):
        x, y = position
        self.world_grid[y][x].slime_tile(new_slime)
        self.slime_list.append(new_slime)
        self.increase_power_for_size()

    def create_initial_slime(self):
        col = random.randint(0, GRID_WIDTH - 1)
        row = random.randint(0, GRID_HEIGHT - 1)

        new_slime = Slime(self.id, self.identifier, self.color, (col, row),
                          self.world_grid, self.growth_speed, self.power)

        self.add_to_list_and_grid(new_slime, (col, row))
        return

    def create_random_color(self):
        return (random.randint(0, 255), random.randint(0, 255),
                random.randint(0, 255))

    def create_new_slime(self, position):
        new_slime = Slime(self.id, self.identifier, self.color, position,
                          self.world_grid, self.growth_speed, self.power)

        self.add_to_list_and_grid(new_slime, position)
        return

    def get_slime_at_position(self, position):
        x, y = position
        return self.world_grid[y][x].slime

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
                self.battler.handle_slime_battle(slime, defending_slime)

                if defending_slime.marked_for_deletion:
                    self.create_new_slime(new_pos)
