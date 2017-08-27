import pygame

import math

from src import constants, bean_image_loader

"""
player.py

This is the player you see on screen.
"""


class Player(pygame.sprite.Sprite):

    chunk_controller = None

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.head_bean = MainBean()

    def draw(self, display):

        display.blit(self.head_bean.image,
                     (self.head_bean.rect.x+math.cos(((self.chunk_controller.world_offset_y % 48)+180)*2)*4,
                      self.head_bean.rect.y+math.sin(((self.chunk_controller.world_offset_x-24) % 48)*2)*4))


class MainBean(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = bean_image_loader.red()

        self.rect = self.image.get_rect()
        self.rect.center = constants.DISPLAY_CENTER
