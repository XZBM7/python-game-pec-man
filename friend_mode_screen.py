import pygame
from settings import RED, WIDTH, HEIGHT, BLACK, WHITE, GREEN, Hot_Pink, COLORS

class FriendModeScreen:
    def __init__(self, screen, font, button_font, selected_colors):
        self.screen = screen
        self.font = font
        self.button_font = button_font
        self.selected_colors = selected_colors
        self.buttons = {}

    def draw_friend_mode(self):
        self.screen.fill(BLACK)

        friend_title = self.font.render("Play Against Friend", True, WHITE)
        friend_title_rect = friend_title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 120))
        self.screen.blit(friend_title, friend_title_rect)

        self._draw_color_options('player', WIDTH // 2 - 90, HEIGHT // 2 - 20)
        self._draw_color_options('enemy', WIDTH // 2 - 90, HEIGHT // 2 + 60)

        start_game_text = self.button_font.render("Start Game", True, GREEN)
        start_game_rect = start_game_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 120))
        pygame.draw.rect(self.screen, WHITE, start_game_rect.inflate(6, 3))
        self.screen.blit(start_game_text, start_game_rect)
        self.buttons['start_game'] = start_game_rect

        back_button_text = self.button_font.render("Back", True, RED)
        back_button_rect = back_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 160))
        pygame.draw.rect(self.screen, WHITE, back_button_rect.inflate(6, 3))
        self.screen.blit(back_button_text, back_button_rect)
        self.buttons['back'] = back_button_rect

    def _draw_color_options(self, player_or_enemy, start_x, start_y):
        color_text = self.font.render(f"{player_or_enemy.capitalize()} Color:", True, WHITE)
        color_rect = color_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
        self.screen.blit(color_text, color_rect)

        for i, color in enumerate(COLORS):
            rect = pygame.Rect(start_x + i * 25, start_y, 20, 20)
            pygame.draw.rect(self.screen, color, rect)
            if self.selected_colors[player_or_enemy] == color:
                pygame.draw.rect(self.screen, WHITE, rect, 2)
            self.buttons[f'{player_or_enemy}_color_{i}'] = rect

    def get_state(self, pos):
        if self.buttons['back'].collidepoint(pos):
            return 'main_menu'
        if self.buttons['start_game'].collidepoint(pos):
            return 'friend_mode'
        for key, rect in self.buttons.items():
            if rect.collidepoint(pos):
                if key.startswith('player_color_'):
                    index = int(key.split('_')[-1])
                    self.selected_colors['player'] = COLORS[index]
                    self.draw_friend_mode()
                elif key.startswith('enemy_color_'):
                    index = int(key.split('_')[-1])
                    self.selected_colors['enemy'] = COLORS[index]
                    self.draw_friend_mode()
        return None
