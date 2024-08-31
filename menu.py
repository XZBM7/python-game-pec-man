import pygame
import sys
from settings import WIDTH, HEIGHT, BLACK, WHITE, GREEN, RED, BLUE, COLORS, DEFAULT_PLAYER_COLOR, DEFAULT_ENEMY_COLOR, BLUE_1, Cyan, Hot_Pink, Orange
from database import load_game_data

class MainMenu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pac-Man Game - Main Menu")
        self.font = pygame.font.Font(None, 30)  # Smaller font for title
        self.button_font = pygame.font.Font(None, 22)  # Smaller font for buttons
        self.running = True
        self.showing_stats = False
        self.showing_settings = False
        self.showing_achievements = False
        self.showing_ai = False
        self.showing_darkness = False
        self.selected_colors = {
            'player': DEFAULT_PLAYER_COLOR,
            'enemy': DEFAULT_ENEMY_COLOR
        }
        self.game_data = load_game_data()  # Load game data here
        self.draw_main_menu()

    def draw_main_menu(self):
        self.screen.fill(BLACK)
        title_text = self.font.render("Pac-Man Game", True, WHITE)
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 120))
        self.screen.blit(title_text, title_rect)

        start_button_text = self.button_font.render("Start Game", True, GREEN)
        start_button_rect = start_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
        pygame.draw.rect(self.screen, WHITE, start_button_rect.inflate(6, 3))
        self.screen.blit(start_button_text, start_button_rect)

        stats_button_text = self.button_font.render("Statistics", True, BLUE)
        stats_button_rect = stats_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10))
        pygame.draw.rect(self.screen, WHITE, stats_button_rect.inflate(6, 3))
        self.screen.blit(stats_button_text, stats_button_rect)

        settings_button_text = self.button_font.render("Settings", True, RED)
        settings_button_rect = settings_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        pygame.draw.rect(self.screen, WHITE, settings_button_rect.inflate(6, 3))
        self.screen.blit(settings_button_text, settings_button_rect)

        achievements_button_text = self.button_font.render("Achievements", True, Orange)  
        achievements_button_rect = achievements_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 90))
        pygame.draw.rect(self.screen, WHITE, achievements_button_rect.inflate(6, 3))
        self.screen.blit(achievements_button_text, achievements_button_rect)

        ai_button_text = self.button_font.render("Enhanced AI", True, Cyan)  
        ai_button_rect = ai_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 130))
        pygame.draw.rect(self.screen, WHITE, ai_button_rect.inflate(6, 3))
        self.screen.blit(ai_button_text, ai_button_rect)

        darkness_button_text = self.button_font.render("Darkness Effect", True, Hot_Pink)  
        darkness_button_rect = darkness_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 170))
        pygame.draw.rect(self.screen, WHITE, darkness_button_rect.inflate(6, 3))
        self.screen.blit(darkness_button_text, darkness_button_rect)

        pygame.display.flip()

        self.buttons = {
            "start_game": start_button_rect,
            "stats": stats_button_rect,
            "settings": settings_button_rect,
            "achievements": achievements_button_rect,
            "ai": ai_button_rect,
            "darkness": darkness_button_rect
        }

    def draw_stats(self):
        self.screen.fill(BLACK)
        stats_title = self.font.render("Game Statistics", True, WHITE)
        stats_title_rect = stats_title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 120))
        self.screen.blit(stats_title, stats_title_rect)

        high_score_text = self.font.render(f"High Score: {self.game_data['high_score']}", True, WHITE)
        high_score_rect = high_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
        self.screen.blit(high_score_text, high_score_rect)

        games_played_text = self.font.render(f"Games Played: {self.game_data['games_played']}", True, WHITE)
        games_played_rect = games_played_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(games_played_text, games_played_rect)

        wins_text = self.font.render(f"Wins: {self.game_data['wins']}", True, WHITE)
        wins_rect = wins_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))
        self.screen.blit(wins_text, wins_rect)

        losses_text = self.font.render(f"Losses: {self.game_data['losses']}", True, WHITE)
        losses_rect = losses_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80))
        self.screen.blit(losses_text, losses_rect)

        back_button_text = self.font.render("Back", True, RED)
        back_button_rect = back_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 130))
        pygame.draw.rect(self.screen, WHITE, back_button_rect.inflate(8, 4))
        self.screen.blit(back_button_text, back_button_rect)

        pygame.display.flip()

        return back_button_rect

    def draw_settings(self):
        self.screen.fill(BLACK)
        settings_title = self.font.render("Settings", True, WHITE)
        settings_title_rect = settings_title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 120))
        self.screen.blit(settings_title, settings_title_rect)

        player_color_text = self.font.render(f"Player Color:", True, WHITE)
        player_color_rect = player_color_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
        self.screen.blit(player_color_text, player_color_rect)

        for i, color in enumerate(COLORS):
            pygame.draw.rect(self.screen, color, pygame.Rect(WIDTH // 2 - 90 + i * 25, HEIGHT // 2 - 20, 20, 20))
            if self.selected_colors['player'] == color:
                pygame.draw.rect(self.screen, WHITE, pygame.Rect(WIDTH // 2 - 90 + i * 25, HEIGHT // 2 - 20, 20, 20), 2)

        enemy_color_text = self.font.render(f"Enemy Color:", True, WHITE)
        enemy_color_rect = enemy_color_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
        self.screen.blit(enemy_color_text, enemy_color_rect)

        for i, color in enumerate(COLORS):
            pygame.draw.rect(self.screen, color, pygame.Rect(WIDTH // 2 - 90 + i * 25, HEIGHT // 2 + 50, 20, 20))
            if self.selected_colors['enemy'] == color:
                pygame.draw.rect(self.screen, WHITE, pygame.Rect(WIDTH // 2 - 90 + i * 25, HEIGHT // 2 + 50, 20, 20), 2)

        back_button_text = self.font.render("Back", True, RED)
        back_button_rect = back_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        pygame.draw.rect(self.screen, WHITE, back_button_rect.inflate(8, 4))
        self.screen.blit(back_button_text, back_button_rect)

        pygame.display.flip()

        return back_button_rect

    def draw_achievements(self):
        self.screen.fill(BLACK)
        achievements_title = self.font.render("Achievements", True, WHITE)
        achievements_title_rect = achievements_title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 120))
        self.screen.blit(achievements_title, achievements_title_rect)

        # Placeholder for achievements display
        achievements_text = self.font.render("Achievements will be displayed here.", True, WHITE)
        achievements_rect = achievements_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(achievements_text, achievements_rect)

        back_button_text = self.font.render("Back", True, RED)
        back_button_rect = back_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 130))
        pygame.draw.rect(self.screen, WHITE, back_button_rect.inflate(8, 4))
        self.screen.blit(back_button_text, back_button_rect)

        pygame.display.flip()

        return back_button_rect

    def draw_ai(self):
        self.screen.fill(BLACK)
        ai_title = self.font.render("Enhanced AI", True, WHITE)
        ai_title_rect = ai_title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 120))
        self.screen.blit(ai_title, ai_title_rect)

        # Placeholder for AI settings
        ai_text = self.font.render("AI settings will be displayed here.", True, WHITE)
        ai_rect = ai_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(ai_text, ai_rect)

        back_button_text = self.font.render("Back", True, RED)
        back_button_rect = back_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 130))
        pygame.draw.rect(self.screen, WHITE, back_button_rect.inflate(8, 4))
        self.screen.blit(back_button_text, back_button_rect)

        pygame.display.flip()

        return back_button_rect

    def draw_darkness(self):
        self.screen.fill(BLACK)
        darkness_title = self.font.render("Darkness Effect", True, WHITE)
        darkness_title_rect = darkness_title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 120))
        self.screen.blit(darkness_title, darkness_title_rect)

        # Placeholder for Darkness settings
        darkness_text = self.font.render("Darkness effect settings will be displayed here.", True, WHITE)
        darkness_rect = darkness_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(darkness_text, darkness_rect)

        back_button_text = self.font.render("Back", True, RED)
        back_button_rect = back_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 130))
        pygame.draw.rect(self.screen, WHITE, back_button_rect.inflate(8, 4))
        self.screen.blit(back_button_text, back_button_rect)

        pygame.display.flip()

        return back_button_rect

    def get_selected_colors(self):
        return self.selected_colors

    def run(self):
        while self.running:
            if self.showing_settings:
                back_button = self.draw_settings()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if back_button.collidepoint(event.pos):
                            self.showing_settings = False
                            self.draw_main_menu()
                        for i, color in enumerate(COLORS):
                            player_color_rect = pygame.Rect(WIDTH // 2 - 90 + i * 25, HEIGHT // 2 - 20, 20, 20)
                            enemy_color_rect = pygame.Rect(WIDTH // 2 - 90 + i * 25, HEIGHT // 2 + 50, 20, 20)
                            if player_color_rect.collidepoint(event.pos):
                                self.selected_colors['player'] = color
                            if enemy_color_rect.collidepoint(event.pos):
                                self.selected_colors['enemy'] = color
            elif self.showing_stats:
                back_button = self.draw_stats()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if back_button.collidepoint(event.pos):
                            self.showing_stats = False
                            self.draw_main_menu()
            elif self.showing_achievements:
                back_button = self.draw_achievements()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if back_button.collidepoint(event.pos):
                            self.showing_achievements = False
                            self.draw_main_menu()
            elif self.showing_ai:
                back_button = self.draw_ai()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if back_button.collidepoint(event.pos):
                            self.showing_ai = False
                            self.draw_main_menu()
            elif self.showing_darkness:
                back_button = self.draw_darkness()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if back_button.collidepoint(event.pos):
                            self.showing_darkness = False
                            self.draw_main_menu()
            else:
                start_button = self.buttons["start_game"]
                stats_button = self.buttons["stats"]
                settings_button = self.buttons["settings"]
                achievements_button = self.buttons["achievements"]
                ai_button = self.buttons["ai"]
                darkness_button = self.buttons["darkness"]
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if start_button.collidepoint(event.pos):
                            self.running = False
                            return
                        if stats_button.collidepoint(event.pos):
                            self.showing_stats = True
                            self.draw_stats()
                        if settings_button.collidepoint(event.pos):
                            self.showing_settings = True
                            self.draw_settings()
                        if achievements_button.collidepoint(event.pos):
                            self.showing_achievements = True
                            self.draw_achievements()
                        if ai_button.collidepoint(event.pos):
                            self.showing_ai = True
                            self.draw_ai()
                        if darkness_button.collidepoint(event.pos):
                            self.showing_darkness = True
                            self.draw_darkness()
