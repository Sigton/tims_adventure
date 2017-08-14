import pygame
import json

from src import constants, tiles

"""
chunks.py

This file handles the terrain chunks.

Chunks are 20x15 tile areas on the map.
Each chunk has it's unique seed, which is
saved in the save file and assigned to a location.
"""


class ChunkController:

    def __init__(self):

        # The key is a 4 digit string
        # to locate the chunk,
        # and then the value is that
        # chunks seed.
        self.map_seeds = {}
        self.map_tiles = {}

        self.load("0000")

    def load(self, chunk):

        # Loads a chunk from the save data

        # Open the save file
        with open("src/saves/maps.json", "r") as infile:
            data = json.load(infile)
            infile.close()

        self.map_seeds[chunk] = data[chunk]

    def create_chunk(self, chunk):

        # Creates a group of tile objects
        # from the seed of the given chunk

        seed = self.map_seeds[chunk]
        new_chunk = pygame.sprite.Group()

        tile_data = [seed[i:i+2] for i in range(0, len(seed), 2)]
        x, y = 0, 0

        for n in tile_data:
            x += 1

            tile = tiles.tiles[int(n)]
            new_chunk.add(tiles.Tile(tile))

            if x % constants.chunk_w-1 == 0:
                x = 0
                y += 1

        self.map_tiles[chunk] = new_chunk
