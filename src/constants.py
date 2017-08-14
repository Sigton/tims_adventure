"""
Constants.py

This file defines variables
that will remain unchanged
throughout the entirety of
the program.
"""

# Display dimensions

DISPLAY_WIDTH = 960
DISPLAY_HEIGHT = 720
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
DISPLAY_CENTER = (DISPLAY_WIDTH//2, DISPLAY_HEIGHT//2)

# Colours

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Terrain Generation Constants

tile_w = 48
tile_h = 48

chunk_w = 20
chunk_h = 15
num_tiles = chunk_w * chunk_h

# The number of different tiles
# that make up the ground
tile_range = [0, 0]

# Assorted variables

dir_to_movements = {
    "U": (0, 1),
    "D": (0, -1),
    "R": (-1, 0),
    "L": (1, 0)
}
