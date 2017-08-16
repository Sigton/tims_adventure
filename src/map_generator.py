import pygame

import operator
import json

from src import constants

"""
map_generator.py

Turns a 2000x1500 image into
JSON data.
"""

tile_colors = {15724527: "00",
               16776960: "01",
               0: "02",
               460551: "03",
               986895: "04",
               1513239: "05",
               2039583: "06",
               2565927: "07",
               3092271: "08",
               3618615: "09",
               4144959: "10",
               4671303: "11",
               5197647: "12",
               5723991: "13",
               6250335: "14",
               6776679: "15",
               7303023: "16",
               15198183: "17"}


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
    print("Preparing to arrange {} chunks....".format(num_chunks))

    chunks = []

    chunk_x, chunk_y = 0, 0
    for n in range(num_chunks):

        chunks += [[[map_pix_arr[x+(chunk_x*constants.chunk_w)][y+(chunk_y*constants.chunk_h)]
                     for x in range(constants.chunk_w)]
                    for y in range(constants.chunk_h)]]

        chunk_x += 1
        if chunk_x % chunks_wide[0] == 0:
            chunk_x = 0
            chunk_y += 1

    print("Chunks arranged, flattening...")
    chunks = [sum(chunk, []) for chunk in chunks]
    print("Chunks flattened.")

    print("Iterating and rendering chunks.")
    chunk_data = {}
    chunk_x, chunk_y = 0, 0
    for chunk in chunks:

        if 16777215 not in chunk:

            chunk_idx, chunk_idy = chunk_x, chunk_y
            while len(str(chunk_idx)) < 2:
                chunk_idx = "0"+str(chunk_idx)

            while len(str(chunk_idy)) < 2:
                chunk_idy = "0"+str(chunk_idy)

            chunk_data[chunk_idx+chunk_idy] = "".join([tile_colors[x] for x in chunk])

        chunk_x += 1
        if chunk_x % chunks_wide[0] == 0:
            chunk_x = 0
            chunk_y += 1

    print("Chunk data collected.")
    print("Preparing to dump to saves file...")

    with open("saves/maps.json", "w") as outfile:
        json.dump(chunk_data, outfile)
        outfile.close()

    print("Chunk data dumped to saves/maps.json")

if __name__ == '__main__':

    pygame.init()

    generate_map("resources/map.png")
