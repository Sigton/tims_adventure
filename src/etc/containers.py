"""
containers.py
"""


class Seed(object):

    # Using __slots__ to maximise memory efficiency
    __slots__ = ["name", "tiles", "decs", "entities"]

    def __int__(self, name, tiles, decs, entities):

        self.name = name
        self.tiles = tiles
        self.decs = decs
        self.entities = entities
