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

    def update(self, direction):

        self.head_bean.set_image(direction)

    def draw(self, display):

        display.blit(self.head_bean.image,
                     (self.head_bean.rect.x+math.cos(((self.chunk_controller.world_offset_y % 48)+180)*2)*4,
                      self.head_bean.rect.y+math.sin(((self.chunk_controller.world_offset_x-24) % 48)*2)*4))


class MainBean(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.images = {}

        self.create_images(bean_image_loader.red())

        self.image = self.images["R"]

        self.rect = self.image.get_rect()
        self.rect.center = constants.DISPLAY_CENTER

    def set_image(self, direction):

        if direction in ("R", "RU", "UR", "RD", "DR"):
            self.image = self.images["R"]
        elif direction in ("L", "LD", "DL", "LU", "UL"):
            self.image = self.images["L"]

    def create_images(self, main_image):

        self.images.clear()

        self.images["R"] = main_image
        self.images["L"] = pygame.transform.flip(main_image, True, False)
        self.images["SR"] = pygame.transform.scale(main_image, (20, 20))
        self.images["SL"] = pygame.transform.flip(self.images["SR"], True, False)
