import pygame
import random

from src import constants, tiles

"""
chunks.py

This file handles the terrain chunks.

Chunks are 20x15 tile areas on the map.
Each chunk has it's unique seed, which is
saved in the save file and assigned to a location.
"""

# The key is the seed of the chunk,
# and then the value is
# an array of coordinates
# as to where that chunk
# can be found.
world_map = {}

def load(chunk):

    # Loads a chunk from the save data
    pass
