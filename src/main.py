import pygame
from pygame.locals import *

import sys

from src import constants, chunks, player

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

        self.chunk_controller = chunks.ChunkController()

        self.player_group = pygame.sprite.GroupSingle()
        self.player = player.Player()
        self.player_group.add(self.player)

    def run(self):

        game_exit = False
        moving = False
        direction = ""

        while not game_exit:

            for event in pygame.event.get():
                if event.type == QUIT:

                    game_exit = True

                elif event.type == KEYDOWN:

                    if not moving:
                        if event.key == K_UP:
                            direction = "U"
                            moving = True

                        elif event.key == K_DOWN:
                            direction = "D"
                            moving = True

                        elif event.key == K_LEFT:
                            direction = "L"
                            moving = True

                        elif event.key == K_RIGHT:
                            direction = "R"
                            moving = True

            if moving:

                movement = constants.dir_to_movements[direction]

                self.chunk_controller.move_chunks(movement)

                moving = False
                direction = ""

            self.display.fill(constants.WHITE)

            self.chunk_controller.draw_chunk("0000", self.display)
            self.player_group.draw(self.display)

            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Main()
    game.run()

    pygame.quit()
    sys.exit(0)
