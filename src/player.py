import pygame

from src import constants, spritesheet

"""
player.py

This is the player you see on screen.
"""


class Player(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([40, 40]).convert()

        self.rect = self.image.get_rect()
        self.rect.center = constants.DISPLAY_CENTER
