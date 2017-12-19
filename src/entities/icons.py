"""
icons.py

This file defines class for various
small icons that appear about the place
"""


class Icon:

    def __init__(self, image, flash):

        self.image = image
        self.rect = self.image.get_rect()

        self.flash = flash
