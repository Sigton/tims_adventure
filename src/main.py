import pygame
from pygame.locals import *

import sys
import operator

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

        self.chunk_controller = chunks.ChunkController(960, 720)

        self.player_group = pygame.sprite.GroupSingle()
        self.player = player.Player()
        self.player_group.add(self.player)

    def run(self):

        game_exit = False

        direction = ""
        moving = 0
        movement_interval = (0, 0)

        while not game_exit:

            for event in pygame.event.get():
                if event.type == QUIT:

                    game_exit = True

                elif event.type == KEYDOWN:

                    if len(direction) < 2:
                        if event.key == K_UP and "U" not in direction:
                            direction += "U"

                        elif event.key == K_DOWN and "D" not in direction:
                            direction += "D"

                        elif event.key == K_LEFT and "L" not in direction:
                            direction += "L"

                        elif event.key == K_RIGHT and "R" not in direction:
                            direction += "R"

            if direction and moving == 0:

                # Make sure we're not at the edge
                if (self.chunk_controller.world_offset_x >= -24 and "L" in direction) or\
                        (self.chunk_controller.world_offset_y >= 0 and "U" in direction):
                    direction = ""
                    movement_interval = (0, 0)
                else:
                    moving = 8

                    if len(direction) > 1:
                        movements = [constants.dir_to_movements[d] for d in list(direction)]
                        movement = tuple(map(operator.add, movements[0], movements[1]))
                    else:
                        movement = constants.dir_to_movements[direction]
                    movement_interval = tuple(map(operator.floordiv, movement,
                                                  [moving for x in range(len(movement))]))

            if moving > 0:
                moving -= 1
                self.chunk_controller.move_chunks(movement_interval)

            if moving == 0 and direction:
                direction = ""
                movement_interval = (0, 0)

            self.chunk_controller.update()

            self.display.fill(constants.WHITE)

            self.chunk_controller.draw(self.display)
            self.player_group.draw(self.display)

            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Main()
    game.run()

    pygame.quit()
    sys.exit(0)
