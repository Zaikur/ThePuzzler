#Quinton Nelson
#2/2/2024
#This file used for game startup, navigation, and calling methods to start puzzles, change options, exit, etc.

#Jason Nelson
#02/12/2024
#Added handling for _2048_submenu
#02/21/2024
# Added the reset button handling within the main loop

#Ayden Hofts
#02/18/2024
#Added the handling for _3x3 up to _8x8 boards

import context
import pygame
from models.menu import DrawMenu
from event_handlers import action_handlers
from _2048.game_board import GameBoard
 
# Create an instance of GameBoard
game_board = None
 
# Set up a flag to indicate if the game board is drawn
board_drawn = False
 
while context.run:
    context.timer.tick(context.fps)
    context.screen.fill('light gray')
    context.screen.blit(context.background.image, context.background.rect)
   
    # Draw the menu if no game board is drawn
    if not board_drawn:
        if context.main_menu:
            buttons = DrawMenu.DrawMainMenu()
        elif context.options_menu:
            buttons = DrawMenu.DrawOptionsMenu()
        elif context.volume_menu:
            buttons = DrawMenu.DrawVolumeMenu()
        elif context._2048_submenu:
            buttons = DrawMenu.Draw2048Submenu()
        else:
            buttons = DrawMenu.DrawStart()
    else:
        buttons = game_board.draw_board()
   
    #Event handling for game navigation and user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            context.run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # Get the mouse click position
            for button in buttons:
                if button.check_click(mouse_pos):
                    print(f"Clicked: {button.action}")
                    # Special handling for the Reset button
                    if button.action == 'Reset' and game_board is not None:
                        game_board.reset_game()  # Reset the game board
                        break
                    # Call the corresponding action handler for other buttons
                    elif button.action in action_handlers:
                        action_handlers[button.action]()
                    # Initialize game board if a size option is clicked
                    if button.action in ['3x3', '4x4', '5x5', '6x6', '7x7', '8x8']:
                        game_board = GameBoard(int(button.action[0]))
                        game_board.spawn_tile()
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d):   #If the key pressed is a WASD key
                if board_drawn:
                    if event.key == pygame.K_w:
                        game_board.move('up')
                    elif event.key == pygame.K_a:
                        game_board.move('left')
                    elif event.key == pygame.K_s:
                        game_board.move('down')
                    elif event.key == pygame.K_d:
                        game_board.move('right')
            elif event.key == pygame.K_ESCAPE:                              
                if board_drawn:
                    game_board.save_and_exit()
                else:
                    context.run = False
 
    # Set the flag to indicate that the game board is drawn
    board_drawn = True if context._3x3 or context._4x4 or context._5x5 or context._6x6 or context._7x7 or context._8x8 else False
   
    pygame.display.flip()                   #Place visual elements on the screen
 
pygame.mixer.music.stop()
pygame.quit()                               #When run = false the while loop ends and this will trigger and clear assets
 