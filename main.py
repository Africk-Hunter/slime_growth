import time
import pygame  
from settings import GRID_WIDTH, GRID_HEIGHT
from world import World

def main():
    pygame.init()
    pygame.mixer.quit()

    world = World(GRID_WIDTH, GRID_HEIGHT)

    # Set up the display
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Slimespread")

    running = True
    clock = pygame.time.Clock()
    FPS = 60
    world.print_grid()
    

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
        # Game logic
        
        time.sleep(.5)
        world.update_all()
        

        # Drawing
        """ screen.fill((0, 0, 0))   """
        # Draw your game elements here

        """ pygame.display.flip() """
        clock.tick(FPS)
    pass

if __name__ == "__main__":
    main()