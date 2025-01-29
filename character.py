# character.py

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Adjust these numbers based on how your sprite sheet is arranged:
        self.frame_width = 32
        self.frame_height = 32
        self.num_frames = 4  # Suppose we have 4 frames horizontally in the sheet

        # Load the player sprite sheet (e.g., 4 frames in a row).
        try:
            self.sprite_sheet = pygame.image.load("assets/images/player/player.png").convert_alpha()
        except pygame.error as e:
            print(f"Unable to load sprite sheet image: {e}")
            self.sprite_sheet = pygame.Surface((self.frame_width, self.frame_height))  # Create a blank surface as a placeholder
        self.frame_width = 32
        self.frame_height = 32
        self.num_frames = 4  # Suppose we have 4 frames horizontally in the sheet
        
        # Extract frames from the sprite sheet
        self.frames = []
        for i in range(self.num_frames):
            x = i * self.frame_width
            y = 0  # single row
            frame_surf = self.sprite_sheet.subsurface(
                pygame.Rect(x, y, self.frame_width, self.frame_height)
            )
            self.frames.append(frame_surf)
        
        # Animation timing
        self.current_frame = 0
        self.last_update_time = 0
        self.frame_rate = 200  # ms per frame (change to taste)
        
        # Start with the first frame
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        
        # Movement speed (pixels per second)
        self.speed = 200.0

    def update(self, dt):
        """
        dt is the time elapsed in seconds since last frame.
        """
        # Handle movement input
        keys = pygame.key.get_pressed()
        dx = 0
        dy = 0
        
        if keys[pygame.K_w]:
            dy = -1
        if keys[pygame.K_s]:
            dy = 1
        if keys[pygame.K_a]:
            dx = -1
        if keys[pygame.K_d]:
            dx = 1
        
        # Normalize diagonal movement
        if dx != 0 and dy != 0:
            # So that diagonal speed is not faster
            dx *= 0.7071
            dy *= 0.7071
        
        # Update position
        self.rect.x += dx * self.speed * dt
        self.rect.y += dy * self.speed * dt
        
        # Update animation only if moving
        if dx != 0 or dy != 0:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update_time > self.frame_rate:
                self.last_update_time = current_time
                self.current_frame = (self.current_frame + 1) % len(self.frames)
                self.image = self.frames[self.current_frame]

    def draw(self, surface):
        # Just blit the current frame at self.rect
        surface.blit(self.image, self.rect)

