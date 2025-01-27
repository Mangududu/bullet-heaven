import pygame
from projectile import Projectile

class Weapon:
    def __init__(self, cooldown=500):
        """
        cooldown in ms: how long between shots.
        """
        self.cooldown = cooldown
        self.last_shot_time = 0
    
    def shoot(self, current_time, x, y, direction):
        """
        If enough time has passed since the last shot, return a new Projectile.
        Otherwise, return None.
        """
        if current_time - self.last_shot_time >= self.cooldown:
            self.last_shot_time = current_time
            return Projectile(x, y, direction)
        return None
