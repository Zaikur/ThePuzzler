#Quinton Nelson
#2/2/2024
#This file used for game startup, navigation, and calling methods to start puzzles, change options, exit, etc.
#2/21/2024
#Added handling for popups in the main loop

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
        buttons = context.game_board.draw_board()
        
        #buttons for popups
        if context.win_popup:
            buttons = GameBoard.show_win_popup()
            context.win_popup = False
        elif context.lose_popup:
            buttons = GameBoard.show_lose_popup()
            context.lose_popup = False
   
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
                    if button.action == 'Reset' and context.game_board is not None:
                        context.game_board.reset_game()  # Reset the game board
                        context.first_time = True
                        context.win_popup = False
                        context.lose_popup = False
                        break
                    if button.action == 'Continue' and context.game_board is not None:
                        context.first_time = False
                        context.win_popup = False
                        context.load_popup = False
                        break
                    if button.action == 'Save/Exit' and context.game_board is not None:
                        context.game_board.save_game()
                        context.run = False
                        break
                        
                    # Call the corresponding action handler for other buttons
                    elif button.action in action_handlers:
                        action_handlers[button.action]()
                    # Initialize game board if a size option is clicked
                    if button.action in ['3x3', '4x4', '5x5', '6x6', '7x7', '8x8']:
                        context.game_board = GameBoard(int(button.action[0]))
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d):   #If the key pressed is a WASD key
                if board_drawn:
                    if event.key == pygame.K_w:
                        context.game_board.move('up')
                    elif event.key == pygame.K_a:
                        context.game_board.move('left')
                    elif event.key == pygame.K_s:
                        context.game_board.move('down')
                    elif event.key == pygame.K_d:
                        context.game_board.move('right')
 
    # Set the flag to indicate that the game board is drawn
    board_drawn = True if context._3x3 or context._4x4 or context._5x5 or context._6x6 or context._7x7 or context._8x8 else False
   
    pygame.display.flip()                   #Place visual elements on the screen
 
pygame.mixer.music.stop()
if board_drawn: GameBoard.save_game(context.game_board)    #Save the game state
pygame.quit()                               #When run = false the while loop ends and this will trigger and clear assets
 