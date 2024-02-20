#Quinton Nelson
#2/2/2024
#This file used for game startup, navigation, and calling methods to start puzzles, change options, exit, etc.

#Jason Nelson
#02/12/2024
#Added handling for _2048_submenu

#Ayden Hofts
#02/18/2024
#Added the handling for _3x3 up to _8x8 boards

import context
import pygame
from models.menu import DrawMenu
from event_handlers import action_handlers
from _2048.game_board import GameBoard

while context.run:
    context.timer.tick(context.fps)
    context.screen.fill('light gray')
    context.screen.blit(context.background.image, context.background.rect)
    
    #This section used to decide how to react to user input - What to draw
    if context.main_menu: buttons = DrawMenu.DrawMainMenu()
    elif context.options_menu: buttons = DrawMenu.DrawOptionsMenu()
    elif context.volume_menu: buttons = DrawMenu.DrawVolumeMenu()
    elif context._2048_submenu: buttons = DrawMenu.Draw2048Submenu()
    elif context._3x3: buttons = GameBoard(3).draw_board()
    elif context._4x4: buttons = DrawMenu.Draw4x4Board()
    elif context._5x5: buttons = DrawMenu.Draw5x5Board()
    elif context._6x6: buttons = DrawMenu.Draw6x6Board()
    elif context._7x7: buttons = DrawMenu.Draw7x7Board()
    elif context._8x8: buttons = DrawMenu.Draw8x8Board()
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
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d):   #If the key pressed is a WASD key
                if pygame.K_w: GameBoard.move('up')
                elif pygame.K_a: GameBoard.move('left')
                elif pygame.K_s: GameBoard.move('down')
                elif pygame.K_d: GameBoard.move('right')
            elif event.key == pygame.K_ESCAPE:                              #If the key pressed is the escape key
                GameBoard.save_and_exit()

    pygame.display.flip()                   #Place visual elements on the screen
pygame.mixer.music.stop()
pygame.quit()                               #When run = false the while loop ends and this will trigger and clear assets