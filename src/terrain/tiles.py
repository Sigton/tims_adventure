from src.entities import shadows
from src.etc import constants
from src.terrain.tile_image_loader import *
from src.terrain.tile_types import *

"""
tiles.py

This file holds the class for the 
tiles that make up the ground.
"""


class Tile:

    def __init__(self, tile_num, x, y, tile_code, to_grid):

        # A tile is a 48x48 image that
        # is part of the ground.

        self.tile_code = tile_code
        self.to_grid = to_grid

        self.image = images[tile_num]

        self.rect = self.image.get_rect()
        if self.to_grid:
            self.rect.x = x * constants.tile_w
            self.rect.y = y * constants.tile_h
        else:
            self.rect.x = x
            self.rect.y = y

        self.offset_x = self.rect.x
        self.offset_y = self.rect.y

        if self.tile_code in shadowed_decs:
            self.shadow = shadows.Shadow(self)

            self.has_shadow = True
        else:
            self.shadow = None

            self.has_shadow = False

    def realign(self, x, y):

        self.rect.x = x + self.offset_x
        self.rect.y = y + self.offset_y

        if self.has_shadow:
            self.shadow.update()

    def draw(self, display):

        if self.has_shadow:
            self.shadow.draw(display)

        display.blit(self.image, (self.rect.x, self.rect.y))


class AnimatedTile:

    def __init__(self, tile_images_index, x, y, tile_code, to_grid):

        self.tile_code = tile_code
        self.to_grid = to_grid

        self.images = [tile for tile in images[tile_images_index]]
        self.image = self.images[0]

        self.rect = self.image.get_rect()
        if self.to_grid:
            self.rect.x = x * constants.tile_w
            self.rect.y = y * constants.tile_h
        else:
            self.rect.x = x
            self.rect.y = y

        self.offset_x = self.rect.x
        self.offset_y = self.rect.y

        self.timer_threshold = constants.animation_thresholds[self.tile_code]
        self.current_image = 0

    def realign(self, x, y):

        self.rect.x = x + self.offset_x
        self.rect.y = y + self.offset_y

    def animate(self, frame):

        if not frame == self.current_image:
            self.current_image = frame % len(self.images)
            self.image = self.images[self.current_image]
