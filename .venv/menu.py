#Quinton Nelson
#2/2/2024
#This file contains classes and methods pertaining or relating to menu creation and navigation

import pygame, sys

#This class loads an image for use as the background
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location        
        
        
#This class used to draw different sections of the menu
class DrawMenu():
    def DrawMainMenu(screen, font):
        pass            
    
    def DrawOptionsMenu(screen):
        pass