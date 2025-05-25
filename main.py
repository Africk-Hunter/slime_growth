import time
import pygame
from settings import GRID_WIDTH, GRID_HEIGHT
from world import World

pygame.init()
pygame.mixer.quit()


def main():
    world = World(GRID_WIDTH, GRID_HEIGHT)

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Slimespread")

    running = True
    clock = pygame.time.Clock()
    FPS = 60
    current_time = 0

    tile_size = min(screen_width // GRID_WIDTH, screen_height // GRID_HEIGHT)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        time.sleep(0.02)
        winner = world.update_all(current_time)
        current_time += 1

        screen.fill((0, 200, 0))

        world.render_grid(screen, tile_size)

        pygame.display.flip()

        clock.tick(FPS)

        if winner is not None:
            print(f'Colony {winner} wins!')
            running = False

    pygame.quit()


if __name__ == "__main__":
    main()
