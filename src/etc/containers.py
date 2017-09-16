"""
containers.py
"""


class Seed(object):

    # Using __slots__ to maximise memory efficiency
    __slots__ = ["name", "tiles", "decs", "entities"]

    def __init__(self, name, tiles, decs, entities):

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

        return KeyError

    def __setitem__(self, key, value):

        if not self.__contains__(key):
            self.seeds.append(value)

        else:

            for seed in self.seeds:
                if seed.name == key:
                    self.seeds[seed.name] = value

    def __delitem__(self, key):

        for seed in self.seeds:
            if seed.name == key:
                del self.seeds[seed.name]

    def __len__(self):

        return len(self.seeds)

    def __contains__(self, item):

        for seed in self.seeds:
            if seed.name == item:
                return True

        return False

    def add(self, seed):

        self.seeds.append(seed)


class Chunk(object):

    __slots__ = ["name", "tiles", "decs"]
