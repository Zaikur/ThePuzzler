#Quinton Nelson
#2/2/2024
#This file used for game startup, navigation, and calling methods to start puzzles, change options, exit, etc.

import context
import pygame
from models.menu import DrawMenu
from event_handlers import action_handlers

while context.run:
    context.timer.tick(context.fps)
    context.screen.fill('light gray')
    context.screen.blit(context.background.image, context.background.rect)
    
    #This section used to decide how to react to user input - What to draw
    if context.main_menu: buttons = DrawMenu.DrawMainMenu()
    elif context.options_menu: buttons = DrawMenu.DrawOptionsMenu()
    elif context.volume_menu: buttons = DrawMenu.DrawVolumeMenu()
    elif context._2048: pass
    else: buttons = DrawMenu.DrawStart()    
    
    #Event handling for game navigation 
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            context.run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.check_click(event.pos):
                    print(f"Clicked: {button.action}")
                    # Call the corresponding action handler
                    if button.action in action_handlers:
                        action_handlers[button.action]()

    pygame.display.flip()                   #Place visual elements on the screen
pygame.mixer.music.stop()
pygame.quit()                               #When run = false the while loop ends and this will trigger and clear assets