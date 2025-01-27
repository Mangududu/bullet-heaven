import pygame
from constants import *
from enemy import Enemy

class World:
    def __init__(self):
        self.current_stage = 1
        self.enemies = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        
        # Track wave info
        self.wave_number = 1
        self.wave_timer = 0
        self.wave_cooldown = 3000  # 3 seconds between waves

        # Load backgrounds
        self.background_stage1 = pygame.image.load("assets/images/backgrounds/stage1.png").convert()

    def update(self, dt, player):
        # Spawn waves if needed
        self.wave_timer += dt * 1000
        if self.wave_timer >= self.wave_cooldown:
            self.wave_timer = 0
            self.spawn_wave(self.wave_number)
            self.wave_number += 1
        
        # Update enemies
        for enemy in self.enemies:
            enemy.update(dt, player)
        
        # Update projectiles
        for projectile in self.projectiles:
            projectile.update(dt, self.enemies)
        
        # Check if stage should change (e.g., if wave_number passes a certain threshold)
        # ...
    
    def draw(self, surface):
        # Draw background
        surface.blit(self.background_stage1, (0, 0))
        
        # Draw enemies
        for enemy in self.enemies:
            enemy.draw(surface)
        
        # Draw projectiles
        for projectile in self.projectiles:
            projectile.draw(surface)

    def spawn_wave(self, wave_number):
        # Example: spawn 5 enemies at random positions
        import random
        for i in range(5 + wave_number):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            self.enemies.add(Enemy(x, y))
        
    def add_projectile(self, projectile):
        self.projectiles.add(projectile)
