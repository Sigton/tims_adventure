import pygame

"""
bean_image_loader.py

This file loads all 
the bean images
"""

sprite_sheet = None


def load_sprite_sheet():

    global sprite_sheet
    sprite_sheet = pygame.image.load("src/resources/beans.png")
