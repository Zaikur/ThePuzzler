#Quinton Nelson
#2/17/2024
#This class used to manage user settings and save them to a file, load them from a file if it exists, and set default settings if the file doesn't exist

import json
import os

class SettingsManager:
    def __init__(self, filename='user_settings.json'):
        self.filename = filename
        self.default_settings = {
            'volume': 0.5,
            'playMusic': True,
            'currentSong': 'Mind-Bender.mp3'
        }
        self.settings = {}

    def load_settings(self):
        """Load settings from a file or use defaults if the file doesn't exist."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.settings = json.load(file)
        else:
            self.settings = self.default_settings
            self.save_settings()  # Save default settings if file doesn't exist

    def save_settings(self):
        """Save the current settings to a file."""
        with open(self.filename, 'w') as file:
            json.dump(self.settings, file, indent=4)

    def get_setting(self, key):
        """Get a specific setting value by key."""
        return self.settings.get(key, self.default_settings.get(key))

    def set_setting(self, key, value):
        """Set a specific setting value by key."""
        self.settings[key] = value
        self.save_settings()  # Save changes immediately
