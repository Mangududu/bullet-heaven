# main.py

import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLACK
from character import Player
from world import World

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Bullet Heaven Example")
    
    clock = pygame.time.Clock()
    running = True

    # Create player, world, etc.
    player = Player()
    world = World()

    while running:
        dt = clock.tick(FPS) / 1000.0  # delta time in seconds
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update game objects
        player.update(dt)
        world.update(dt, player)
        
        # Render
        screen.fill(BLACK)
        world.draw(screen)
        player.draw(screen)  # or if you have a sprite group, group.draw(screen)
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()

