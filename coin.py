import pygame
import random
from settings import WIDTH, HEIGHT

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((15, 15))  
        self.image.fill((255, 215, 0)) 
        self.rect = self.image.get_rect(topleft=(x, y))

def create_coins(num_coins):
    coins = pygame.sprite.Group()
    for _ in range(num_coins):
        x = random.randint(30, WIDTH - 30)
        y = random.randint(30, HEIGHT - 30)
        coin = Coin(x, y)
        coins.add(coin)
    return coins
