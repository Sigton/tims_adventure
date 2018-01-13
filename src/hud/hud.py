from src.hud import hud_widgets

"""
hud.py

This file manages the
games heads-up display
"""


class HUD:

    def __init__(self, player, master):

        self.player = player
        self.master = master

        self.health_display = hud_widgets.HealthDisplay(self.player, self.master)
        self.bean_select = hud_widgets.BeanSelectPopup(self.player, self.master, 297, 452)

        self.components = []

        self.hud_saves = {}
        self.hud_id = None

    def update(self):

        [component.update() for component in self.components]

    def open_widget(self, widget):

        self.components.append(widget)

    def close_widget(self, widget):

        self.components.remove(widget)

    def draw(self, display):

        [component.draw(display) for component in self.components]


