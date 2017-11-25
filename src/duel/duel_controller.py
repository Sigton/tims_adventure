from src.duel.duel_gui import load_images
from src.etc import gui_components

"""
duel.py

This deals with the game mechanics and GUI of duelling
"""


class DuelController:

    def __init__(self):

        self.images = load_images()

        self.background = self.images["background"]

        self.attack_main_button = gui_components.Button(self.images["attack_main_button"], 0, 0)
        self.attack_alt_button = gui_components.Button(self.images["attack_alt_button"], 0, 50)
        self.item_button = gui_components.Button(self.images["item_button"], 0, 100)
        self.retreat_button = gui_components.Button(self.images["retreat_button"], 0, 150)

        self.buttons = [
            self.attack_main_button,
            self.attack_alt_button,
            self.item_button,
            self.retreat_button
        ]

    def update(self):

        pass

    def draw(self, display):

        display.blit(self.background, (0, 0))

        [button.draw(display) for button in self.buttons]
