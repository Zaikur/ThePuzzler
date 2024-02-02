#Quinton Nelson
#2/2/2024
#This file used for game startup, navigation, and calling methods to start puzzles, change options, exit, etc.

import pygame
from menu import Background 
from menu import DrawMenu

pygame.init()  #initialize imported pygame modules  i.e. Get everything started

#Set up initial window, refresh rate, caption, etc.
WIDTH = 1200
HEIGHT = 685
screen = pygame.display.set_mode([WIDTH, HEIGHT])           #Set the width and height of the game window
pygame.display.set_caption('Main Menu')                     #Change window caption to Menu on startup
fps = 60                                                    #Framerate
timer = pygame.time.Clock()                                 #How fast the game moves

#Boolean values to trigger different menu responses
main_menu = False
options_menu = False
q_puzzle = False
a_puzzle = False
j_puzzle = False

#Fonts used
font = pygame.font.Font('.venv/assets/fonts/audiowide.ttf', 54)             #Set the font to be used in the menu ('font', font_size)

#Images and other loaded assets
background = Background('.venv/assets/background.png', (0,0))               #Get the image to be used as a background

run = True
while run:
    timer.tick(fps)
    screen.blit(background.image, background.rect)
    title = font.render('THE PUZZLER', True, 'black')               #Declare title - (String, AntiAlias, Color)
    screen.blit(title, (365, 100))                                  #Place title - (CreatedTitle, (x_location, y_location))
    
    DrawMenu.DrawMainMenu(screen, font)
    
    #This section used to decide how to react to user input
    if options_menu: DrawMenu.DrawOptionsMenu(screen)
    elif q_puzzle: pass
    elif a_puzzle: pass
    elif j_puzzle: pass
    
    
    for event in pygame.event.get():        #Way out of the loop
        if event.type == pygame.QUIT:       #Default exit button in the PyGame Window
            run = False
            
            
    pygame.display.flip()                   #Place visual elements on the screen
pygame.quit()                               #When run = false the while loop ends and this will run to clear assets
