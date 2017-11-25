import pygame

from src.etc import constants
from src.terrain.tile_types import *

'''
shadows.py

This file defines the shadow class,
which is an on-screen shadow displayed
under some decorations and entities.
'''


class Shadow:

    def __init__(self, parent):

        # A shadow generates its size based
        # off of its parents dimensions.
        self.parent = parent

        self.width = self.parent.rect.width * 0.8
        try:
            self.height = self.width * shadow_width_ratios[self.parent.tile_code]
        except AttributeError:
            self.height = self.width * 0.5

        try:
            self.height_offset = self.parent.rect.height * shadow_height_ratios[self.parent.tile_code]
        except AttributeError:
            self.height_offset = self.parent.rect.height*constants.shadow_offset

        self.rect = pygame.Rect((parent.rect.x, parent.rect.y+self.height_offset), (self.width, self.height))

        self.image = pygame.Surface([self.width, self.height])

        self.image.fill(constants.WHITE)
        self.image.set_colorkey(constants.WHITE)

        pygame.draw.ellipse(self.image, constants.BLACK, [0, 0, self.width, self.height])
        self.image.set_alpha(128)

    def update(self):

        self.rect.centerx = self.parent.rect.centerx
        self.rect.y = self.parent.rect.y + self.height_offset

    def draw(self, display):

        display.blit(self.image, (self.rect.x, self.rect.y))
