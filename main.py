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
        world = World(GRID_WIDTH, GRID_HEIGHT, screen)
        clock = pygame.time.Clock()
        playing = True
        winner = None
        current_time = 0

        while playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN
                                                 and event.key
                                                 == pygame.K_ESCAPE):
                    running = False
                    playing = False

            time.sleep(0.02)
            winner = world.update_all(current_time)
            current_time += 1

            screen.fill((0, 0, 0))
            world.RH.render_grid()
            pygame.display.flip()
            clock.tick(FPS)

            if winner is not None:
                playing = False

        if winner is not None and running:
            waiting_for_input = True
            while waiting_for_input:
                screen.fill((0, 0, 0))
                world.RH.render_grid()
                world.RH.render_win_screen(winner)
                button_rect = world.RH.render_play_again_button()
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        waiting_for_input = False
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        running = False
                        waiting_for_input = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if button_rect.collidepoint(event.pos):
                            waiting_for_input = False  # Restart the game

    pygame.quit()


if __name__ == "__main__":
    main()
