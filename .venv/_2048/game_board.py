# Ayden Hofts
#02/18/2024
#This class handles drawing a game board, updating the board, and checking for win conditions
 
#Quinton Nelson
#2/2/2024
#Consolidated board drawing to one method that calculates grid based on board size
#and added a method to load and save high scores
#2/21/2024
#Added logic to color tiles based on their value
#Added sounds to tile combine
#Added methods to display popups for certain game events
#2/22/2024
#Added logic to save and load game state

#2/21/2024
#Added logic to color tiles based on their value
#Added sounds to tile combine and game win

#Jason Nelson
#02/21/2024
#Added logic for checking if game is over, also added the reset button that resets the game state

#Ayden Hofts
#02/22/2024
#Added logic for moving tiles based on keyboard input and combining the tiles if they are the same
#number and mulitplying them by 2.
 
import random
import pygame
import context
import json
import os
import numpy as np
from models.button import Button
from _2048.colors import TILE_COLORS, get_font_color
from _2048.popup import Popup
from _2048.save_and_load import load_game_state, save_game_state
 
class GameBoard:
    def __init__(self, size=3):
        self.size = size  # Board size (3 for 3x3)
        if size >= 3 and size <= 6:
            self.board_width = 100 * size
            self.board_height = 100 * size
            self.cell_size = 100
        elif size > 6 and size <= 8:
            self.board_width = 75 * size
            self.board_height = 75 * size
            self.cell_size = 75    
        
        #Check for saved game states
        loaded_state = load_game_state(self.size)
        if loaded_state[0] is not None and loaded_state[1] is not None:
            self.board, self.current_score = loaded_state
        else:
            self.board = np.zeros((self.size, self.size), dtype=int)
            self.current_score = 0
            self.spawn_tile()  # Spawn 2 tiles when the board is initialized
            self.spawn_tile()

        
        self.high_score = 0
        self.load_high_score()
        
 
    def draw_board(self):
        if self.check_game_over(): context.lose_popup = True
        if self.check_win(): context.win_popup = True
        
        # Drawing logic
        center_x, center_y = context.WIDTH // 2, context.HEIGHT // 2
        board_x, board_y = center_x - self.board_width // 2, center_y - self.board_height // 2
 
        # Create an opaque box for the board
        board_surface = pygame.Surface((self.board_width, self.board_height))
        board_surface.set_alpha(210)
        board_surface.fill((0, 0, 0))
        context.screen.blit(board_surface, (board_x, board_y))
 
        # Draw cells and numbers or tiles
        for i in range(self.size):
            for j in range(self.size):
                cell_x = board_x + i * self.cell_size
                cell_y = board_y + j * self.cell_size
                value = self.board[i][j]
                pygame.draw.rect(context.screen, (255, 255, 255), (cell_x, cell_y, self.cell_size, self.cell_size), 2)
                # Draw number or tile if the value is not zero
                if value != 0:
                    tile_color = TILE_COLORS.get(value, (205, 193, 180))
                    pygame.draw.rect(context.screen, tile_color, (cell_x, cell_y, self.cell_size, self.cell_size))
                    font = pygame.font.Font(None, 36)
                    text_surface = font.render(str(value), True, get_font_color(tile_color))        #Get font color based on tile color brightness
                    text_rect = text_surface.get_rect(center=(cell_x + self.cell_size // 2, cell_y + self.cell_size // 2))
                    context.screen.blit(text_surface, text_rect)
 
        # Draw back button and scores
        buttons = self.draw_buttons()
        self.draw_scores()
       
        return buttons
 
    #This method loads the high score from a file
    def load_high_score(self):
        try:
            with open('high_score.json', 'r') as file:
                data = json.load(file)
                self.high_score = int(data.get(str(self.size), 0))
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            self.high_score = 0
 
    #This method saves the high score to a file
    def save_high_score(self):
        try:
            with open('high_score.json', 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = {}
        data[str(self.size)] = int(self.high_score)
        with open('high_score.json', 'w') as file:
            json.dump(data, file, indent=4)
 
    #This method updates the current score and high score
    def update_score(self, score):
        self.current_score = score
        if score > self.high_score:
            self.high_score = score
            self.save_high_score()
           
    #This method draws the back button on the screen
    def draw_buttons(self):
        button_width, button_height = 250, 50
        margin = 10
        
        # Position the back and save buttons at the bottom left
        back_button_x, back_button_y = margin, context.HEIGHT - button_height - margin
        save_and_exit_button_x, save_and_exit_button_y = margin, context.HEIGHT - button_height * 2 - margin * 2

        back_button = Button((back_button_x, back_button_y, button_width, button_height), 'Back', 'Back')
        save_and_exit_button = Button((save_and_exit_button_x, save_and_exit_button_y, button_width, button_height), 'Save/Exit', 'Save/Exit')
        
        # Position the reset button at the bottom right
        reset_button_x = margin
        reset_button_y = margin
        mute_button_text = "Mute" 
        if context.mute_sound: mute_button_text =  "Unmute"
        reset_button = Button((reset_button_x, reset_button_y, button_width, button_height), mute_button_text, mute_button_text)
        
        # Position the mute button at the top left
        mute_button_x = context.WIDTH - button_width - margin
        mute_button_y = context.HEIGHT - button_height - margin
        mute_button = Button((mute_button_x, mute_button_y, button_width, button_height), 'Reset', 'Reset')
        
        # Draw the buttons
        back_button.draw()
        save_and_exit_button.draw()
        reset_button.draw()
        
        return [back_button, save_and_exit_button, reset_button]

       
    #This method draws the scores on the screen
    def draw_scores(self):
        margin = 10
        score_x = context.WIDTH - margin
        score_y = margin
 
        high_score_text = f"High Score: {self.high_score}"
        current_score_text = f"Current Score: {self.current_score}"
 
        # Render the high score
        high_score_surf = context.fontScore.render(high_score_text, True, (39, 18, 48))
        high_score_rect = high_score_surf.get_rect(topright=(score_x, score_y))
 
        # Render the current score
        current_score_surf = context.fontScore.render(current_score_text, True, (39, 18, 48))
        current_score_rect = current_score_surf.get_rect(topright=(score_x, high_score_rect.bottom + 5))
 
        # Blit the score surfaces to the screen
        context.screen.blit(high_score_surf, high_score_rect)
        context.screen.blit(current_score_surf, current_score_rect)
       
    #This method spawns a new '2' tile on the board in a random empty spot
    def spawn_tile(self):
        empty_positions = [(i, j) for i in range(self.size) for j in range(self.size) if self.board[i][j] == 0]
        if empty_positions:
            # Shuffle the empty positions to randomize the tile placement
            random.shuffle(empty_positions)
            # Spawn two tiles
            for _ in range(1):
                if empty_positions:
                    i, j = empty_positions.pop()
                    self.board[i][j] = 2

    def move(self, direction):
    # Move and combine tiles based on the direction ('w', 'a', 's', 'd').
        moved = False
        combined = False

        if direction == 'up':  # Move Up
           for i in range(self.size):
                for j in range(1, self.size):
                    if self.board[i][j] != 0:
                        for k in range(j, 0, -1):
                            if self.board[i][k - 1] == 0:
                                self.board[i][k - 1] = self.board[i][k]
                                self.board[i][k] = 0
                                moved = True
                            elif self.board[i][k - 1] == self.board[i][k]:
                                self.board[i][k - 1] *= 2
                                self.board[i][k] = 0
                                self.current_score += self.board[i][k - 1]
                                moved = True
                                combined = True
                                break

        elif direction == 'left':  # Move Left
            for j in range(self.size):
                for i in range(1, self.size):
                    if self.board[i][j] != 0:
                        for k in range(i, 0, -1):
                            if self.board[k - 1][j] == 0:
                                self.board[k - 1][j] = self.board[k][j]
                                self.board[k][j] = 0
                                moved = True
                            elif self.board[k - 1][j] == self.board[k][j]:
                                self.board[k - 1][j] *= 2
                                self.board[k][j] = 0
                                self.current_score += self.board[k - 1][j]
                                moved = True
                                combined = True
                                break


        elif direction == 'down':  # Move Down
            for i in range(self.size):
                for j in range(self.size - 2, -1, -1):
                    if self.board[i][j] != 0:
                        for k in range(j, self.size - 1):
                            if self.board[i][k + 1] == 0:
                                self.board[i][k + 1] = self.board[i][k]
                                self.board[i][k] = 0
                                moved = True
                            elif self.board[i][k + 1] == self.board[i][k]:
                                self.board[i][k + 1] *= 2
                                self.board[i][k] = 0
                                self.current_score += self.board[i][k + 1]
                                moved = True
                                combined = True
                                break

        elif direction == 'right':  # Move Right
            for j in range(self.size):
                for i in range(self.size - 2, -1, -1):
                    if self.board[i][j] != 0:
                        for k in range(i, self.size - 1):
                            if self.board[k + 1][j] == 0:
                                self.board[k + 1][j] = self.board[k][j]
                                self.board[k][j] = 0
                                moved = True
                            elif self.board[k + 1][j] == self.board[k][j]:
                                self.board[k + 1][j] *= 2
                                self.board[k][j] = 0
                                self.current_score += self.board[k + 1][j]
                                moved = True
                                combined = True
                                break

        if combined:
            if not context.mute_sound: context.combine_sound.play()  # Play sound only when a combination occurs
        
        if moved:
            self.spawn_tile()  # Spawn a new tile if any movement or combination occurred
            self.update_score(self.current_score)  # Update the current score
            
        if self.check_win():
            return 'win'
        elif self.check_game_over():
            return 'game_over'
        return 'continue'

 
    def check_win(self):
        #Check if the player has reached the 2048 tile.
        if context.first_time:
            return np.any(self.board == 2048)
        else: return False
 
    def check_game_over(self):
        # Check if there are no valid moves left.
        if any(0 in row for row in self.board):
            return False  # If there are empty cells, game is not over yet.

        # Check if there are adjacent cells with the same value
        for i in range(self.size):
            for j in range(self.size):
                current_tile = self.board[i][j]
                if (i < self.size - 1 and self.board[i + 1][j] == current_tile) or \
                (j < self.size - 1 and self.board[i][j + 1] == current_tile):
                    return False  # If there are adjacent cells with the same value, game is not over yet

        return True  # If no empty cells and no adjacent cells with the same value, game is over
    
    # This method resets the game state and spawns two new tiles
    def reset_game(self):
        self.board = np.zeros((self.size, self.size), dtype=int)  # Reset the board
        self.current_score = 0  # Reset the current score
        
        # after reset, spawns 2 new tiles
        self.spawn_tile()
        self.spawn_tile()
        
        self.load_high_score()  # reload the high score on reset
        
    # This method saves the current game state to a file by calling the save_game_state method
    def save_game(self):
        save_game_state(self.size, self.board, self.current_score)
   
    # The following methods are to show popups for different game scenarios, such as game over, win, and load state
    def show_win_popup():
        popup = Popup(context.screen, "You've won!", "Continue", "Continue", "Reset")
        return popup.draw()
    
    def show_lose_popup():
        popup = Popup(context.screen, "You're out of moves.", "Try again?", "Reset", "Back")
        return popup.draw()