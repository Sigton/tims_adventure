import pygame

from src import constants

"""
spritesheet.py

This file holds the SpriteSheet class,
used to take images from within images.
"""


class SpriteSheet(object):

    sprite_sheet = None

    def __init__(self, filename):

        # Load the sprite sheet
        self.sprite_sheet = pygame.image.load(filename).convert()
