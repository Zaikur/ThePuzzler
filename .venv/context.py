# Quinton Nelson
# 2/4/2024
# context.py module contains global configuration such as the screen size, fonts, menu state booleans, and other shared resources that need to be used
# throughout the application

#Jason Nelson
#02/12/2024
#Set the initial state of _2048_submenu to false

#Ayden Hofts
#02/18/2024
#Set the intial state of _3x3 up to _8x8 to false

import pygame
from models.background import Background
from settings_manager import SettingsManager

# Initialize Pygame
pygame.init()                               #initialize imported pygame modules  i.e. Get everything started

# Get saved user settings from file
settings_manager = SettingsManager()
settings_manager.load_settings()


# Screen setup
WIDTH = 1200
HEIGHT = 685
screen = pygame.display.set_mode([WIDTH, HEIGHT])           #Set the width and height of the game window
pygame.display.set_caption('Main Menu')                     #Change window caption to Menu on startup

# Frame rate
fps = 60
timer = pygame.time.Clock()

# Menu states
main_menu = False
options_menu = False
start_menu = True
volume_menu = False
win_popup = False
lose_popup = False
load_popup = False
_2048 = False
_2048_submenu = False
_3x3 = False
_4x4 = False
_5x5 = False
_6x6 = False
_7x7 = False
_8x8 = False

# State to show whether this is the first time you've reached 2048
first_time = True


# Font setup
fontMain = pygame.font.Font('.venv/assets/fonts/audiowide.ttf', 40)     #Set the main font to be used('font', font_size)
fontScore = pygame.font.Font('.venv/assets/fonts/audiowide.ttf', 20)    #Set the score font to be used('font', font_size)

#Image setup
background = Background('.venv/assets/images/title_background.png', (0,0))               #Get the image to be used as a background

#Music setup
pygame.mixer.init()                                                                 #Initialize mixer
pygame.mixer.music.load('.venv/assets/music/' + settings_manager.get_setting('currentSong'))                       #Load the music file

if (settings_manager.get_setting('playMusic')):                                     #If the user has music set to on
    pygame.mixer.music.play(-1)                                                     #Play the music on loop

pygame.mixer.music.set_volume(settings_manager.get_setting('volume'))               #Set volume to last saved volume
adjustment = .1                                                                     #Volume change increment

#Game state - set to false to close the application
run = True