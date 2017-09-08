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


class SeedDict(object):

    __slots__ = ["seeds"]

    def __init__(self, seeds):

        self.seeds = seeds

    def __getitem__(self, item):

        for seed in self.seeds:
            if seed.name == item:
                return seed
