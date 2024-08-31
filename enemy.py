import math
import pygame
from settings import WIDTH, HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed=1, color=(255, 0, 0)):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(color)  
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed

    def update(self, target_position, all_enemies):
        self._chase(target_position, all_enemies)

    def _chase(self, target_position, all_enemies):
        dx = target_position[0] - self.rect.x
        dy = target_position[1] - self.rect.y
        distance_to_player = math.hypot(dx, dy)
        
        if distance_to_player > 0:
            dx /= distance_to_player
            dy /= distance_to_player

        separation_force_x = 0
        separation_force_y = 0

        for enemy in all_enemies:
            if enemy != self:
                distance_to_enemy = math.hypot(self.rect.x - enemy.rect.x, self.rect.y - enemy.rect.y)
                if distance_to_enemy < 50:  
                    separation_force_x += (self.rect.x - enemy.rect.x) / distance_to_enemy
                    separation_force_y += (self.rect.y - enemy.rect.y) / distance_to_enemy

        velocity_x = dx + separation_force_x
        velocity_y = dy + separation_force_y

        length = math.hypot(velocity_x, velocity_y)
        if length > 0:
            velocity_x = (velocity_x / length) * self.speed
            velocity_y = (velocity_y / length) * self.speed

        self.rect.x += velocity_x
        self.rect.y += velocity_y

def spawn_enemies(round_number, all_sprites, enemies, enemy_speed, color):
    corners = [(0, 0), (WIDTH - 20, 0), (0, HEIGHT - 20), (WIDTH - 20, HEIGHT - 20)]
    num_enemies = round_number
    for i in range(num_enemies):
        x, y = corners[i % 4]
        enemy = Enemy(x, y, speed=enemy_speed, color=color)
        enemies.add(enemy)
        all_sprites.add(enemy)
