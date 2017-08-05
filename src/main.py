import pygame
from pygame.locals import *

from src import constants


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

    def run(self):

        game_exit = False

        while not game_exit:

            for event in pygame.event.get():
                if event.type == QUIT:

                    game_exit = True

            self.display.fill(constants.WHITE)

            pygame.display.update()
            self.clock.tick()

if __name__ == "__main__":
    game = Main()
    game.run()
