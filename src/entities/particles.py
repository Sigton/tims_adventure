from src.etc import spritesheet, tools

import random

"""
particles.py

The games particle engine
"""

particle_sprite_sheet = None


def load_sprite_sheet():
    global particle_sprite_sheet
    particle_sprite_sheet = spritesheet.SpriteSheet("src/resources/particles.png")


class ParticleEngine:

    def __init__(self):

        self.particles = []
        self.fade_particles = []

        self.particle_types = {
            "fire": FireParticle
        }

    def update(self):

        for particle in self.particles:
            particle.update()

            if particle.lifetime == 0:
                self.particles.remove(particle)
                self.fade_particles.append(particle)
                particle.image.set_alpha(255)

        for particle in self.fade_particles:

            particle.fade_time -= 1
            if particle.fade_time == 0:
                self.fade_particles.remove(particle)
            else:
                particle.image.set_alpha(particle.image.get_alpha()-particle.fade_increment)

    def draw(self, display):

        for particle in self.particles:
            particle.draw(display)

        for particle in self.fade_particles:
            tools.blit_alpha(display, particle.image, particle.rect.topleft, particle.image.get_alpha())

    def clear_particles(self):

        self.particles = []
        self.fade_particles = []

    def create_particle_spread(self, particle_type, amount, x, y, noise_x, noise_y,
                               lifetime, noise_lifetime, fade_out_time, fade_in_time):

        for n in range(amount):

            self.particles.append(self.particle_types[particle_type](x+random.randint(-noise_x, noise_x),
                                                                     y+random.randint(-noise_y, noise_y),
                                                                     lifetime+random.randint(-noise_lifetime,
                                                                                             noise_lifetime),
                                                                     fade_out_time, fade_in_time))


class Particle:

    def __init__(self, image, x, y, lifetime, fade_out_time, fade_in_time):

        self.image = image

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.lifetime = lifetime
        self.fade_time = fade_out_time
        self.fade_increment = 255 // fade_out_time

    def update(self):

        self.lifetime -= 1

    def draw(self, display):

        display.blit(self.image, (self.rect.x, self.rect.y))


class FireParticle(Particle):

    def __init__(self, x, y, lifetime, fade_out_time, fade_in_time):

        self.image = particle_sprite_sheet.get_image_src_alpha(0, 0, 20, 20)

        Particle.__init__(self, self.image, x, y, lifetime, fade_out_time, fade_in_time)
