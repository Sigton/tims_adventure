import json
import operator

import pygame

from src.etc import constants

"""
map_generator.py

Turns a 2000x1500 image into
JSON data.
"""

tile_colors = {15724527: "0000",  # Generic ground
               16776960: "0001",  # Blue Ground
               0: "0002",  # Path 1
               460551: "0003",  # Path 2
               986895: "0004",  # Path 3
               1513239: "0005",  # Path 4
               2039583: "0006",  # Path 5
               2565927: "0007",  # Path 6
               3092271: "0008",  # Path 7
               3618615: "0009",  # Path 8
               4144959: "0010",  # Path 9
               4671303: "0011",  # Path 10
               5197647: "0012",  # Path 11
               5723991: "0013",  # Path 12
               6250335: "0014",  # Path 13
               6776679: "0015",  # Path 14
               7303023: "0016",  # Path 15
               15198183: "0017",  # Dark Ground
               7829367: "0018",  # Wall 1
               8355711: "0019",  # Wall 2
               8882055: "0020",  # Wall 3
               9408399: "0021",  # Wall 4
               9934743: "0022",  # Wall 5
               10461087: "0023",  # Wall 6
               10987431: "0024",  # Wall 7
               11513775: "0025",  # Wall 8
               12040119: "0026",  # Wall 9
               12566463: "0027",  # Wall 10
               13092807: "0028",  # Wall 11
               13619151: "0029",  # Wall 12
               3170456: "0030",  # Chocolate River
               9973906: "0031"  # Lolipop tree
               }


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

        chunks += [[[map_pix_arr[x + (chunk_x * constants.chunk_w)][y + (chunk_y * constants.chunk_h)]
                     for x in range(constants.chunk_w)]
                    for y in range(constants.chunk_h)]]

        chunk_x += 1
        if chunk_x % chunks_wide[0] == 0:
            chunk_x = 0
            chunk_y += 1

    print("Chunks arranged, flattening...")
    chunks = [sum(chunk, []) for chunk in chunks]
    print("Chunks flattened.")

    print("Loading decorations data...")

    with open("src/saves/decs.json") as infile:
        decs = json.load(infile)
        infile.close()

    print("Decorations data loaded.")

    print("Iterating and rendering chunks...")
    chunk_data = {}
    chunk_x, chunk_y = 0, 0

    for chunk in chunks:

        if 16777215 not in chunk:

            chunk_idx, chunk_idy = chunk_x, chunk_y
            while len(str(chunk_idx)) < 2:
                chunk_idx = "0"+str(chunk_idx)

            while len(str(chunk_idy)) < 2:
                chunk_idy = "0"+str(chunk_idy)

            chunk_id = chunk_idx+chunk_idy

            chunk_data[chunk_id] = {}
            chunk_data[chunk_id]["tiles"] = "".join([tile_colors[x] for x in chunk])

            if chunk_id in decs:
                chunk_data[chunk_id]["decs"] = decs[chunk_id]
            else:
                chunk_data[chunk_id]["decs"] = []

        chunk_x += 1
        if chunk_x % chunks_wide[0] == 0:
            chunk_x = 0
            chunk_y += 1

    print("Chunk data collected.")
    print("Preparing to dump to saves file...")

    with open("src/saves/maps.json", "w") as outfile:
        json.dump(chunk_data, outfile)
        outfile.close()

    print("Chunk data dumped to saves/maps.json")


if __name__ == '__main__':

    pygame.init()

    generate_map("src/resources/map.png")