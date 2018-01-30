import pygame
from pygame.constants import *

from src.etc import constants, gui_components, tools
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

        dark_screen = gui_components.Fill(0, 0, 960, 720, constants.BLACK)
        dark_screen.image.set_alpha(200)

        self.dark_background = tools.combine_images([self.background] + self.buttons + [dark_screen])
        self.normal_background = self.background.image

        self.hud = hud.HUD(None, self)

        self.hud.save_hud("menu", ["save_select", ])
        self.hud.load_saved_hud("menu")

        self.save_select_open = False

    def update(self):

        for event in pygame.event.get():

            if event.type == QUIT:
                self.master.game_exit = True

            elif self.save_select_open:
                if not self.hud.has_component("save_select"):
                    self.hud.open_widget("save_select")

                self.hud.get_component("save_select").handle_event(event)

        if self.save_select_open:
            self.background.image = self.dark_background
        else:
            self.background.image = self.normal_background

        [button.update() for button in self.buttons]

        self.hud.update()

    def callback(self, button_id):

        if button_id == 0:
            self.save_select_open = True

        elif button_id == 1:
            pass

        else:
            self.master.game_exit = True

    def draw(self, display):

        self.background.draw(display)

        if self.save_select_open:
            self.hud.draw(display)
        else:
            [button.draw(display) for button in self.buttons]
