"""
containers.py
"""


# A Seed is the information about
# a chunk within the game
class Seed(object):

    # Using __slots__ to maximise memory efficiency
    __slots__ = ["name", "tiles", "decs", "entities"]

    def __init__(self, name, tiles, decs, entities):

        # Assign all of the attributes their values
        self.name = name
        self.tiles = tiles
        self.decs = decs
        self.entities = entities


# A SeedDict holds a list of seeds
# and has functions to manage
# the seeds held within
class SeedDict(object):

    # Using __slots__ for optimal efficiency
    __slots__ = ["seeds"]

    def __init__(self, seeds):

        # Assign the seeds
        self.seeds = seeds

    def __getitem__(self, item):

        # Get an item from the seed dict
        for seed in self.seeds:
            if seed.name == item:
                return seed

        # If the item cannot be found then
        # return a keyerror
        return KeyError

    def __setitem__(self, key, value):

        # Allow items to be assigned values
        # within the dictionary

        # If the item does not already
        # exist, then we create a new item
        if not self.__contains__(key):
            self.seeds.append(value)

        else:

            # Otherwise find the existing item
            # and replace the value
            for seed in self.seeds:
                if seed.name == key:
                    self.seeds[seed.name] = value

    def __delitem__(self, key):

        # Removes an item from the dictionary

        for seed in self.seeds:
            if seed.name == key:
                del self.seeds[seed.name]
                return

        # Return a keyerror if the item was not found
        return KeyError

    def __len__(self):

        # Returns the number of seeds
        return len(self.seeds)

    def __contains__(self, item):

        # Check if a seed exists within the dictionary
        for seed in self.seeds:
            if seed.name == item:
                return True

        return False

    def add(self, seed):

        # Add a new seed to the dictionary
        self.seeds.append(seed)


class Chunk(object):

    __slots__ = ["name", "tiles", "decs"]

    def __init__(self, name, tiles, decs):

        self.name = name
        self.tiles = tiles
        self.decs = decs

    def add_tile(self, tile):

        self.tiles.append(tile)

    def remove_tile(self, tile):

        del self.tiles[self.tiles.index(tile)]

    def add_dec(self, dec):

        self.decs.append(dec)

    def remove_dec(self, dec):

        del self.decs[self.decs.index(dec)]

    def draw(self, display, watch_layering, player):

        for tile in self.tiles:
            display.blit(tile.image, (tile.rect.x, tile.rect.y))

        if watch_layering:

            threshold_y = player.beans[0].rect.bottom

            [display.blit(dec.image, (dec.rect.x, dec.rect.y)) for dec in self.decs if dec.rect.bottom < threshold_y]
            player.draw(display)
            [display.blit(dec.image, (dec.rect.x, dec.rect.y)) for dec in self.decs if dec.rect.bottom >= threshold_y]

            player.drawn = True

        else:
            for tile in self.decs:
                display.blit(tile.image, (tile.rect.x, tile.rect.y))
