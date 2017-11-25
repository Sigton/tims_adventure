import pygame
from pygame.locals import *

from src.duel.duel_gui import load_images
from src.etc import gui_components

"""
duel.py

This deals with the game mechanics and GUI of duelling
"""


class DuelController:

    def __init__(self, master, player, enemy):

        self.master = master

        self.player = player.meta
        self.enemy = enemy.meta

        self.images = load_images()

        self.background = self.images["background"]

        self.attack_main_button = gui_components.Button(self.images["attack_main_button"], 508, 584)
        self.attack_alt_button = gui_components.Button(self.images["attack_alt_button"], 730, 584)
        self.item_button = gui_components.Button(self.images["item_button"], 508, 645)
        self.retreat_button = gui_components.Button(self.images["retreat_button"], 730, 645)

        self.buttons = [
            self.attack_main_button,
            self.attack_alt_button,
            self.item_button,
            self.retreat_button
        ]

    def update(self):

        for event in pygame.event.get():
            if event.type == QUIT:
                self.master.game_exit = True

        [button.update() for button in self.buttons]

    def draw(self, display):

        display.blit(self.background, (0, 0))

        [button.draw(display) for button in self.buttons]
