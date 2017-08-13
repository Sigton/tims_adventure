import pygame

"""
tiles.py

This file holds the class for the 
tiles that make up the ground.
"""


class Tile(pygame.sprite.Sprite):

    def __init__(self):

        # A tile is a 48x48 image that
        # is part of the ground.

        pygame.sprite.Sprite.__init__(self)
