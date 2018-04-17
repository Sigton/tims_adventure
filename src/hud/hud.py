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

        self.health_display = lambda: hud_widgets.HealthDisplay(self.player, self.master, self, 0, 34)
        self.bean_select = lambda: hud_widgets.BeanSelectPopup(self.player, self.master, self, 297, 452)
        self.save_select = lambda: hud_widgets.SaveSelect(self.master, self, 238, 178)
        self.taskbar = lambda: hud_widgets.Taskbar(self.master, self, 900, 246)
        self.inventory_display = lambda: hud_widgets.InventoryDisplay(self.master, self, 237, 179)
        self.journal_display = lambda: hud_widgets.JournalDisplay(self.master, self, 237, 179)
        self.map_display = lambda: hud_widgets.MapDisplay(self.master, self, 237, 179)
        self.item_select = lambda: hud_widgets.ItemSelect(self.master, self, 237, 179)
        self.backing = lambda: hud_widgets.Backing(self.master, 0, 0)
        self.healing_display = lambda: hud_widgets.HealingDisplay(self.master, self, self.player, 237, 179)
        self.options_menu = lambda: hud_widgets.OptionsMenu(self.master, self, 350, 110)

        self.defined_components = {
            "health_display": self.health_display,
            "bean_select": self.bean_select,
            "save_select": self.save_select,
            "taskbar": self.taskbar,
            "inventory_display": self.inventory_display,
            "journal_display": self.journal_display,
            "map_display": self.map_display,
            "item_select": self.item_select,
            "backing": self.backing,
            "healing_display": self.healing_display,
            "options_menu": self.options_menu
        }

        self.components = []

        self.hud_saves = {}
        self.hud_id = None

    def update(self):

        [component.update() for component in self.components]

    def load_saved_hud(self, hud_id):

        self.hud_id = hud_id
        self.components = [component() for component in self.hud_saves[self.hud_id]]

    def save_hud(self, hud_id, components, current=False):

        if not current:
            self.hud_saves[hud_id] = [self.defined_components[component] for component in components]
        else:
            self.hud_saves[hud_id] = self.components

    def open_widget(self, widget):

        self.components.append(self.defined_components[widget]())

        if self.hud_id is not None:
            self.save_hud(self.hud_id, None, True)

    def close_widget(self, widget):

        self.components.remove([w for w in self.components if w.id == widget][0])

        if self.hud_id is not None:
            self.save_hud(self.hud_id, None, True)

    def close_hud(self):

        self.components = []
        self.hud_id = None

    def get_component(self, name):

        return [component for component in self.components if component.id == name][0]

    def has_component(self, name):

        return bool(len([component for component in self.components if component.id == name]))

    def draw(self, display):

        [component.draw(display) for component in self.components]

    def refresh(self):

        [component.refresh() for component in self.components]
