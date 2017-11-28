import pygame
from pygame.constants import *

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
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()

    def get_image(self, x, y, width, height):

        # Create a blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the sprite sheet
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Set white to transparent
        image.set_colorkey(constants.WHITE)

        # Return the image
        return image

    def get_image_src_alpha(self, x, y, width, height):

        image = pygame.Surface([width, height], flags=SRCALPHA).convert_alpha()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        return image

    def create_template_image(self, template, material):

        image = self.get_image(template[0],
                               template[1],
                               template[2],
                               template[3])

        image.blit(material, (0, 0), None, BLEND_ADD)

        return image
