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

    def draw(self, display):

        display.blit(self.head_bean.image, (self.head_bean.rect.x, self.head_bean.rect.x))


class MainBean(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = bean_image_loader.red()

        self.rect = self.image.get_rect()
        self.rect.center = constants.DISPLAY_CENTER
