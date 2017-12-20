import pygame

from src.etc import constants
from src.entities import bean_image_loader, icons, shadows
from src.entities.entity_meta import entity_data

import random

"""
entities.py

This file holds the classes for on screen entities,
and metadata about entities
"""


class EntityMeta:

    def __init__(self, parent):

        self.parent = parent

        self.bean = self.parent.bean

        self.max_hp = entity_data[self.bean]["max_hp"]
        self.hp = self.max_hp

        self.level = 1
        self.xp = 0

        self.energy = entity_data[self.bean]["energy"]

        self.moves = entity_data[self.bean]["moves"]
        self.attack = entity_data[self.bean]["attack"]

        self.images = self.parent.images


class RandomBean:

    def __init__(self, x, y, to_grid):

        self.bean = random.choice(list(bean_image_loader.beans.keys()))

        self.images = {}
        self.create_images(bean_image_loader.beans[self.bean]())

        self.image = self.images["R"]

        self.rect = self.image.get_rect()
        if to_grid:
            self.rect.x = x * constants.tile_w
            self.rect.y = y * constants.tile_h
        else:
            self.rect.x = x
            self.rect.y = y

        self.offset_x = self.rect.x
        self.offset_y = self.rect.y

        self.interaction_icon = icons.PressSpace(self.rect.centerx, self.rect.y - 35)

        self.meta = EntityMeta(self)
        self.shadow = shadows.Shadow(self)

    def create_images(self, main_img):

        self.images.clear()

        self.images["R"] = main_img
        self.images["L"] = pygame.transform.flip(main_img, True, False)

    def realign(self, x, y):

        self.rect.x = x + self.offset_x
        self.rect.y = y + self.offset_y

        if self.interaction_icon is not None:
            self.interaction_icon.realign(x, y)

    def update(self):

        if self.interaction_icon is not None:
            self.interaction_icon.update()

        self.shadow.update()

    def draw(self, display):

        self.shadow.draw(display)

        display.blit(self.image, (self.rect.x, self.rect.y))

        if self.interaction_icon is not None:
            self.interaction_icon.draw(display)
