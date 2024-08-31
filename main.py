from game import run_game
from menu import MainMenu

if __name__ == "__main__":
    menu = MainMenu()
    menu.run()  
    selected_colors = menu.get_selected_colors() 
    run_game(selected_colors)
