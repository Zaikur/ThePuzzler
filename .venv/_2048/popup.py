# Quinton Nelson
# 2/21/2024
# This file contains logic to draw a popup over the game screen and handle button clicks

import pygame
import context
from models.button import Button  # Assuming Button class is defined properly

class Popup:
    # Initialize the popup with the screen, prompts, and button text
    def __init__(self, screen, prompt1, prompt2, button1_text, button2_text):
        self.screen = screen
        self.prompt1 = prompt1
        self.prompt2 = prompt2
        self.button1_text = button1_text
        self.button2_text = button2_text
        self.font = context.fontMain

    # Draw the popup box and buttons
    def draw(self):
        # Draw the semi-transparent rectangle
        overlay = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
        #overlay.fill((0, 0, 0, 255))  # Fully opaque black
        self.screen.blit(overlay, (0, 0))

        # Draw the popup box
        popup_rect = pygame.Rect(300, 192, 600, 300)
        pygame.draw.rect(self.screen, (241, 177, 111), popup_rect, border_radius=5)
        pygame.draw.rect(self.screen, (27, 39, 83), popup_rect, 5, 5)

        # Draw the prompts
        text_surf = self.font.render(self.prompt1, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=(popup_rect.centerx, popup_rect.top + 75))
        self.screen.blit(text_surf, text_rect)
        
        text_surf = self.font.render(self.prompt2, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=(popup_rect.centerx, popup_rect.top + 125))
        self.screen.blit(text_surf, text_rect)

        # Draw buttons
        button1 = Button((popup_rect.x + 55, popup_rect.bottom - 75, 220, 50), self.button1_text, self.button1_text)
        button2 = Button((popup_rect.right - 275, popup_rect.bottom - 75, 220, 50), self.button2_text, self.button2_text)
        button1.draw()
        button2.draw()

        return button1, button2
