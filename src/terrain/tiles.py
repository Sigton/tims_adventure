import pygame

from src import constants
from src.terrain.tile_image_loader import *

"""
tiles.py

This file holds the class for the 
tiles that make up the ground.
"""


class Tile(pygame.sprite.Sprite):

    def __init__(self, tile_num, x, y, o_x, o_y):

        # A tile is a 48x48 image that
        # is part of the ground.

        pygame.sprite.Sprite.__init__(self)

        self.image = images[tile_num]

        self.rect = self.image.get_rect()
        self.rect.x = x*constants.tile_w
        self.rect.y = y*constants.tile_h

        self.offset_x = o_x
        self.offset_y = o_y

    def realign(self, x, y):

        self.rect.x = x+self.offset_x * constants.tile_w
        self.rect.y = y+self.offset_y * constants.tile_h

    def reuse(self, tile_num, x, y, o_x, o_y):

        self.image = images[tile_num]

        self.rect = self.image.get_rect()
        self.rect.x = x * constants.tile_w
        self.rect.y = y * constants.tile_h

        self.offset_x = o_x
        self.offset_y = o_y


class AnimatedTile(pygame.sprite.Sprite):

    def __init__(self, tile_images_index, x, y, o_x, o_y):

        pygame.sprite.Sprite.__init__(self)

        self.images = [tile for tile in images[tile_images_index]]
        self.image = self.images[0]

        self.rect = self.image.get_rect()
        self.rect.x = x*constants.tile_w
        self.rect.y = y*constants.tile_h

        self.offset_x = o_x
        self.offset_y = o_y

        self.timer_threshold = 20
        self.current_image = 0
        self.timer = 0

    def realign(self, x, y):

        self.rect.x = x+self.offset_x * constants.tile_w
        self.rect.y = y+self.offset_y * constants.tile_h

    def animate(self):

        self.timer += 1

        if self.timer > self.timer_threshold:
            self.timer = 0
            self.current_image += 1
            self.image = self.images[self.current_image]
