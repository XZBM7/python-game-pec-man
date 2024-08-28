#sooooooooon#
import pygame
from settings import BLUE

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

        for row_idx, row in enumerate(layout):
            for col_idx, cell in enumerate(row):
                if cell == "1":
                    wall = pygame.Rect(col_idx * 30, row_idx * 30, 30, 30)
                    self.walls.append(wall)

        self.add_boundaries()

    def add_boundaries(self):
        if not self.walls:
            return
        
        width = len(self.walls[0]) // 30
        height = len(self.walls) // 30
        border_thickness = 30

        top_border = pygame.Rect(0, 0, width * 30, border_thickness)
        bottom_border = pygame.Rect(0, height * 30, width * 30, border_thickness)
        
        left_border = pygame.Rect(0, 0, border_thickness, height * 30)
        right_border = pygame.Rect(width * 30, 0, border_thickness, height * 30)
        
        self.walls.extend([top_border, bottom_border, left_border, right_border])

    def draw(self, screen):
        for wall in self.walls:
            pygame.draw.rect(screen, BLUE, wall)
