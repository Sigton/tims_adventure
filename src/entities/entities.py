from src.entities import bean_image_loader
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

    def __init__(self):

        self.bean = random.choice(list(bean_image_loader.beans.keys()))

        self.image = bean_image_loader.beans[self.bean]()

        self.rect = self.image.get_rect()
