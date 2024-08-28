import pygame
import sys
import random
from settings import WIDTH, HEIGHT, FPS, BLACK, WHITE, RED, YELLOW, GREEN
from player import Player
from enemy import Enemy
from maze import Maze
from coin import Coin
from database import load_game_data, save_game_data
#
def create_coins(num_coins):
    """Create a specified number of coins at random positions."""
    coins = pygame.sprite.Group()
    for _ in range(num_coins):
        x = random.randint(30, WIDTH - 30)
        y = random.randint(30, HEIGHT - 30)
        coin = Coin(x, y)
        coins.add(coin)
    return coins

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

def spawn_enemies(round_number, all_sprites, enemies, enemy_speed):
    corners = [(0, 0), (WIDTH - 20, 0), (0, HEIGHT - 20), (WIDTH - 20, HEIGHT - 20)]
    num_enemies = round_number
    for i in range(num_enemies):
        x, y = corners[i % 4]
        enemy = Enemy(x, y, speed=enemy_speed)
        enemies.add(enemy)
        all_sprites.add(enemy)

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pac-Man Game")
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 36)
    game_over_font = pygame.font.Font(None, 100)
    win_font = pygame.font.Font(None, 100)

    game_data = load_game_data()
    high_score = game_data["high_score"]
    player_name = game_data["player_name"]
    games_played = game_data["games_played"]
    wins = game_data["wins"]
    losses = game_data["losses"]

    num_rounds = 5
    current_round = 1
    game_over = False
    score = 0

    enemy_speed = 1

    while current_round <= num_rounds:
        all_sprites = pygame.sprite.Group()
        enemies = pygame.sprite.Group()
        coins = pygame.sprite.Group()
        
        maze = Maze()
        player = Player(WIDTH // 2, HEIGHT // 2)
        all_sprites.add(player)

        num_coins = 10 + (current_round - 1) * 5
        coins = create_coins(num_coins)
        all_sprites.add(coins)

        spawn_enemies(current_round, all_sprites, enemies, enemy_speed)

        round_start_time = pygame.time.get_ticks()
        round_end_time = round_start_time + 30000

        coins_collected = 0
        enemy_movement_allowed = True

        while not game_over and pygame.time.get_ticks() < round_end_time:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            player.update(keys)

            hits = pygame.sprite.spritecollide(player, coins, True)
            if hits:
                coins_collected += len(hits)
                score += len(hits)
                print(f"Score: {score}")

            if coins_collected >= num_coins:
                enemy_movement_allowed = False
            else:
                enemy_movement_allowed = True

            if enemy_movement_allowed:
                for enemy in enemies:
                    enemy.update(player.rect.center)

            if pygame.sprite.spritecollideany(player, enemies):
                game_over = True
                losses += 1
                break

            screen.fill(BLACK)
            maze.draw(screen)
            all_sprites.draw(screen)
            draw_round_info(screen, font, current_round, num_coins - coins_collected, len(enemies))
            score_text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(score_text, (10, 50))
            pygame.display.flip()
            clock.tick(FPS)

        if game_over:
            show_message(screen, game_over_font, "Game Over!", WHITE, RED)
            pygame.time.wait(5000)
            games_played += 1
            if score > high_score:
                high_score = score
            game_data = {
                "high_score": high_score,
                "player_name": player_name,
                "games_played": games_played,
                "wins": wins,
                "losses": losses
            }
            save_game_data(game_data)
            pygame.quit()
            sys.exit()

        if coins_collected >= num_coins:
            wins += 1

        if current_round < num_rounds:
            show_message(screen, font, "Break... Wait", WHITE, RED)
            pygame.time.wait(5000)

        enemy_speed += 1
        current_round += 1

    show_message(screen, win_font, "You Win!", GREEN, BLACK)
    pygame.time.wait(5000)
    games_played += 1
    if score > high_score:
        high_score = score
    game_data = {
        "high_score": high_score,
        "player_name": player_name,
        "games_played": games_played,
        "wins": wins,
        "losses": losses
    }
    save_game_data(game_data)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    run_game()
