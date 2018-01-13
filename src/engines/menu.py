from src.etc import gui_components

"""
menu.py

This file loads and defines
the different components of the menu.
"""


class MainMenu:

    def __init__(self):

        self.background = gui_components.Image("src/resources/title.png")

    def update(self):

        pass

    def draw(self, display):

        self.background.draw(display)
