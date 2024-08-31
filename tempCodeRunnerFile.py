import pygame
import sys
from settings import WIDTH, HEIGHT, BLACK, WHITE, GREEN, RED, BLUE, COLORS, DEFAULT_PLAYER_COLOR, DEFAULT_ENEMY_COLOR, BLUE_1, Cyan, Hot_Pink, Orange
from database import load_game_data

class MainMenu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pac-Man Game - Main Menu")
        self.font = pygame.font.Font(None, 30)
        self.button_font = pygame.font.Font(None, 22)
        self.running = True
        self.showing_stats = False
        self.showing_settings = False
        self.showing_achievements = False
        self.showing_ai = False
        self.super_power_enabled = False
        self.showing_exit = False  

        self.selected_colors = {
            'player': DEFAULT_PLAYER_COLOR,
            'enemy': DEFAULT_ENEMY_COLOR
        }
        self.game_data = load_game_data()
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

     exit_button_text = self.button_font.render("Exit", True, RED)
     exit_button_rect = exit_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 210))
     pygame.draw.rect(self.screen, WHITE, exit_button_rect.inflate(6, 3))
     self.screen.blit(exit_button_text, exit_button_rect)

     pygame.display.flip()

     self.buttons = {
        "start_game": start_button_rect,
        "stats": stats_button_rect,
        "settings": settings_button_rect,
        "achievements": achievements_button_rect,
        "ai": ai_button_rect,
        "exit": exit_button_rect
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

        super_power_text = self.font.render(f"Super Power: {'ON' if self.super_power_enabled else 'OFF'}", True, WHITE)
        super_power_rect = super_power_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80))
        self.screen.blit(super_power_text, super_power_rect)

        toggle_button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 100, 100, 30)
        pygame.draw.rect(self.screen, GREEN if self.super_power_enabled else RED, toggle_button_rect)
        toggle_button_text = self.font.render("Toggle Power", True, WHITE)
        toggle_button_text_rect = toggle_button_text.get_rect(center=toggle_button_rect.center)
        self.screen.blit(toggle_button_text, toggle_button_text_rect)

        back_button_text = self.font.render("Back", True, RED)
        back_button_rect = back_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
        pygame.draw.rect(self.screen, WHITE, back_button_rect.inflate(8, 4))
        self.screen.blit(back_button_text, back_button_rect)

        pygame.display.flip()

        return back_button_rect, toggle_button_rect

    def draw_achievements(self):
        self.screen.fill(BLACK)
        achievements_title = self.font.render("Achievements", True, WHITE)
        achievements_title_rect = achievements_title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 120))
        self.screen.blit(achievements_title, achievements_title_rect)

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

        ai_text = self.font.render("AI settings will be displayed here.", True, WHITE)
        ai_rect = ai_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(ai_text, ai_rect)

        back_button_text = self.font.render("Back", True, RED)
        back_button_rect = back_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 130))
        pygame.draw.rect(self.screen, WHITE, back_button_rect.inflate(8, 4))
        self.screen.blit(back_button_text, back_button_rect)

        pygame.display.flip()

        return back_button_rect

    def draw_exit(self):
     self.screen.fill(BLACK)

     exit_title = self.font.render("Are you sure you want to exit?", True, WHITE)
     exit_title_rect = exit_title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60))
     self.screen.blit(exit_title, exit_title_rect)

     confirm_button_text = self.font.render("Yes", True, GREEN)
     confirm_button_rect = confirm_button_text.get_rect(center=(WIDTH // 2 - 60, HEIGHT // 2 + 20))
     pygame.draw.rect(self.screen, WHITE, confirm_button_rect.inflate(6, 3))
     self.screen.blit(confirm_button_text, confirm_button_rect)

     cancel_button_text = self.font.render("No", True, RED)
     cancel_button_rect = cancel_button_text.get_rect(center=(WIDTH // 2 + 60, HEIGHT // 2 + 10))
     pygame.draw.rect(self.screen, WHITE, cancel_button_rect.inflate(6, 3))
     self.screen.blit(cancel_button_text, cancel_button_rect)

     pygame.display.flip()

     return confirm_button_rect, cancel_button_rect


    def get_selected_colors(self):
        return self.selected_colors

    def run(self):
        while self.running:
            if self.showing_settings:
                back_button, toggle_button = self.draw_settings()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if back_button.collidepoint(event.pos):
                            self.showing_settings = False
                            self.draw_main_menu()
                        if toggle_button.collidepoint(event.pos):
                            self.super_power_enabled = not self.super_power_enabled
                            self.draw_settings()
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
            elif self.showing_exit:
                confirm_button, cancel_button = self.draw_exit()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if confirm_button.collidepoint(event.pos):
                            pygame.quit()
                            sys.exit()
                        if cancel_button.collidepoint(event.pos):
                            self.showing_exit = False
                            self.draw_main_menu()
            else:
                start_button = self.buttons["start_game"]
                stats_button = self.buttons["stats"]
                settings_button = self.buttons["settings"]
                achievements_button = self.buttons["achievements"]
                ai_button = self.buttons["ai"]
                exit_button = self.buttons["exit"]

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
                        if exit_button.collidepoint(event.pos):
                            self.showing_exit = True
                            self.draw_exit()
