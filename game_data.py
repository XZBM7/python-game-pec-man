import json

class GameData:
    def __init__(self, file_path="game_data.json"):
        self.file_path = file_path
        self.data = self.load_game_data()

    def load_game_data(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {
                "high_score": 0,
                "player_name": "Player1",
                "games_played": 0
            }

    def save_game_data(self):
        with open(self.file_path, "w") as file:
            json.dump(self.data, file, indent=4)

    def update_game_data(self, score):
        self.data["games_played"] += 1
        if score > self.data["high_score"]:
            self.data["high_score"] = score
        self.save_game_data()
