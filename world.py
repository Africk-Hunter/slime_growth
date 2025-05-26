import os
from slime_manager import SlimeManager
from tile import Tile
import pygame


class World:

    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.grid = self.init_grid()
        self.SM = SlimeManager(self.grid)
        self.create_initial_slimes()

    def init_grid(self):
        matrix = [[Tile(col, row) for col in range(self.columns)]
                  for row in range(self.rows)]
        return matrix

    def create_initial_slimes(self):
        self.SM.call_initialization()

    def update_all(self, time):
        winner = self.SM.call_update(time)
        self.cls()
        return winner

    def render_grid(self, screen, tile_height, tile_width):
        for row in range(self.rows):
            for col in range(self.columns):
                current_tile = self.grid[row][col]
                self.draw_tile(screen, current_tile, tile_height, tile_width)

    def draw_tile(self, screen, tile, tile_height, tile_width):

        color = (0, 0, 0)
        if tile.has_slime:
            color = tile.slime.color

        pygame.draw.rect(screen, color,
                         (tile.x * tile_width, tile.y * tile_height,
                          tile_width, tile_height))

    def print_grid(self):
        for row in self.grid:
            print(" ".join(tile.print_output() for tile in row))

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')
