from src.etc import gui_components, constants

"""
hud.py

This file manages the
games heads-up display
"""


class HUD:

    def __init__(self):

        self.background = gui_components.Fill(0, 0, 200, 209, constants.GUI_BACKING)

        self.components = [self.background]

    def update(self):

        pass

    def draw(self, display):

        [component.draw(display) for component in self.components]
