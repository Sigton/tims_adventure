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

        self.defined_components = {
            "health_display": self.health_display,
            "bean_select": self.bean_select
        }

        self.components = []

        self.hud_saves = {}
        self.hud_id = None

    def update(self):

        [component.update() for component in self.components]

    def load_saved_hud(self, hud_id):

        self.hud_id = hud_id
        self.components = self.hud_saves[self.hud_id]

    def open_widget(self, widget):

        self.components.append(widget)

    def close_widget(self, widget):

        self.components.remove(widget)

    def draw(self, display):

        [component.draw(display) for component in self.components]


