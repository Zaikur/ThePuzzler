#Quinton Nelson
#2/4/2024
#This class used to neatly package rectangle, text, and associated metadata for a button
#Makes it much easier to create buttons and check collidepoints for click events and color change on hover


import pygame
import context

class Button:
    def __init__(self, rect, action, text, color=(228, 125, 79), hover_color=(241, 177, 111), text_color=(39, 18, 48), border_radius=5):
        self.rect = pygame.Rect(rect)  # Ensure rect is a pygame.Rect
        self.action = action  # Action can be a string identifier or a function
        self.text = text  # Button label
        self.color = color  # Normal color
        self.hover_color = hover_color  # Color when hovered over
        self.text_color = text_color  # Text color
        self.border_radius = border_radius  # Rounded corner radius

    def draw(self):
        # Determine if the mouse is over the button
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            color = self.hover_color
        else:
            color = self.color

        # Draw the button with the appropriate color
        pygame.draw.rect(context.screen, color, self.rect, border_radius=self.border_radius)
        border_color = (27, 39, 83)
        pygame.draw.rect(context.screen, border_color, self.rect, 5, 5)     #Border

        # Render and draw the text
        text_surf = context.fontMain.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        context.screen.blit(text_surf, text_rect)

    def check_click(self, position):
        # Check if a given position collides with the button
        return self.rect.collidepoint(position)
