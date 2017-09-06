import pygame

from src.etc import constants
from src.terrain.tile_image_loader import *
from src.terrain.tile_types import *

"""
tiles.py

This file holds the class for the 
tiles that make up the ground.
"""


class Tile(pygame.sprite.Sprite):

    def __init__(self, tile_num, x, y, o_x, o_y, tile_code):

        # A tile is a 48x48 image that
        # is part of the ground.

        pygame.sprite.Sprite.__init__(self)

        self.tile_code = tile_code

        self.image = images[tile_num]

        self.rect = self.image.get_rect()
        self.rect.x = x * constants.tile_w
        self.rect.y = y * constants.tile_h

        self.offset_x = o_x
        self.offset_y = o_y

    def realign(self, x, y):

        self.rect.x = x+ self.offset_x * constants.tile_w
        self.rect.y = y+ self.offset_y * constants.tile_h

    def reuse(self, tile_num, x, y, o_x, o_y, tile_code):

        if tile_code in animated_tiles:
            new_tile = AnimatedTile(tile_num, x, y, o_x, o_y, tile_code)
            [group.add(new_tile) for group in self.groups()]
        else:
            self.tile_code = tile_code

            self.image = images[tile_num]

            self.rect = self.image.get_rect()
            self.rect.x = x * constants.tile_w
            self.rect.y = y * constants.tile_h

            self.offset_x = o_x
            self.offset_y = o_y


class AnimatedTile(pygame.sprite.Sprite):

    def __init__(self, tile_images_index, x, y, o_x, o_y, tile_code):

        pygame.sprite.Sprite.__init__(self)

        self.tile_code = tile_code

        self.images = [tile for tile in images[tile_images_index]]
        self.image = self.images[0]

        self.rect = self.image.get_rect()
        self.rect.x = x * constants.tile_w
        self.rect.y = y * constants.tile_h

        self.offset_x = o_x
        self.offset_y = o_y

        self.timer_threshold = 15
        self.current_image = 0
        self.timer = 0

    def realign(self, x, y):

        self.rect.x = x+ self.offset_x * constants.tile_w
        self.rect.y = y+ self.offset_y * constants.tile_h

    def animate(self):

        self.timer += 1

        if self.timer > self.timer_threshold:
            self.timer = 0
            self.current_image = (self.current_image + 1) % len(self.images)
            self.image = self.images[self.current_image]

    def reuse(self):

        pass
