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
        self.power += (GRID_HEIGHT * GRID_WIDTH) * 0.0000001875

        self.refresh_slimes()

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

    def refresh_slimes(self):
        for slime in self.slime_list:
            slime.power = random.uniform(self.power - 1, self.power + 1)
            slime.growth_speed = round(
                random.uniform(self.growth_speed - 1, self.growth_speed + 1))

    def handle_fruit_collection(self, position):
        x, y = position
        fruit = self.world_grid[y][x].fruit
        if fruit.type == 'power':
            print('power from:', self.power, 'to', self.power * fruit.modifier)
            self.power *= fruit.modifier
        else:
            print('growth from:', self.growth_speed, 'to',
                  self.growth_speed / fruit.modifier)
            self.growth_speed /= fruit.modifier
        self.refresh_slimes()
        self.world_grid[y][x].has_fruit = False

    def call_update(self, time):
        current_slimes = self.slime_list.copy()
        for slime in current_slimes:

            if slime.marked_for_deletion:
                self.slime_list.remove(slime)
                continue

            new_pos, new_tile_type = slime.update(time)
            if not new_pos:
                continue

            match new_tile_type:
                case 'fruit':
                    self.handle_fruit_collection(new_pos)
                case 'empty':
                    self.create_new_slime(new_pos)
                case 'enemy':
                    defending_slime = self.get_slime_at_position(new_pos)
                    self.battler.handle_slime_battle(slime, defending_slime)

                    if defending_slime.marked_for_deletion:
                        self.create_new_slime(new_pos)
