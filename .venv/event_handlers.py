#Quinton Nelson
#2/4/2024
#This dictionary decides what actions to take based on what buttons were clicked. Calls methods to start puzzles, change options, exit, etc. that are included in this file

#Jason Nelson
#02/12/2024
#Added handling for _2048_submenu

import context
from context import settings_manager        #Allows access to global settings that were initialized in the context.py module
import pygame
from settings_manager import SettingsManager


def handle_back():
    context.main_menu = False
    context.options_menu = False
    context._2048 = False
    context.start_menu = False
    context.volume_menu = False
    context._2048_submenu = False
    print("Going back to main menu")

def handle_exit():
    context.run = False

def handle_options():
    context.main_menu = False
    context.options_menu = True
    context._2048 = False
    context.start_menu = False
    context.volume_menu = False

def handle_2048():
    context.main_menu = False
    context.options_menu = False
    context._2048 = True
    context.start_menu = False
    context.volume_menu = False

def handle_2048_submenu():
    context._2048_submenu = True
    context._2048 = False
    context.main_menu = False
    context.options_menu = False
    context.volume_menu = False
    
def handle_puzzle2():
    context.main_menu = False
    context.options_menu = False
    context._2048 = False
    context.start_menu = False
    context.volume_menu = False
    
def handle_puzzle3():
    context.main_menu = False
    context.options_menu = False
    context._2048 = False
    context.start_menu = False
    context.volume_menu = False
    
def handle_start():
    context.main_menu = True
    context.options_menu = False
    context._2048_submenu = False
    context._2048 = False
    context.start_menu = False
    context.volume_menu = False
    
def handle_volume():
    context.main_menu = False
    context.options_menu = False
    context._2048 = False
    context.start_menu = False
    context.volume_menu = True
    
def handle_stop():
    pygame.mixer.music.fadeout(2)
    settings_manager.set_setting('playMusic', False)
    
def handle_play():
    pygame.mixer.music.play(-1)
    settings_manager.set_setting('playMusic', True)
    
def handle_quieter():
    if pygame.mixer.music.get_busy():  # Returns True if music is playing
        current_volume = pygame.mixer.music.get_volume()
        # Adjust volume only if music is playing
        new_volume = max(0.0, min(1.0, current_volume - context.adjustment))
        pygame.mixer.music.set_volume(new_volume)
        settings_manager.set_setting('volume', new_volume)
    else:
        print("Music is not playing.")

    
def handle_louder():
    if pygame.mixer.music.get_busy():  # Returns True if music is playing
        current_volume = pygame.mixer.music.get_volume()
        # Adjust volume only if music is playing
        new_volume = max(0.0, min(1.0, current_volume + context.adjustment))
        pygame.mixer.music.set_volume(new_volume)
        settings_manager.set_setting('volume', new_volume)
    else:
        print("Music is not playing.")
        

def handle_next():
    current_song = settings_manager.get_setting('currentSong')
    if current_song == 'Mind-Bender.mp3':
        settings_manager.set_setting('currentSong', 'Glory.mp3')
        pygame.mixer.music.load('.venv/assets/music/Glory.mp3')
        pygame.mixer.music.play(-1)
    elif current_song == 'Glory.mp3':
        settings_manager.set_setting('currentSong', 'Hidden-Official.mp3')
        pygame.mixer.music.load('.venv/assets/music/Hidden-Official.mp3')
        pygame.mixer.music.play(-1)
    elif current_song == 'Hidden-Official.mp3':
        settings_manager.set_setting('currentSong', 'reset.mp3')
        pygame.mixer.music.load('.venv/assets/music/reset.mp3')
        pygame.mixer.music.play(-1)
    elif current_song == 'reset.mp3':
        settings_manager.set_setting('currentSong', 'trap.mp3')
        pygame.mixer.music.load('.venv/assets/music/trap.mp3')
        pygame.mixer.music.play(-1)
    elif current_song == 'trap.mp3':
        settings_manager.set_setting('currentSong', 'Mind-Bender.mp3')
        pygame.mixer.music.load('.venv/assets/music/Mind-Bender.mp3')
        pygame.mixer.music.play(-1)
    else:
        settings_manager.set_setting('currentSong', 'Mind-Bender.mp3')
        pygame.mixer.music.load('.venv/assets/music/Mind-Bender.mp3')
        pygame.mixer.music.play(-1)
        

# Map button actions to their handlers
action_handlers = {
    'Main Menu': handle_start,
    'Back': handle_back,
    'Exit': handle_exit,
    'Options': handle_options,
    'Volume': handle_volume,
    'Stop': handle_stop,
    'Play': handle_play,
    'Next': handle_next,
    '-': handle_quieter,
    '+': handle_louder,
    '2048': handle_2048_submenu,
    'Puzzle2': handle_puzzle2,
    'Puzzle3': handle_puzzle3,
}