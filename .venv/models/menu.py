#Quinton Nelson
#2/4/2024
#This class used to draw different sections of the menu

import context
import pygame
from models.button import Button

class DrawMenu(pygame.sprite.Sprite):
    
    #This static method accepts a list of names, menu x/y position, and menu width/height
    #Calculates button positioning and sizing based on those values
    #Returns a list of button objects
    @staticmethod
    def CreateButtons(names, menu_x, menu_y, menu_width, menu_height, button_width = 400):
        buttons = []
        button_height = 60
        button_margin = 15  # Margin between buttons
        total_buttons_height = (button_height + button_margin) * len(names) - button_margin
        start_y = menu_y + (menu_height - total_buttons_height) // 2

        for index, name in enumerate(names):
            button_y = start_y + (button_height + button_margin) * index
            rect = (menu_x + (menu_width - button_width) // 2, button_y, button_width, button_height)
            action = name  # Use the name as the action identifier
            buttons.append(Button(rect, action, name))

        return buttons
    
    #This static method places buttons on the start screen
    @staticmethod
    def DrawStart():
        # Dimensions for the menu box - Calculated from current window width and height
        menu_width = context.WIDTH // 2
        menu_height = context.HEIGHT // 2
        menu_x = ((context.WIDTH - menu_width) // 2) + 10
        menu_y = (context.HEIGHT - menu_height)
        
        button_names = ['Main Menu', 'Exit']
        buttons = DrawMenu.CreateButtons(button_names, menu_x, menu_y, menu_width, menu_height)

        for button in buttons:
            button.draw()
            
        return buttons
    
    #This static method draws the MainMenu after Start has been clicked
    @staticmethod
    def DrawMainMenu():
        # Dimensions for the menu box - Calculated from current window width and height
        menu_width = context.WIDTH // 1.5
        menu_height = context.HEIGHT
        menu_x = ((context.WIDTH - menu_width) // 2) + 10
        menu_y = (context.HEIGHT - menu_height) // 2

        # Create an opaque box
        menu_surface = pygame.Surface((menu_width, menu_height))
        menu_surface.set_alpha(210)  # Adjust alpha for opacity (0-255)
        menu_surface.fill((0, 0, 0))  # Fill with black or any color
        context.screen.blit(menu_surface, (menu_x, menu_y))

        # Button positions and names
        button_names = ['2048', 'Puzzle1', 'Puzzle2', 'Options', 'Back', 'Exit']
        buttons = DrawMenu.CreateButtons(button_names, menu_x, menu_y, menu_width, menu_height)
        
        for button in buttons:
            button.draw()

        # Return button_positions for click detection tracking
        return buttons
        
    #This static method draws the options menu
    @staticmethod
    def DrawOptionsMenu():
        # Dimensions for the menu box - Calculated from current window width and height
        menu_width = context.WIDTH // 1.5
        menu_height = context.HEIGHT
        menu_x = ((context.WIDTH - menu_width) // 2) + 10
        menu_y = (context.HEIGHT - menu_height) // 2

        # Create an opaque box
        menu_surface = pygame.Surface((menu_width, menu_height))
        menu_surface.set_alpha(210)  # Adjust alpha for opacity (0-255)
        menu_surface.fill((0, 0, 0))  # Fill with black or any color
        context.screen.blit(menu_surface, (menu_x, menu_y))

        # Button positions and names
        button_names = ['Volume', 'Main Menu']
        buttons = DrawMenu.CreateButtons(button_names, menu_x, menu_y, menu_width, menu_height)
        
        for button in buttons:
            button.draw()

        return buttons
    
    @staticmethod
    def DrawVolumeMenu():
        # Dimensions for the menu box - Calculated from current window width and height
        menu_width = context.WIDTH // 1.5
        menu_height = context.HEIGHT
        menu_x = ((context.WIDTH - menu_width) // 2) + 10
        menu_y = (context.HEIGHT - menu_height) // 2

        # Create an opaque box
        menu_surface = pygame.Surface((menu_width, menu_height))
        menu_surface.set_alpha(210)  # Adjust alpha for opacity (0-255)
        menu_surface.fill((0, 0, 0))  # Fill with black or any color
        context.screen.blit(menu_surface, (menu_x, menu_y))

        # Button positions and names
        button_names = ['Stop', 'Play', 'Main Menu']
        buttons = DrawMenu.CreateButtons(button_names, menu_x, menu_y, menu_width, menu_height)
        
        # Example of creating volume control buttons
        buttons.append(Button((menu_x + 50, menu_y + 100, 50, 50), "-", "-"))
        buttons.append(Button((menu_x + menu_width - 100, menu_y + 100, 50, 50), "+", "+"))

        # Current volume (for drawing the slider)
        volume_level = pygame.mixer.music.get_volume()  # This is a value between 0.0 and 1.0
        slider_background = pygame.Rect(menu_x + 100, menu_y + 100, menu_width - 200, 50)
        slider_foreground = pygame.Rect(menu_x + 100, menu_y + 100, (menu_width - 200) * volume_level, 50)

        # Drawing the slider background
        pygame.draw.rect(context.screen, (150, 150, 150), slider_background)
        # Drawing the slider foreground to represent the current volume
        pygame.draw.rect(context.screen, (100, 200, 100), slider_foreground)
        
        for button in buttons:
            button.draw()

        return buttons