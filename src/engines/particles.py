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
            "smoke": SmokeParticle,
            "snowball": SnowballParticle,
            "feather": FeatherParticle,
            "leaf": LeafParticle,
            "venom": VenomParticle,
            "lemon": LemonParticle,
            "stone": StoneParticle,
            "pink_bubbles": PinkBubbleParticle,
            "blue_bubbles": BlueBubbleParticle
        }

        self.scrolling_particles = [
            "SmokeParticle",
            "PinkBubbleParticle"
        ]

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

    def realign(self, x, y):

        for particle in self.particles + self.fade_in_particles + self.fade_out_particles:
            if str(particle) in self.scrolling_particles:
                particle.realign(x, y)


class Particle:

    def __init__(self, image, x, y, lifetime, fade_out_time, fade_in_time):

        self.image = image
        self.image.set_alpha(0)

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.offset_x, self.offset_y = self.rect.topleft

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

    def realign(self, x, y):

        self.rect.x += x
        self.rect.y += y

    def __str__(self):

        return self.__class__.__name__


class FireParticle(Particle):

    def __init__(self, x, y, lifetime, fade_out_time, fade_in_time):

        self.image = particle_sprite_sheet.get_image_src_alpha(0, 0, 40, 40)

        Particle.__init__(self, self.image, x, y, lifetime, fade_out_time, fade_in_time)


class SnowParticle(Particle):

    def __init__(self, x, y, lifetime, fade_out_time, fade_in_time):

        self.image = particle_sprite_sheet.get_image_src_alpha(40, 0, 32, 32)

        Particle.__init__(self, self.image, x, y, lifetime, fade_out_time, fade_in_time)


class ChiliParticle(Particle):

    def __init__(self, x, y, lifetime, fade_out_time, fade_in_time):

        self.image = particle_sprite_sheet.get_image_src_alpha(72, 0, 40, 34)

        Particle.__init__(self, self.image, x, y, lifetime, fade_out_time, fade_in_time)


class SmokeParticle(Particle):

    def __init__(self, x, y, lifetime, fade_out_time, fade_in_time):

        self.image = particle_sprite_sheet.get_image_src_alpha(0, 40, 20, 20)

        Particle.__init__(self, self.image, x, y, lifetime, fade_out_time, fade_in_time)


class SnowballParticle(Particle):

    def __init__(self, x, y, lifetime, fade_out_time, fade_in_time):

        self.image = particle_sprite_sheet.get_image_src_alpha(88, 34, 24, 24)

        Particle.__init__(self, self.image, x, y, lifetime, fade_out_time, fade_in_time)


class FeatherParticle(Particle):

    def __init__(self, x, y, lifetime, fade_out_time, fade_in_time):

        self.image = particle_sprite_sheet.get_image_src_alpha(74, 58, 38, 38)

        Particle.__init__(self, self.image, x, y, lifetime, fade_out_time, fade_in_time)


class LeafParticle(Particle):

    def __init__(self, x, y, lifetime, fade_out_time, fade_in_time):

        self.image = particle_sprite_sheet.get_image_src_alpha(54, 64, 20, 36)

        Particle.__init__(self, self.image, x, y, lifetime, fade_out_time, fade_in_time)


class VenomParticle(Particle):

    def __init__(self, x, y, lifetime, fade_out_time, fade_in_time):

        self.image = particle_sprite_sheet.get_image_src_alpha(34, 66, 20, 34)

        Particle.__init__(self, self.image, x, y, lifetime, fade_out_time, fade_in_time)


class LemonParticle(Particle):

    def __init__(self, x, y, lifetime, fade_out_time, fade_in_time):

        self.image = particle_sprite_sheet.get_image_src_alpha(0, 68, 30, 32)

        Particle.__init__(self, self.image, x, y, lifetime, fade_out_time, fade_in_time)


class StoneParticle(Particle):

    def __init__(self, x, y, lifetime, fade_out_time, fade_in_time):

        self.image = particle_sprite_sheet.get_image_src_alpha(68, 34, 20, 20)

        Particle.__init__(self, self.image, x, y, lifetime, fade_out_time, fade_in_time)


class PinkBubbleParticle(Particle):

    def __init__(self, x, y, lifetime, fade_out_time, fade_in_time):

        self.image = particle_sprite_sheet.get_image_src_alpha(52, 32, 16, 16)

        Particle.__init__(self, self.image, x, y, lifetime, fade_out_time, fade_in_time)


class BlueBubbleParticle(Particle):

    def __init__(self, x, y, lifetime, fade_out_time, fade_in_time):

        self.image = particle_sprite_sheet.get_image_src_alpha(52, 48, 16, 16)

        Particle.__init__(self, self.image, x, y, lifetime, fade_out_time, fade_in_time)
