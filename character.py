import pygame
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load images or animations
        self.image = pygame.image.load("assets/images/player/player_idle_1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        
        # Player stats
        self.speed = PLAYER_SPEED
        self.health = MAX_HEALTH
        # You could store all animation frames in a dict or list.

    def update(self, dt):
        # Handle movement or any logic
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= int(self.speed)
        if keys[pygame.K_s]:
            self.rect.y += int(self.speed)
        if keys[pygame.K_a]:
            self.rect.x -= int(self.speed)
        if keys[pygame.K_d]:
            self.rect.x += int(self.speed)
        
        # If using an automatic weapon, you might trigger projectile creation here
        # or in a separate weapon class.

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            # Trigger death, game over, or respawn logic
            pass
