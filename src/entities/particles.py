from src.etc import spritesheet

"""
particles.py

The games particle engine
"""

particle_sprite_sheet = spritesheet.SpriteSheet("src/resources/particles.png")


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


class FireParticle(Particle):

    def __init__(self):

        self.image = particle_sprite_sheet.get_image(0, 0, 20, 20)

        Particle.__init__(self, self.image)
