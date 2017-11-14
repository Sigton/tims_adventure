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
    "U": (0, 48),
    "D": (0, -48),
    "R": (-48, 0),
    "L": (48, 0)
}

# Player constants
movement_speed = 16  # Must be a factor of 48

player_pos_x = 460
player_pos_y = 340

player_pos = (player_pos_x, player_pos_y)

max_trail_offset = [0, 1, 2, 3, 4]

shadow_offset = 0.7

# Tile information

animation_thresholds = {
    "0030": 4
}
