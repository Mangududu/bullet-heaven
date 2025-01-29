# world.py

import pygame
import random

from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, TILE_WIDTH, TILE_HEIGHT,
    WORLD_WIDTH, WORLD_HEIGHT, BLACK
)

class World:
    def __init__(self):
        # Load your grass tile
        self.grass_tile = pygame.image.load("assets/images/backgrounds/Grass_Middle.png").convert_alpha()
        
        # If you have multiple tile variations, you can store them in a list:
        # self.grass_tiles = [
        #     pygame.image.load("assets/images/backgrounds/grass_tile1.png").convert_alpha(),
        #     pygame.image.load("assets/images/backgrounds/grass_tile2.png").convert_alpha()
        # ]
        
        # For demonstration, we'll keep it super simple: just one grass tile.
        
        # Camera position
        self.camera_x = 0
        self.camera_y = 0

    def update(self, dt, player):
        """
        We'll just keep the camera centered on the player for now.
        """
        # Center camera on player's center
        self.camera_x = player.rect.centerx - SCREEN_WIDTH // 2
        self.camera_y = player.rect.centery - SCREEN_HEIGHT // 2
        
        # Optional: clamp camera if you have a finite map
        max_camera_x = WORLD_WIDTH * TILE_WIDTH - SCREEN_WIDTH
        max_camera_y = WORLD_HEIGHT * TILE_HEIGHT - SCREEN_HEIGHT
        # Make sure we don't scroll beyond the world edges:
        if self.camera_x < 0:
            self.camera_x = 0
        if self.camera_y < 0:
            self.camera_y = 0
        if self.camera_x > max_camera_x:
            self.camera_x = max_camera_x
        if self.camera_y > max_camera_y:
            self.camera_y = max_camera_y

    def draw(self, surface):
        """
        Draw only the visible tiles within the camera's viewport.
        """
        # Determine which part of the map is visible
        start_col = self.camera_x // TILE_WIDTH
        end_col = (self.camera_x + SCREEN_WIDTH) // TILE_WIDTH + 1
        start_row = self.camera_y // TILE_HEIGHT
        end_row = (self.camera_y + SCREEN_HEIGHT) // TILE_WIDTH + 1
        
        # Clamp to our world size
        end_col = min(end_col, WORLD_WIDTH)
        end_row = min(end_row, WORLD_HEIGHT)

        for row in range(start_row, end_row):
            for col in range(start_col, end_col):
                # Calculate the tile's world x/y
                world_x = col * TILE_WIDTH
                world_y = row * TILE_HEIGHT
                
                # Convert to screen coordinates using camera offset
                screen_x = world_x - self.camera_x
                screen_y = world_y - self.camera_y
                
                # Blit the grass tile
                surface.blit(self.grass_tile, (screen_x, screen_y))

