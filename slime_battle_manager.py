import random


## Add types to slimes that have effectivness
class SlimeBattleManager:

    def __init__(self, world_grid):
        self.world_grid = world_grid

    def handle_slime_battle(self, attacking_slime, defending_slime):
        power_differential = attacking_slime.power - defending_slime.power
        if power_differential > 0:
            if random.uniform(0, 1) <= power_differential:
                self.replace_slime_after_battle(attacking_slime,
                                                defending_slime)

    def replace_slime_after_battle(self, attacking_slime, defending_slime):
        x, y = defending_slime.position
        defending_tile = self.world_grid[y][x]
        defending_slime.marked_for_deletion = True
        defending_tile.slime_tile(attacking_slime)
