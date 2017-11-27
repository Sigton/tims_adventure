"""
particles.py

The games particle engine
"""


class Particle:

    def __init__(self, image):

        self.image = image

        self.rect = self.image.get_rect()
