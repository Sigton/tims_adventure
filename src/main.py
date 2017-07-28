import pygame
from pygame.locals import *


class Main:

    def __init__(self):

        pygame.mixer.pre_init(22050, -16, 1, 512)
        pygame.mixer.init()
        pygame.init()

if __name__ == "__main__":
    game = Main()
