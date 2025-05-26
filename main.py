import time
import pygame
from settings import GRID_WIDTH, GRID_HEIGHT
from world import World

pygame.init()
pygame.mixer.quit()
font = pygame.font.Font(None, 36)


def main():
    world = World(GRID_WIDTH, GRID_HEIGHT)

    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Slimespread")

    running = True
    clock = pygame.time.Clock()
    FPS = 60
    current_time = 0

    tile_width = screen_width / GRID_WIDTH
    tile_height = screen_height / GRID_HEIGHT

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        time.sleep(0.02)
        winner = world.update_all(current_time)
        current_time += 1

        screen.fill((0, 0, 0))

        world.render_grid(screen, tile_width, tile_height)

        clock.tick(FPS)

        if winner is not None:
            winner_text = font.render(f'Colony {winner} wins!', True,
                                      (255, 255, 255))
            text_rect = winner_text.get_rect(center=(screen_width / 2,
                                                     screen_height / 2))
            screen.blit(winner_text, text_rect)

            running = False
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
