import pygame
from pygame.constants import *

from src.etc import gui_components

"""
menu.py

This file loads and defines
the different components of the menu.
"""


class MainMenu:

    def __init__(self, master):

        self.master = master

        self.background = gui_components.Image("src/resources/title.png")

    def update(self):

        for event in pygame.event.get():

            if event.type == QUIT:
                self.master.game_exit = True

    def draw(self, display):

        self.background.draw(display)
