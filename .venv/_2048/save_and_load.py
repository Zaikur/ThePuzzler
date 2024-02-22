# Quinton Nelson
# 2/21/2024
# This file handles saving and loading the game state

import json
import os
import numpy as np
import context


#This method saves the current board state for later use
def save_game_state(board_size, board, current_score):
    filename = f"save_state_{board_size}x{board_size}.json"
    
    # Ensure the board is converted to a list of lists with Python integers
    board_list = board.tolist()
    board_list_py = [[int(cell) for cell in row] for row in board_list]
    
    save_data = {
        'board': board_list_py,
        'current_score': int(current_score),
        'first_time': context.first_time
    }
    
    with open(filename, 'w') as file:
        json.dump(save_data, file, indent=4)


#This method loads the saved game state from a file
def load_game_state(board_size):
    filename = f"save_state_{board_size}x{board_size}.json"
    
    # Check if the save file exists
    if os.path.exists(filename):
        # Read the save data from the file
        with open(filename, 'r') as file:
            save_data = json.load(file)
            
        # Convert the list back to a numpy array for the board
        board = np.array(save_data['board'])
        current_score = save_data['current_score']
        context.first_time = save_data['first_time']
        
        return board, current_score
    else:
        # Return None if the save file doesn't exist
        return None, None
