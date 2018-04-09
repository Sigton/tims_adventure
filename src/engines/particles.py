from src.etc import spritesheet, tools, constants

import random
import math

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
        self.fade_out_particles = []
        self.fade_in_particles = []

        self.particle_types = {
            "fire": FireParticle,
            "snow": SnowParticle,
            "chili": ChiliParticle,
            "smoke": SmokeParticle
        }

    def update(self):

        for particle in self.particles:
            particle.update()

            if particle.lifetime == 0:
                self.particles.remove(particle)
                self.fade_out_particles.append(particle)
                particle.image.set_alpha(255)

        for particle in self.fade_out_particles:

            particle.fade_out_time -= 1
            if particle.fade_out_time == 0:
                self.fade_out_particles.remove(particle)
            else:
                particle.image.set_alpha(particle.image.get_alpha()-particle.fade_out_increment)

        for particle in self.fade_in_particles:

            particle.fade_in_time -= 1
            if particle.fade_in_time == 0:
                self.fade_in_particles.remove(particle)
                self.particles.append(particle)
            else:
                particle.image.set_alpha(particle.image.get_alpha()+particle.fade_in_increment)

    def draw(self, display):

        for particle in self.particles:
            particle.draw(display)

        for particle in self.fade_out_particles:
            tools.blit_alpha(display, particle.image, particle.rect.topleft, particle.image.get_alpha())

        for particle in self.fade_in_particles:
            tools.blit_alpha(display, particle.image, particle.rect.topleft, particle.image.get_alpha())

    def clear_particles(self):

        self.particles = []
        self.fade_out_particles = []

    def create_particle_spread(self, particle_type, amount, x, y, noise_pos,
                               lifetime, noise_lifetime, fade_out_time, fade_in_time):

        for n in range(amount):

            ds = random.randint(0, noise_pos)
            angle = random.randint(0, 360)

            new_p_x = x + ds*math.cos(math.radians(angle))
            new_p_y = y + ds*math.sin(math.radians(angle))

            self.fade_in_particles.append(self.particle_types[particle_type](new_p_x,
                                                                             new_p_y,
                                                                             lifetime+random.randint(-noise_lifetime,
                                                                                                     noise_lifetime),
                                                                             fade_out_time, fade_in_time))


class Particle:

    def __init__(self, image, x, y, lifetime, fade_out_time, fade_in_time):

        self.image = image
        self.image.set_alpha(0)

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.lifetime = int(lifetime * constants.PARTICLE_LIFE_MULTIPLIER)
        if self.lifetime <= 0:
            self.lifetime = 1

        self.fade_out_time = int(fade_out_time * constants.PARTICLE_LIFE_MULTIPLIER)
        if self.fade_out_time <= 0:
            self.fade_out_time = 1
        self.fade_out_increment = 255 // self.fade_out_time

        self.fade_in_time = int(fade_in_time * constants.PARTICLE_LIFE_MULTIPLIER)
        if self.fade_in_time <= 0:
            self.fade_in_time = 1
        self.fade_in_increment = 255 // self.fade_in_time

    def update(self):

        self.lifetime -= 1

    def draw(self, display):

        display.blit(self.image, (self.rect.x, self.rect.y))


class FireParticle(Particle):

    def __init__(self, x, y, lifetime, fade_out_time, fade_in_time):

        self.image = particle_sprite_sheet.get_image_src_alpha(0, 0, 20, 20)

        Particle.__init__(self, self.image, x, y, lifetime, fade_out_time, fade_in_time)


class SnowParticle(Particle):

    def __init__(self, x, y, lifetime, fade_out_time, fade_in_time):

        self.image = particle_sprite_sheet.get_image_src_alpha(20, 0, 16, 16)

        Particle.__init__(self, self.image, x, y, lifetime, fade_out_time, fade_in_time)


class ChiliParticle(Particle):

    def __init__(self, x, y, lifetime, fade_out_time, fade_in_time):

        self.image = particle_sprite_sheet.get_image_src_alpha(36, 0, 20, 20)

        Particle.__init__(self, self.image, x, y, lifetime, fade_out_time, fade_in_time)


class SmokeParticle(Particle):

    def __init__(self, x, y, lifetime, fade_out_time, fade_in_time):

        self.image = particle_sprite_sheet.get_image_src_alpha(0, 20, 20, 20)

        Particle.__init__(self, self.image, x, y, lifetime, fade_out_time, fade_in_time)
