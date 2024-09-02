import pygame
import sys
from settings import WIDTH, HEIGHT, BLACK, WHITE, GREEN, RED, BLUE, COLORS, DEFAULT_PLAYER_COLOR, DEFAULT_ENEMY_COLOR, BLUE_1, Cyan, Hot_Pink, Orange
from database import load_game_data
 
class MainMenu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Phantom Escape (DEV : XZ )")
        self.font = pygame.font.Font(None, 30)
        self.button_font = pygame.font.Font(None, 22)
        self.running = True
        self.showing_stats = False
        self.showing_settings = False
        self.showing_ai = False
        self.super_power_enabled = False
        self.showing_exit = False  
        self.showing_friend_mode = False 
        self.selected_colors = {'player': DEFAULT_PLAYER_COLOR, 'enemy': DEFAULT_ENEMY_COLOR}



        self.selected_colors = {
            'player': DEFAULT_PLAYER_COLOR,
            'enemy': DEFAULT_ENEMY_COLOR
        }
        self.game_data = load_game_data()
        self.draw_main_menu()
        

    def draw_main_menu(self):
     self.screen.fill(BLACK)
     title_text = self.font.render("Phantom Escape - Main Menu ", True, WHITE)
     title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
     self.screen.blit(title_text, title_rect)

     ai_button_text = self.button_font.render(" AI mode", True, GREEN)
     ai_button_rect = ai_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60))
     pygame.draw.rect(self.screen, WHITE, ai_button_rect.inflate(20, 20))
     self.screen.blit(ai_button_text, ai_button_rect)

     friend_button_text = self.button_font.render("Play Against Friend", True, Hot_Pink)
     friend_button_rect = friend_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 15))
     pygame.draw.rect(self.screen, WHITE, friend_button_rect.inflate(20, 20))
     self.screen.blit(friend_button_text, friend_button_rect)


     stats_button_text = self.button_font.render("Statistics", True, BLUE)
     stats_button_rect = stats_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
     pygame.draw.rect(self.screen, WHITE, stats_button_rect.inflate(20, 20))
     self.screen.blit(stats_button_text, stats_button_rect)

     settings_button_text = self.button_font.render("Settings", True, RED)
     settings_button_rect = settings_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 75))
     pygame.draw.rect(self.screen, WHITE, settings_button_rect.inflate(20, 20))
     self.screen.blit(settings_button_text, settings_button_rect)


     exit_button_text = self.button_font.render("Exit", True, RED)
     exit_button_rect = exit_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 125))
     pygame.draw.rect(self.screen, WHITE, exit_button_rect.inflate(20, 20))
     self.screen.blit(exit_button_text, exit_button_rect)

     pygame.display.flip()

     self.buttons = {
        "play_against_friend": friend_button_rect, 
        "stats": stats_button_rect,
        "settings": settings_button_rect,
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
    
   
    def draw_friend_mode(self):
     self.screen.fill(BLACK)

     friend_title = self.font.render("Play Against Friend", True, WHITE)
     friend_title_rect = friend_title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 120))
     self.screen.blit(friend_title, friend_title_rect)

     player_color_text = self.font.render("Player 1 Color:", True, WHITE)
     player_color_rect = player_color_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
     self.screen.blit(player_color_text, player_color_rect)

     player_color_rects = []
     for i, color in enumerate(COLORS):
        rect = pygame.Rect(WIDTH // 2 - 90 + i * 25, HEIGHT // 2 - 20, 20, 20)
        pygame.draw.rect(self.screen, color, rect)
        if self.selected_colors['player'] == color:
            pygame.draw.rect(self.screen, WHITE, rect, 3)  
        player_color_rects.append(rect)

     enemy_color_text = self.font.render("Player 2 Color:", True, WHITE)
     enemy_color_rect = enemy_color_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
     self.screen.blit(enemy_color_text, enemy_color_rect)

     enemy_color_rects = []
     for i, color in enumerate(COLORS):
        rect = pygame.Rect(WIDTH // 2 - 90 + i * 25, HEIGHT // 2 + 60, 20, 20)
        pygame.draw.rect(self.screen, color, rect)
        if self.selected_colors['enemy'] == color:
            pygame.draw.rect(self.screen, WHITE, rect, 3)  
        enemy_color_rects.append(rect)

     start_game_text = self.button_font.render("Start Game", True, GREEN)
     start_game_rect = start_game_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 120))
     pygame.draw.rect(self.screen, WHITE, start_game_rect.inflate(6, 3))
     self.screen.blit(start_game_text, start_game_rect)

     back_button_text = self.button_font.render("Back", True, RED)
     back_button_rect = back_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 160))
     pygame.draw.rect(self.screen, WHITE, back_button_rect.inflate(6, 3))
     self.screen.blit(back_button_text, back_button_rect)

     pygame.display.flip()

     return back_button_rect, start_game_rect, player_color_rects, enemy_color_rects


    def draw_settings(self):
     self.screen.fill(BLACK)
     settings_title = self.font.render("Settings", True, WHITE)
     settings_title_rect = settings_title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 120))
     self.screen.blit(settings_title, settings_title_rect)

     player_color_text = self.font.render("Player Color:", True, WHITE)
     player_color_rect = player_color_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
     self.screen.blit(player_color_text, player_color_rect)

     player_color_rects = []
     for i, color in enumerate(COLORS):
        rect = pygame.Rect(WIDTH // 2 - 90 + i * 25, HEIGHT // 2 - 20, 20, 20)
        pygame.draw.rect(self.screen, color, rect)
        if self.selected_colors['player'] == color:
            pygame.draw.rect(self.screen, WHITE, rect, 2)
        player_color_rects.append(rect)

     enemy_color_text = self.font.render("Enemy Color:", True, WHITE)
     enemy_color_rect = enemy_color_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
     self.screen.blit(enemy_color_text, enemy_color_rect)

     enemy_color_rects = []
     for i, color in enumerate(COLORS):
        rect = pygame.Rect(WIDTH // 2 - 90 + i * 25, HEIGHT // 2 + 50, 20, 20)
        pygame.draw.rect(self.screen, color, rect)
        if self.selected_colors['enemy'] == color:
            pygame.draw.rect(self.screen, WHITE, rect, 2)
        enemy_color_rects.append(rect)

     super_power_text = self.font.render(f"REC Notification: {'ON' if self.super_power_enabled else 'OFF'}", True, WHITE)
     super_power_rect = super_power_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 85))
     self.screen.blit(super_power_text, super_power_rect)

     toggle_button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 100, 130, 30)
     pygame.draw.rect(self.screen, GREEN if self.super_power_enabled else RED, toggle_button_rect)
     toggle_button_text = self.font.render("Notification", True, WHITE)
     toggle_button_text_rect = toggle_button_text.get_rect(center=toggle_button_rect.center)
     self.screen.blit(toggle_button_text, toggle_button_text_rect)

     back_button_text = self.font.render("Back", True, RED)
     back_button_rect = back_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
     pygame.draw.rect(self.screen, WHITE, back_button_rect.inflate(8, 4))
     self.screen.blit(back_button_text, back_button_rect)

     pygame.display.flip()

     return back_button_rect, toggle_button_rect, player_color_rects, enemy_color_rects
 

    def draw_ai(self):
     self.screen.fill(BLACK)
     ai_title = self.font.render("Enhanced AI", True, WHITE)
     ai_title_rect = ai_title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 120))
     self.screen.blit(ai_title, ai_title_rect)

     

     back_button_text = self.font.render("Back", True, RED)
     back_button_rect = back_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))
     pygame.draw.rect(self.screen, WHITE, back_button_rect.inflate(8, 4))
     self.screen.blit(back_button_text, back_button_rect)

     start_game_text = self.font.render("Start Game", True, GREEN)
     start_game_rect = start_game_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
     pygame.draw.rect(self.screen, WHITE, start_game_rect.inflate(6, 3))
     self.screen.blit(start_game_text, start_game_rect)

     pygame.display.flip()

     return back_button_rect, start_game_rect


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

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return event.pos
        return None

    def run(self):
        while self.running:
            pos = self.handle_events()

            if self.showing_settings:
                back_button, toggle_button, player_color_rects, enemy_color_rects = self.draw_settings()
                if pos:
                    if back_button.collidepoint(pos):
                        self.showing_settings = False
                        self.draw_main_menu()
                    if toggle_button.collidepoint(pos):
                        self.super_power_enabled = not self.super_power_enabled
                        self.draw_settings()
                    for i, rect in enumerate(player_color_rects):
                        if rect.collidepoint(pos):
                            self.selected_colors['player'] = COLORS[i]
                            self.draw_settings() 
                    for i, rect in enumerate(enemy_color_rects):
                        if rect.collidepoint(pos):
                            self.selected_colors['enemy'] = COLORS[i]
                            self.draw_settings()  

            elif self.showing_stats:
                back_button = self.draw_stats()
                if pos:
                    if back_button.collidepoint(pos):
                        self.showing_stats = False
                        self.draw_main_menu()

            elif self.showing_ai:
                back_button, start_game_button = self.draw_ai()
                if pos:
                    if back_button.collidepoint(pos):
                        self.showing_ai = False
                        self.draw_main_menu()
                    if start_game_button.collidepoint(pos):
                        self.running = False
                        return "ai_mode"  

            elif self.showing_exit:
                confirm_button, cancel_button = self.draw_exit()
                if pos:
                    if confirm_button.collidepoint(pos):
                        pygame.quit()
                        sys.exit()
                    if cancel_button.collidepoint(pos):
                        self.showing_exit = False
                        self.draw_main_menu()

            elif self.showing_friend_mode:
                back_button, start_game_button, player_color_rects, enemy_color_rects = self.draw_friend_mode()
                if pos:
                    if back_button.collidepoint(pos):
                        self.showing_friend_mode = False
                        self.draw_main_menu()
                    if start_game_button.collidepoint(pos):
                        self.running = False
                        return "friend_mode"  
                    for i, rect in enumerate(player_color_rects):
                        if rect.collidepoint(pos):
                            self.selected_colors['player'] = COLORS[i]
                            self.draw_friend_mode 
                    for i, rect in enumerate(enemy_color_rects):
                        if rect.collidepoint(pos):
                            self.selected_colors['enemy'] = COLORS[i]
                            self.draw_friend_mode() 

            else:
                ai_button = self.buttons["ai"]
                friend_button = self.buttons["play_against_friend"]
                stats_button = self.buttons["stats"]
                settings_button = self.buttons["settings"]
                exit_button = self.buttons["exit"]

                if pos:
                    if ai_button.collidepoint(pos):
                        self.showing_ai = True
                        self.draw_ai()
                    if friend_button.collidepoint(pos):
                        self.showing_friend_mode = True
                        self.draw_friend_mode()
                    if stats_button.collidepoint(pos):
                        self.showing_stats = True
                        self.draw_stats()
                    if settings_button.collidepoint(pos):
                        self.showing_settings = True
                        self.draw_settings()
                    if exit_button.collidepoint(pos):
                        self.showing_exit = True
                        self.draw_exit()

            pygame.display.flip() 



           