import json
import os

DATA_FILE = 'game_data.json'

def load_game_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    else:
        return {
            "high_score": 0,
            "player_name": "Player",
            "games_played": 0,
            "wins": 0,
            "losses": 0
        }

def save_game_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)
