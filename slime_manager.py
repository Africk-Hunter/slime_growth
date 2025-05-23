import random
from slime_colony import SlimeColony
from settings import MAX_SLIMES

class SlimeManager():

    def __init__(self, world_grid):
        self.slime_colonies = 0
        self.colony_list = []
        self.world_grid = world_grid

    def create_new_colony(self):
        new_colony = SlimeColony(self.slime_colonies, self.world_grid)
        self.slime_colonies += 1
        self.colony_list.append(new_colony)

    def call_initialization(self):
        colony_count = random.randint(2, MAX_SLIMES)

        for colony in range(colony_count):
            self.create_new_colony()

        for colony in self.colony_list:
            colony.create_initial_slime()

    def call_update(self):
        activity = False
        for colony in self.colony_list:
            before = len(colony.slime_list)
            colony.call_update()
            after = len(colony.slime_list)
            if before != after:
                activity = True

        if not activity:
            print("Simulation stalled: No slime expanded.")