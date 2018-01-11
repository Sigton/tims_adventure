import sys

import pygame

from src.engines import sounds, particles
from src.etc import constants, gui_components
from src.terrain import chunks
from src.entities import bean_image_loader, icons
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

        self.load_components()

        self.sound_engine = sounds.SoundEngine()
        self.particle_engine = particles.ParticleEngine()

        self.game_exit = False

        self.chunk_controller = chunks.ChunkController(self, 16320, 66240)
        self.duel_controller = duel_controller.DuelController(self)

        self.fade_screen = gui_components.Fade()
        self.fade_screen.set_opacity(0)

        self.game_mode = 0
        self.full_screen = False

        self.fade = 0
        self.new_game_mode = -1

        self.controllers = [
            self.chunk_controller,
            self.duel_controller
        ]

    def load_components(self):

        constants.load_font()
        bean_image_loader.load_sprite_sheet()
        particles.load_sprite_sheet()
        icons.load_sprite_sheet()

    def set_full_screen(self):

        if not self.full_screen:
            self.display = pygame.display.set_mode(constants.DISPLAY_SIZE, pygame.FULLSCREEN)
            self.full_screen = True
        else:
            self.display = pygame.display.set_mode(constants.DISPLAY_SIZE)
            self.full_screen = False

    def run(self):

        pygame.time.set_timer(constants.MUSIC_START_EVENT, 1000)

        self.fade = 0

        while not self.game_exit:

            if self.fade > 0:
                self.fade -= 1

                if self.fade == 30 and self.new_game_mode >= 0:
                    self.switch_game_mode()

            else:

                if self.fade_screen.opacity > 0:
                    self.fade_screen.set_opacity(0)

                self.controllers[self.game_mode].update()

            self.particle_engine.update()

            self.display.fill(constants.WHITE)

            self.controllers[self.game_mode].draw(self.display)

            self.particle_engine.draw(self.display)

            if self.fade > 30:
                self.fade_screen.set_opacity(int(((30-(self.fade-30))/30)*255))
            elif self.fade > 0:
                self.fade_screen.set_opacity(int((self.fade/30)*255))

            self.fade_screen.draw(self.display)

            self.sound_engine.play_sounds()

            pygame.display.update()
            self.clock.tick(60)

    def switch_game_mode(self):

        self.game_mode = self.new_game_mode
        self.new_game_mode = -1

        self.controllers[self.game_mode].update()

    def switch_to(self, game_mode):

        self.new_game_mode = game_mode
        self.fade = 60


if __name__ == "__main__":
    game = Main()
    game.run()

    pygame.quit()
    sys.exit(0)
