import time
import pygame
from settings import GRID_WIDTH, GRID_HEIGHT
from world import World

pygame.init()
pygame.mixer.quit()


def main():

    screen_width = 500
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Slimespread")

    running = True
    playing = True
    winner = None
    clock = pygame.time.Clock()
    FPS = 60
    current_time = 0

    world = World(GRID_WIDTH, GRID_HEIGHT, screen)

    while running:
        while playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            time.sleep(0.02)
            winner = world.update_all(current_time)
            current_time += 1

            screen.fill((0, 0, 0))

            world.RH.render_grid()

            clock.tick(FPS)

            if winner is not None:
                playing = False

            pygame.display.flip()

        world.RH.render_win_screen(winner)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
