import pygame
from settings import WIDTH, HEIGHT, DEFAULT_PLAYER_COLOR, DEFAULT_ENEMY_COLOR
from game import run_game
from menu import MainMenu

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    menu = MainMenu()
    mode = menu.run()
    print(f"Selected mode: {mode}")
    
    selected_colors = menu.get_selected_colors()
    
    if mode == "ai_mode":
        run_game(selected_colors, friend_mode=False)
    elif mode == "friend_mode":
        run_game(selected_colors, friend_mode=True)
    else:
        print("Error: Unknown mode selected.")
        pygame.quit()
        exit()

if __name__ == "__main__":
    main()
