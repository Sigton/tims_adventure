import pygame
from pygame.constants import *

from src.etc import gui_components
from src.menu import menu_image_loader
from src.hud import hud

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

        self.play_button = gui_components.Button(self.images["play_button"], 11, 25, lambda: self.callback(0))
        self.options_button = gui_components.Button(self.images["option_button"], 11, 136, lambda: self.callback(1))
        self.quit_button = gui_components.Button(self.images["quit_button"], 11, 249, lambda: self.callback(2))

        self.buttons = [
            self.play_button,
            self.options_button,
            self.quit_button
        ]

        self.hud = hud.HUD(None, self)

        self.hud.save_hud("menu", ["save_select", ])
        self.hud.load_saved_hud("menu")

    def update(self):

        for event in pygame.event.get():

            if event.type == QUIT:
                self.master.game_exit = True

            else:
                self.hud.get_component("save_select").handle_event(event)

        [button.update() for button in self.buttons]

        self.hud.update()

    def callback(self, button_id):

        if button_id == 0:
            self.master.switch_to(0)

        elif button_id == 1:
            pass

        else:
            self.master.game_exit = True

    def draw(self, display):

        self.background.draw(display)

        [button.draw(display) for button in self.buttons]

        self.hud.draw(display)
