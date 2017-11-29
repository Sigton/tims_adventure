import sys

import pygame

from src import sounds
from src.etc import constants
from src.terrain import chunks
from src.entities import bean_image_loader, player, particles
from src.duel import duel_controller

"""
main.py

This is where the magic happens.
"""


class Main:

    def __init__(self):

        # Initiate pygame
        pygame.mixer.pre_init(22050, -16, 1, 512)
        pygame.mixer.init()
        pygame.init()

        # Create the display
        self.display = pygame.display.set_mode(constants.DISPLAY_SIZE)

        # Set the title on the window
        pygame.display.set_caption("Bean RPG")

        self.clock = pygame.time.Clock()

        constants.load_font()
        particles.load_sprite_sheet()

        self.sound_engine = sounds.SoundEngine()
        self.particle_engine = particles.ParticleEngine()

        self.game_exit = False

        self.chunk_controller = chunks.ChunkController(self, 16320, 66240)

        bean_image_loader.load_sprite_sheet()
        self.player = player.Player()

        self.chunk_controller.player = self.player
        self.player.set_chunk_controller(self.chunk_controller)

        self.duel_controller = duel_controller.DuelController(self, self.player.beans[0], self.player.beans[1])

    def run(self):

        self.sound_engine.queue_sound([self.sound_engine.ambient2_sound, -1])

        n = 0

        while not self.game_exit:

            # self.chunk_controller.update()
            self.duel_controller.update()

            if not n%10:
                self.particle_engine.create_particle_spread("fire", 2,
                                                            pygame.mouse.get_pos()[0],
                                                            pygame.mouse.get_pos()[1],
                                                            20, 20, 10, 5, 10)
            n+=1

            self.particle_engine.update()

            self.display.fill(constants.WHITE)

            # self.chunk_controller.draw(self.display)
            self.duel_controller.draw(self.display)
            self.particle_engine.draw(self.display)

            self.sound_engine.play_sounds()

            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Main()
    game.run()

    pygame.quit()
    sys.exit(0)
