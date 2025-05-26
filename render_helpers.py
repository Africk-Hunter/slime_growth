import pygame
from settings import GRID_HEIGHT, GRID_WIDTH


class RenderHelpers:

  def __init__(self, screen, grid, rows, columns):
    self.screen = screen
    screen_width, screen_height = screen.get_window_size()
    self.tile_width = screen_width / GRID_WIDTH
    self.tile_height = screen_height / GRID_HEIGHT
    self.grid = grid
    self.rows = rows
    self.columns = columns

  def render_grid(self):
    for row in range(self.rows):
      for col in range(self.columns):
        current_tile = self.grid[row][col]
        self.draw_tile(current_tile)

  def draw_tile(self, tile):
    color = (0, 0, 0)
    if tile.has_slime:
      color = tile.slime.color

    pygame.draw.rect(self.screen, color,
                     (tile.x * self.tile_width, tile.y * self.tile_height,
                      self.tile_width, self.tile_height))

    def print_grid(self):
      for row in self.grid:
        print(" ".join(tile.print_output() for tile in row))
