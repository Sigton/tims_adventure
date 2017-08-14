import pygame

from src import spritesheet

"""
player.py

This is the player you see on screen.
"""


class Player(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
