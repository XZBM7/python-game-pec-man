import pygame
import math
#
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed=1):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0)) 
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed

    def update(self, target_position):
        self._chase(target_position)

    def _chase(self, target_position):
        dx = target_position[0] - self.rect.x
        dy = target_position[1] - self.rect.y
        distance = (dx**2 + dy**2) ** 0.5
        if distance > 0:
            dx /= distance
            dy /= distance
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed
