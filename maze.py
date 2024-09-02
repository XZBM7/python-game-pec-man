
import pygame
from settings import BLUE_1, WIDTH, HEIGHT

class Maze:
    def __init__(self):
        self.walls = []
        self.create_maze()

    def create_maze(self):
        layout = [
            "1111111111111111111",
            "1000000000000000001",
            "1011111111111011101",
            "1001000000010010001",
            "1011101111011111101",
            "1000100000001000001",
            "1111111111111111111"
        ]

        cell_width = WIDTH // len(layout[0])  
        cell_height = HEIGHT // len(layout)  

        for row_idx, row in enumerate(layout):
            for col_idx, cell in enumerate(row):
                if cell == "1":
                    wall = pygame.Rect(col_idx * cell_width, row_idx * cell_height, cell_width, cell_height)
                    self.walls.append(wall)

    def draw(self, screen):
        for wall in self.walls:
            pygame.draw.rect(screen, BLUE_1, wall)

