import pygame
from pygame.constants import *

from src.etc import gui_components
from src.menu import menu_image_loader

"""
menu.py

This file loads and defines
the different components of the menu.
"""


class MainMenu:

    def __init__(self, master):

        self.master = master

        self.images = menu_image_loader.load_images()

        self.background = gui_components.Image("src/resources/title.png")

        self.play_button = gui_components.Button(self.images["play_button"], 11, 25, None)
        self.options_button = gui_components.Button(self.images["option_button"], 11, 136, None)
        self.quit_button = gui_components.Button(self.images["quit_button"], 11, 249, None)

        self.buttons = [
            self.play_button,
            self.options_button,
            self.quit_button
        ]

    def update(self):

        for event in pygame.event.get():

            if event.type == QUIT:
                self.master.game_exit = True

        [button.update() for button in self.buttons]

    def draw(self, display):

        self.background.draw(display)

        [button.draw(display) for button in self.buttons]
