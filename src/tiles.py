import pygame

"""
tiles.py

This file holds the class for the 
tiles that make up the ground.
"""

# Spritesheet data
# This is where each tile can be found on terrain.png

generic_ground = (0, 0, 48, 48)


class Tile(pygame.sprite.Sprite):

    def __init__(self):

        # A tile is a 48x48 image that
        # is part of the ground.

        pygame.sprite.Sprite.__init__(self)
