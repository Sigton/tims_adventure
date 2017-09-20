import pygame

from src.etc import constants
from src.terrain.tile_image_loader import *
from src.terrain.tile_types import *

"""
tiles.py

This file holds the class for the 
tiles that make up the ground.
"""


class Tile:

    def __init__(self, tile_num, x, y, o_x, o_y, tile_code):

        # A tile is a 48x48 image that
        # is part of the ground.

        self.tile_code = tile_code

        self.image = images[tile_num]

        self.rect = self.image.get_rect()
        self.rect.x = x * constants.tile_w
        self.rect.y = y * constants.tile_h

        self.offset_x = o_x
        self.offset_y = o_y

    def realign(self, x, y):

        self.rect.x = x + self.offset_x * constants.tile_w
        self.rect.y = y + self.offset_y * constants.tile_h


class AnimatedTile:

    def __init__(self, tile_images_index, x, y, o_x, o_y, tile_code):

        self.tile_code = tile_code

        self.images = [tile for tile in images[tile_images_index]]
        self.image = self.images[0]

        self.rect = self.image.get_rect()
        self.rect.x = x * constants.tile_w
        self.rect.y = y * constants.tile_h

        self.offset_x = o_x
        self.offset_y = o_y

        self.timer_threshold = constants.animation_thresholds[self.tile_code]
        self.current_image = 0

    def realign(self, x, y):

        self.rect.x = x + self.offset_x * constants.tile_w
        self.rect.y = y + self.offset_y * constants.tile_h

    def animate(self, frame):

        if not frame == self.current_image:
            self.current_image = frame % len(self.images)
            self.image = self.images[self.current_image]
