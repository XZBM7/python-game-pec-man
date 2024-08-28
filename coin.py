import pygame
#
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((15, 15))  
        self.image.fill((255, 215, 0))  
        self.rect = self.image.get_rect(topleft=(x, y))
