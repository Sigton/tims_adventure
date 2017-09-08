"""
containers.py
"""


class Seed(object):

    # Using __slots__ to maximise memory efficiency
    __slots__ = ["tiles", "decs", "entities"]

    def __int__(self, tiles, decs, entities):

        self.tiles = tiles
        self.decs = decs
        self.entities = entities
