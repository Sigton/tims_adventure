import pygame

import operator

from src import constants

"""
map_generator.py

Turns a 2000x1500 image into
JSON data.
"""


def generate_map(blueprint):

    # This function takes a blueprint diagram of a world map
    # and turns it into a format use-able by the terrain engine.

    map_img = pygame.image.load(blueprint)
    print("Image loaded.")

    map_pix_arr = pygame.PixelArray(map_img)
    print("Created pixel array with shape {}.".format(map_pix_arr.shape))

    chunks_wide = tuple(map(operator.floordiv, map_pix_arr.shape,
                           (constants.chunk_w, constants.chunk_h)))
    num_chunks = chunks_wide[0] * chunks_wide[1]
    print("Preparing to arrange {} chunks.".format(num_chunks))

    chunk_x, chunk_y = 0, 0
    for n in range(num_chunks):

        chunk_x += 1
        if chunk_x % chunks_wide[0] == 0:
            chunk_x = 0
            chunk_y += 1


if __name__ == '__main__':

    pygame.init()

    generate_map("resources/map.png")
