from src.entities.entity_meta import entity_data

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

        self.moves = entity_data[self.bean]["moves"]
        self.attack = entity_data[self.bean]["attack"]

        self.images = self.parent.images
