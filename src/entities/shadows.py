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

        try:
            self.width = self.parent.rect.width * shadow_width_to_parent_ratios[self.parent.tile_code]
        except (AttributeError, KeyError):
            self.width = self.parent.rect.width * 0.8

        try:
            self.height = self.width * shadow_width_ratios[self.parent.tile_code]
        except (AttributeError, KeyError):
            self.height = self.width * 0.5

        try:
            self.height_offset = self.parent.rect.height * shadow_height_ratios[self.parent.tile_code]
        except (AttributeError, KeyError):
            self.height_offset = self.parent.rect.height*constants.shadow_offset

        try:
            self.x_offset = shadow_x_offset[self.parent.tile_code]
        except (AttributeError, KeyError):
            self.x_offset = 0

        self.image = pygame.Surface([self.width, self.height])

        self.image.fill(constants.WHITE)
        self.image.set_colorkey(constants.WHITE)

        self.rect = self.image.get_rect()
        self.rect.centerx = self.parent.rect.centerx + self.x_offset
        self.rect.y = self.parent.rect.y + self.height_offset

        pygame.draw.ellipse(self.image, constants.BLACK, [0, 0, self.width, self.height])
        self.image.set_alpha(128)

    def update(self):

        self.rect.centerx = self.parent.rect.centerx+self.x_offset
        self.rect.y = self.parent.rect.y + self.height_offset

    def draw(self, display):

        display.blit(self.image, (self.rect.x, self.rect.y))
