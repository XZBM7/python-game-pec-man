import pygame
import random
from settings import WIDTH, HEIGHT, GREEN, BLUE

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, power_type):
        super().__init__()
        self.power_type = power_type
        self.image = pygame.Surface((20, 20))
        if power_type == 'speed':
            self.image.fill(GREEN)
        elif power_type == 'invincibility':
            self.image.fill(BLUE)
        elif power_type == 'freeze':
            self.image.fill((255, 255, 0)) 
        self.rect = self.image.get_rect(topleft=(x, y))

    def apply_power(self, player):
        if self.power_type == 'speed':
            player.speed *= 2
        elif self.power_type == 'invincibility':
            player.invincible = True
        elif self.power_type == 'freeze':
            player.freeze_enemies()
        self.kill()

def create_powerups(num_powerups):
    powerups = pygame.sprite.Group()
    power_types = ['speed', 'invincibility', 'freeze']
    for _ in range(num_powerups):
        x = random.randint(30, WIDTH - 30)
        y = random.randint(30, HEIGHT - 30)
        power_type = random.choice(power_types)
        powerup = PowerUp(x, y, power_type)
        powerups.add(powerup)
    return powerups
