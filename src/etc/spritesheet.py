import pygame

from src.etc import constants

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

    def get_image(self, x, y, width, height):

        # Create a blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the sprite sheet
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Set white to transparent
        image.set_colorkey(constants.WHITE)

        # Return the image
        return image
