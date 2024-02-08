#Quinton Nelson
#2/4/2024
#This dictionary decides what actions to take based on what buttons were clicked.

import context
import pygame


def handle_back():
    context.main_menu = False
    context.options_menu = False
    context.q_puzzle = False
    context.a_puzzle = False
    context.j_puzzle = False
    context.start_menu = False
    context.volume_menu = False

def handle_exit():
    context.run = False

def handle_options():
    context.main_menu = False
    context.options_menu = True
    context.q_puzzle = False
    context.a_puzzle = False
    context.j_puzzle = False
    context.start_menu = False
    context.volume_menu = False

def handle_2048():
    context.main_menu = False
    context.options_menu = False
    context.q_puzzle = True
    context.a_puzzle = False
    context.j_puzzle = False
    context.start_menu = False
    context.volume_menu = False
    
def handle_puzzle2():
    context.main_menu = False
    context.options_menu = False
    context.q_puzzle = False
    context.a_puzzle = True
    context.j_puzzle = False
    context.start_menu = False
    context.volume_menu = False
    
def handle_puzzle3():
    context.main_menu = False
    context.options_menu = False
    context.q_puzzle = False
    context.a_puzzle = False
    context.j_puzzle = True
    context.start_menu = False
    context.volume_menu = False
    
def handle_start():
    context.main_menu = True
    context.options_menu = False
    context.q_puzzle = False
    context.a_puzzle = False
    context.j_puzzle = True
    context.start_menu = False
    context.volume_menu = False
    
def handle_volume():
    context.main_menu = False
    context.options_menu = False
    context.q_puzzle = False
    context.a_puzzle = False
    context.j_puzzle = False
    context.start_menu = False
    context.volume_menu = True
    
def handle_stop():
    pygame.mixer.music.fadeout(2)
    
def handle_play():
    pygame.mixer.music.play(-1)
    
def handle_quieter():
    if pygame.mixer.music.get_busy():  # Returns True if music is playing
        current_volume = pygame.mixer.music.get_volume()
        # Adjust volume only if music is playing
        new_volume = max(0.0, min(1.0, current_volume - context.adjustment))
        pygame.mixer.music.set_volume(new_volume)
    else:
        print("Music is not playing.")

    
def handle_louder():
    if pygame.mixer.music.get_busy():  # Returns True if music is playing
        current_volume = pygame.mixer.music.get_volume()
        # Adjust volume only if music is playing
        new_volume = max(0.0, min(1.0, current_volume + context.adjustment))
        pygame.mixer.music.set_volume(new_volume)
    else:
        print("Music is not playing.")


# Map button actions to their handlers
action_handlers = {
    'Main Menu': handle_start,
    'Back': handle_back,
    'Exit': handle_exit,
    'Options': handle_options,
    'Volume': handle_volume,
    'Stop': handle_stop,
    'Play': handle_play,
    '-': handle_quieter,
    '+': handle_louder,
    '2048': handle_2048,
    'Puzzle2': handle_puzzle2,
    'Puzzle3': handle_puzzle3,
}