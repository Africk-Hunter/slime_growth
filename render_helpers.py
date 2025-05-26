import pygame
from settings import GRID_HEIGHT, GRID_WIDTH


class RenderHelpers:

  def __init__(self, screen, grid, rows, columns):
    self.screen = screen
    self.screen_width, self.screen_height = screen.get_size()
    self.tile_width = self.screen_width / GRID_WIDTH
    self.tile_height = self.screen_height / GRID_HEIGHT
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

    # Convert to integers to avoid gaps between tiles
    x = int(tile.x * self.tile_width)
    y = int(tile.y * self.tile_height)
    width = int((tile.x + 1) * self.tile_width) - x
    height = int((tile.y + 1) * self.tile_height) - y

    pygame.draw.rect(self.screen, color, (x, y, width, height))

    def print_grid(self):
      for row in self.grid:
        print(" ".join(tile.print_output() for tile in row))

  def render_win_screen(self, winner):
    font = pygame.font.Font('freesansbold.ttf', 36)

    text = font.render(f'Colony {winner} wins!', True, (255, 255, 255))

    text_rect = text.get_rect()

    text_rect.center = self.screen_width / 2, self.screen_height / 2

    self.screen.blit(text, text_rect)
