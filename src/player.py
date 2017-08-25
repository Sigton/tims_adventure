import pygame

from src import constants, bean_image_loader

"""
player.py

This is the player you see on screen.
"""


class Player(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.head_bean = MainBean()

        self.image = self.head_bean.image

        self.rect = self.head_bean.rect


class MainBean(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = bean_image_loader.red()

        self.rect = self.image.get_rect()
        self.rect.center = constants.DISPLAY_CENTER
