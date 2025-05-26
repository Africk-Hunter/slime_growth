import random
from settings import RESET_CODE
from slime_battle_manager import SlimeBattleManager
from slime_factory import SlimeFactory


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
        self.factory = SlimeFactory(self.world_grid, self.power,
                                    self.growth_speed, self.slime_list,
                                    self.id, self.identifier, self.color)

    def create_random_color(self):
        return (random.randint(15, 250), random.randint(15, 250),
                random.randint(15, 250))

    def get_slime_at_position(self, position):
        x, y = position
        return self.world_grid[y][x].slime

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
        self.factory.refresh_slimes()
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
                    self.factory.create_new_slime(new_pos)
                case 'enemy':
                    defending_slime = self.get_slime_at_position(new_pos)
                    self.battler.handle_slime_battle(slime, defending_slime)

                    if defending_slime.marked_for_deletion:
                        self.factory.create_new_slime(new_pos)
