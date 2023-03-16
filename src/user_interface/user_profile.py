import json


class UserProfile:
    def __init__(self, user_id):
        self.user_id = user_id
        self.preferences_file = f"user_preferences/{user_id}.json"
        self.preferences = self.load_preferences()

    def load_preferences(self):
        try:
            with open(self.preferences_file, "r") as f:
                preferences = json.load(f)
        except FileNotFoundError:
            preferences = {
                "movies": True,
                "tv_shows": True,
                "graphic_novels": True,
                "nfts": True
            }
            self.save_preferences(preferences)
        return preferences

    def save_preferences(self, preferences):
        with open(self.preferences_file, "w") as f:
            json.dump(preferences, f, indent=2)

    def update_preferences(self, preferences):
        self.preferences.update(preferences)
        self.save_preferences(self.preferences)

    def get_preferences(self):
        return self.preferences
