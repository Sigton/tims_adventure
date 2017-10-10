import pygame

from src.etc import constants
from src.terrain import tile_data

import os, json, operator

"""
dec_generator.py

This file translates external decoration
maps into JSON format. The decoration
maps are not included in source to save
storage space, so this should never be ran
in runtime.
"""


def generate_decs(map_dir):

    files = os.listdir(map_dir)

    pix_arrays = [pygame.PixelArray(pygame.image.load(file)) for file in files]

    for layer in pix_arrays:

        chunks_wide = tuple(map(operator.floordiv, layer.shape,
                                (constants.chunk_w, constants.chunk_h)))
        num_chunks = chunks_wide[0] * chunks_wide[1]

        chunks = []
        chunk_x, chunk_y = 0, 0
        for n in range(num_chunks):

            chunks += [[[layer[x + (chunk_x * constants.chunk_w)][y + (chunk_y * constants.chunk_h)]
                         for x in range(constants.chunk_w)]
                        for y in range(constants.chunk_h)]]

            chunk_x += 1
            if chunk_x % chunks_wide[0] == 0:
                chunk_x = 0
                chunk_y += 1

        chunks = [sum(chunk, []) for chunk in chunks]


if __name__ == "__main__":

    pygame.init()

    generate_decs("D:/bean_rpg etc/decmaps")
