"""
particles.py

The games particle engine
"""


class ParticleEngine:

    def __init__(self):

        self.particles = []

    def update(self):

        for particle in self.particles:
            particle.update()

    def draw(self, display):

        for particle in self.particles:
            particle.draw(display)

    def clear_particles(self):

        self.particles = []


class Particle:

    def __init__(self, image):

        self.image = image

        self.rect = self.image.get_rect()

    def update(self):

        pass

    def draw(self, display):

        display.blit(self.image, (self.rect.x, self.rect.y))
