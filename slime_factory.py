import random
from settings import GRID_HEIGHT, GRID_WIDTH
from slime import Slime


class SlimeFactory:

  def __init__(self, world_grid, colony_power, colony_growth, slime_list,
               colony_id, colony_identifier, colony_color):
    self.world_grid = world_grid
    self.colony_power = colony_power
    self.colony_growth = colony_growth
    self.slime_list = slime_list
    self.colony_id = colony_id
    self.colony_identifier = colony_identifier
    self.colony_color = colony_color

  def refresh_slimes(self):
    for slime in self.slime_list:
      slime.power = random.uniform(self.colony_power - 1,
                                   self.colony_power + 1)
      slime.growth_speed = round(
          random.uniform(self.colony_growth - 1, self.colony_growth + 1))

  def increase_power_for_size(self):
    self.colony_power += (GRID_HEIGHT * GRID_WIDTH) * 0.0000001875
    self.refresh_slimes()

  def add_to_list_and_grid(self, new_slime, position):
    x, y = position
    self.world_grid[y][x].slime_tile(new_slime)
    self.slime_list.append(new_slime)
    self.increase_power_for_size()

  def create_initial_slime(self):
    col = random.randint(0, GRID_WIDTH - 1)
    row = random.randint(0, GRID_HEIGHT - 1)

    new_slime = Slime(self.colony_id, self.colony_identifier,
                      self.colony_color, (col, row), self.world_grid,
                      self.colony_growth, self.colony_power)

    self.add_to_list_and_grid(new_slime, (col, row))
    return

  def create_new_slime(self, position):
    new_slime = Slime(self.colony_id, self.colony_identifier,
                      self.colony_color, position, self.world_grid,
                      self.colony_growth, self.colony_power)

    self.add_to_list_and_grid(new_slime, position)
    return
