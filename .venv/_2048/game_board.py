# Ayden Hofts
#02/18/2024
#This class handles drawing a game board, updating the board, and checking for win conditions
 
#Quinton Nelson
#2/2/2024
#Consolidated board drawing to one method that calculates grid based on board size
#and added a method to load and save high scores
 
import random
import pygame
import context
import json
import os
import numpy as np
from models.button import Button
 
 
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
        self.board = np.zeros((size, size), dtype=int)
        self.high_score = 0
        self.current_score = 0
        self.load_high_score()
        self.spawn_tile()  # Spawn a tile when the board is initialized
 
    def draw_board(self):
        self.check_game_over()
        self.check_win()
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
                pygame.draw.rect(context.screen, (255, 255, 255), (cell_x, cell_y, self.cell_size, self.cell_size), 2)
                # Draw number or tile if the value is not zero
                value = self.board[i][j]
                if value != 0:
                    # Example code to draw number/text
                    font = pygame.font.Font(None, 36)
                    text_surface = font.render(str(value), True, (255, 255, 255))
                    text_rect = text_surface.get_rect(center=(cell_x + self.cell_size // 2, cell_y + self.cell_size // 2))
                    context.screen.blit(text_surface, text_rect)
 
        # Draw back button and scores
        buttons = self.draw_back_button()
        self.draw_scores()
       
        return buttons
 
    #This method loads the high score from a file
    def load_high_score(self):
        try:
            with open('high_score.json', 'r') as file:
                data = json.load(file)
                self.high_score = data.get(str(self.size), 0)
        except FileNotFoundError:
            self.high_score = 0
 
    #This method saves the high score to a file
    def save_high_score(self):
        try:
            with open('high_score.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
        data[str(self.size)] = self.high_score
        with open('high_score.json', 'w') as file:
            json.dump(data, file, indent=4)
 
    #This method updates the current score and high score
    def update_score(self, score):
        self.current_score = score
        if score > self.high_score:
            self.high_score = score
            self.save_high_score()
           
    #This method draws the back button on the screen
    def draw_back_button(self):
        button_width, button_height = 250, 50
        margin = 10
        # Position at bottom left
        button_x, button_y = margin, context.HEIGHT - button_height - margin
 
        back_button = Button((button_x, button_y, button_width, button_height), 'Back', 'Back')
        save_and_exit_button = Button((button_x, button_y - 60, button_width, button_height), 'Save/Exit', 'Save/Exit')
        back_button.draw()
        save_and_exit_button.draw()
        return [back_button, save_and_exit_button]
       
       
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
        #Move and combine tiles based on the direction ('w', 'a', 's', 'd').
 
        pass
 
    def check_win(self):
        #Check if the player has reached the 2048 tile.
        return np.any(self.board == 2048)
 
    def check_game_over(self):
        #Check if there are no valid moves left.
        pass    
   
    #This method saves the current board state for later use
    @staticmethod
    def save_state():
        pass