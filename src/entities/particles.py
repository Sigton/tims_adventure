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

            if particle.lifetime == 0:
                self.particles.remove(particle)

    def draw(self, display):

        for particle in self.particles:
            particle.draw(display)

    def clear_particles(self):

        self.particles = []


class Particle:

    def __init__(self, image, x, y, lifetime):

        self.image = image

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.lifetime = lifetime

    def update(self):

        self.lifetime -= 1

    def draw(self, display):

        display.blit(self.image, (self.rect.x, self.rect.y))


class FireParticle(Particle):

    def __init__(self, x, y, lifetime):

        self.image = particle_sprite_sheet.get_image(0, 0, 20, 20)

        Particle.__init__(self, self.image, x, y, lifetime)
