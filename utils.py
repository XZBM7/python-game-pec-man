import pygame
from settings import WIDTH, HEIGHT, WHITE

def show_message(screen, font, text, color, background_color=None):
    if background_color:
        screen.fill(background_color)
    message = font.render(text, True, color)
    text_rect = message.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(message, text_rect)
    pygame.display.flip()

def draw_round_info(screen, font, round_number, coins_needed, num_enemies):
    info_text = f"Round: {round_number} | Coins Needed: {coins_needed} | Enemies: {num_enemies}"
    info_surface = font.render(info_text, True, WHITE)
    screen.blit(info_surface, (10, 10))
