import pygame
import os

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


if __name__ == "__main__":

    pygame.init()

    generate_decs("D:/bean_rpg etc/decmaps")
