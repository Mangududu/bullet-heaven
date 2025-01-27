import pygame

class HealthPickup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/items/health.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.heal_amount = 20

    def update(self, dt):
        # If the player collides with it, increase health, then destroy
        pass
