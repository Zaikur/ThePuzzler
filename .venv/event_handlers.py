#Quinton Nelson
#2/4/2024
#This dictionary decides what actions to take based on what buttons were clicked. Calls methods to start puzzles, change options, exit, etc. that are included in this file

#Jason Nelson
#02/12/2024
#Added handling for _2048_submenu
#02/19/2024
#updated the action handler of handle_back to take the player back to the submenu if they use the back button in a game, otherwise the back button will take them to the main menu.

#Ayden Hofts
#02/18/2024
#Added handling for the _3x3 and up to _8x8 boards

import context
from context import settings_manager        #Allows access to global settings that were initialized in the context.py module
import pygame
from _2048.game_board import GameBoard


def reset_context():
    context.main_menu = False
    context.options_menu = False
    context._2048 = False
    context.start_menu = False
    context.volume_menu = False
    context._2048_submenu = False
    context._3x3 = False
    context._4x4 = False
    context._5x5 = False
    context._6x6 = False
    context._7x7 = False
    context._8x8 = False

def handle_back():
    if not context.main_menu:
        handle_2048_submenu()
    else:
        reset_context()
        print("Going back to main menu")

def handle_exit():
    context.run = False

def handle_options():
    reset_context()
    context.options_menu = True

def handle_2048():
    reset_context()
    context._2048 = True

def handle_2048_submenu():
    reset_context()
    context._2048_submenu = True

def handle_3x3():
    reset_context()
    context._3x3 = True

def handle_4x4():
    reset_context()
    context._4x4 = True

def handle_5x5():
    reset_context()
    context._5x5 = True

def handle_6x6():
    reset_context()
    context._6x6 = True

def handle_7x7():
    reset_context()
    context._7x7 = True

def handle_8x8():
    reset_context()
    context._8x8 = True
    
def handle_start():
    reset_context()
    context.main_menu = True
    
def handle_volume():
    reset_context()
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
        
def handle_save_and_exit():
    GameBoard.save_state()
    handle_exit()
        

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
    '3x3': handle_3x3,
    '4x4': handle_4x4,
    '5x5': handle_5x5,
    '6x6': handle_6x6,
    '7x7': handle_7x7,
    '8x8': handle_8x8,
    'Save/Exit': handle_save_and_exit
}