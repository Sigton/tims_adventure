"""
particles.py

The games particle engine
"""


class ParticleEngine:

    def __init__(self):

        self.particles = []


class Particle:

    def __init__(self, image):

        self.image = image

        self.rect = self.image.get_rect()
