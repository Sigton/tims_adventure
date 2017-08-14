import pygame
import json

from src import tiles

"""
chunks.py

This file handles the terrain chunks.

Chunks are 20x15 tile areas on the map.
Each chunk has it's unique seed, which is
saved in the save file and assigned to a location.
"""


class ChunkController:

    # The key is the seed of the chunk,
    # and then the value is
    # an array of coordinates
    # as to where that chunk
    # can be found.
    world_map = {}

    @staticmethod
    def load(chunk):

        # Loads a chunk from the save data

        # Open the save file
        with open("src/saves/maps.json", "r") as infile:
            data = json.load(infile)

            if chunk not in data:
                infile.close()
                return None
            else:
                infile.close()
                return data[chunk]
