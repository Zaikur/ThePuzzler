#Quinton Nelson
#2/17/2024
#This class used to manage user settings and save them to a file, load them from a file if it exists, and set default settings if the file doesn't exist

import json
import os

class SettingsManager:
    # Initialize the settings manager with a filename
    def __init__(self, filename='user_settings.json'):
        self.filename = filename
        self.default_settings = {
            'musicVolume': 0.5,
            'combineVolume': 0.5,
            'previousVolume': 0.5,
            'playMusic': True,
            'currentSong': 'Mind-Bender.mp3'
        }
        self.settings = {}

    # Load settings from a file or use defaults if the file doesn't exist
    def load_settings(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.settings = json.load(file)
        else:
            self.settings = self.default_settings
            self.save_settings()  # Save default settings if file doesn't exist

    # Save the current settings to a file
    def save_settings(self):
        with open(self.filename, 'w') as file:
            json.dump(self.settings, file, indent=4)

    # Get a specific setting value by key
    def get_setting(self, key):
        return self.settings.get(key, self.default_settings.get(key))

    # Set a specific setting value by key
    def set_setting(self, key, value):
        self.settings[key] = value
        self.save_settings()  # Save changes immediately
