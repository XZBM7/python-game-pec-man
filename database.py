import json
#
def load_game_data():
    try:
        with open("game_data.json", "r") as file:
            data = json.load(file)
            if "wins" not in data:
                data["wins"] = 0
            if "losses" not in data:
                data["losses"] = 0
            return data
    except FileNotFoundError:
        return {
            "high_score": 0,
            "player_name": "Player1",
            "games_played": 0,
            "wins": 0,
            "losses": 0
        }

def save_game_data(data):
    with open("game_data.json", "w") as file:
        json.dump(data, file, indent=4)

