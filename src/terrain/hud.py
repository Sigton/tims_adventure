from src.etc import gui_components, constants

"""
hud.py

This file manages the
games heads-up display
"""


class HUD:

    def __init__(self):

        self.background = gui_components.Fill(0, 0, 200, 209, constants.GUI_BACKING)
        self.bean_stats = [gui_components.Fill(5, 5+35*n, 190, 30, constants.GUI_FILL) for n in range(5)]

        self.components = [self.background] + self.bean_stats

        self.active_bean_stat = 0

    def update(self):

        if self.bean_stats[self.active_bean_stat].rect.height == 30:
            pass

    def draw(self, display):

        [component.draw(display) for component in self.components]
