import pygame

def draw_text(surface, text, x, y, font, color=(255,255,255)):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))
