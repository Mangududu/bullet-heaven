import pygame
from constants import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed=8, damage=5):
        super().__init__()
        self.image = pygame.image.load("assets/images/projectiles/bullet.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        
        self.direction = direction  # (dx, dy) or just a float angle
        self.speed = speed
        self.damage = damage

    def update(self, dt, enemies):
        # Move the projectile
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed
        
        # Check if it hits an enemy
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                enemy.take_damage(self.damage)
                # Destroy projectile after hitting
                self.kill()
                break
        
        # If off-screen, kill it
        if (self.rect.x < 0 or self.rect.x > SCREEN_WIDTH or
            self.rect.y < 0 or self.rect.y > SCREEN_HEIGHT):
            self.kill()
