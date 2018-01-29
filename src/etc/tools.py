import pygame
import gzip
import shutil

"""
tools.py

Random tools that are used throughout the game
"""


def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)


def compress(file):
    with open(file, 'rb') as f_in:
        with gzip.open(file + ".gz", "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)


def combine_images(images):

    image = pygame.Surface([960, 720])

    [image.blit(i.image, i.rect.topleft) for i in images]

    return image
