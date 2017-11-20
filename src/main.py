import sys

import pygame
from pygame.locals import *

from src import player, sounds
from src.etc import constants
from src.terrain import chunks

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

        self.sound_engine = sounds.SoundEngine()

        self.chunk_controller = chunks.ChunkController(960, 720)

        player.bean_image_loader.load_sprite_sheet()
        self.player = player.Player()

        self.chunk_controller.player = self.player
        self.player.set_chunk_controller(self.chunk_controller)

    def run(self):

        game_exit = False

        direction = ""

        self.sound_engine.queue_sound([self.sound_engine.ambient2_sound, -1])

        while not game_exit:

            for event in pygame.event.get():
                if event.type == QUIT:

                    game_exit = True

                elif event.type == KEYDOWN:

                    if event.key == K_UP:
                        direction = "U"

                    elif event.key == K_DOWN:
                        direction = "D"

                    elif event.key == K_LEFT:
                        direction = "L"

                    elif event.key == K_RIGHT:
                        direction = "R"

                elif event.type == KEYUP:

                    if event.key == K_UP:
                        direction = direction.replace("U", "")

                    elif event.key == K_DOWN:
                        direction = direction.replace("D", "")

                    elif event.key == K_LEFT:
                        direction = direction.replace("L", "")

                    elif event.key == K_RIGHT:
                        direction = direction.replace("R", "")

            self.chunk_controller.update(direction)

            self.display.fill(constants.WHITE)

            self.chunk_controller.draw(self.display)

            self.sound_engine.play_sounds()

            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Main()
    game.run()

    pygame.quit()
    sys.exit(0)
