import pygame
from constants import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/enemies/enemy_type1_1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.speed = ENEMY_SPEED
        self.health = 20
        
    def update(self, dt, player):
        """
        Example AI: Move toward the player at a constant speed.
        """
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        
        # Normalize direction (simple approach)
        length = max((dx**2 + dy**2)**0.5, 1)
        dx /= length
        dy /= length
        
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        
        # Check collision with player, deal damage, etc.

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            # Mark for removal or kill sprite
            self.kill()
