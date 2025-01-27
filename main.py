import pygame
from constants import *
from character import Player
from enemy import Enemy
from world import World

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    
    # Create player, enemies, world, etc.
    player = Player()
    world = World()

    while running:
        dt = clock.tick(FPS) / 1000.0  # Delta time in seconds
        
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
        player.draw(screen)
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
