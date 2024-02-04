# Quinton Nelson
# 2/4/2024
# context.py module contains global configuration such as the screen size, fonts, menu state booleans, and other shared resources that need to be used
# throughout the application

import pygame
from models.background import Background

# Initialize Pygame
pygame.init()                               #initialize imported pygame modules  i.e. Get everything started


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
q_puzzle = False
a_puzzle = False
j_puzzle = False

# Font setup
fontMain = pygame.font.Font('.venv/assets/fonts/audiowide.ttf', 40)     #Set the main font to be used('font', font_size)

#Image setup
background = Background('.venv/assets/images/title_background.png', (0,0))               #Get the image to be used as a background

#Music setup
pygame.mixer.init()                                                 #Initialize mixer
pygame.mixer.music.load('.venv/assets/sounds/Mind-Bender.mp3')      #Load the music file
pygame.mixer.music.play(-1)                                         #Play the music on loop
pygame.mixer.music.set_volume(.5)                                   #Set volume to 50%
adjustment = .1                                                     #Volume change increment

#Game state - set to false to close the application
run = True
