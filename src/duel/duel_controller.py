from src.duel.duel_gui import load_images

"""
duel.py

This deals with the game mechanics and GUI of duelling
"""


class DuelController:

    def __init__(self):

        self.images = load_images()

        self.background = self.images["background"]

    def update(self):

        pass

    def draw(self, display):

        display.blit(self.background, (0, 0))
