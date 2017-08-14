import pygame

from src import constants, spritesheet

"""
tiles.py

This file holds the class for the 
tiles that make up the ground.
"""

# Sprite sheet data
# This is where each tile can be found on terrain.png

generic_ground = (0, 0, 48, 48)

tiles = [generic_ground]


class Tile(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data, x, y):

        # A tile is a 48x48 image that
        # is part of the ground.

        pygame.sprite.Sprite.__init__(self)

        self.image = spritesheet.SpriteSheet("src/resources/terrain.png").get_image(
            sprite_sheet_data[0],
            sprite_sheet_data[1],
            sprite_sheet_data[2],
            sprite_sheet_data[3]
        )

        self.rect = self.image.get_rect()
        self.rect.x = x*constants.tile_w
        self.rect.y = y*constants.tile_h
