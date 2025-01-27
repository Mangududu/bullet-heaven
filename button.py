import pygame

class Button:
    def __init__(self, x, y, image_normal, image_hover):
        self.image_normal = pygame.image.load(image_normal).convert_alpha()
        self.image_hover = pygame.image.load(image_hover).convert_alpha()
        self.rect = self.image_normal.get_rect(topleft=(x, y))
        self.is_hovered = False

    def update(self):
        pos = pygame.mouse.get_pos()
        self.is_hovered = self.rect.collidepoint(pos)

    def draw(self, surface):
        if self.is_hovered:
            surface.blit(self.image_hover, self.rect)
        else:
            surface.blit(self.image_normal, self.rect)

    def is_clicked(self):
        return self.is_hovered and pygame.mouse.get_pressed()[0]
