import pygame
from pygame.locals import *

from src.etc import gui_components, constants
from src.entities import icons
from src.menu import menu_image_loader
from src.hud import hud_image_loader

"""
hud_widgets.py

This file defines classes for various widgets
displayed in the heads-up display
"""


class HealthDisplay:

    def __init__(self, player, master, controller, x=0, y=0):

        self.player = player
        self.master = master
        self.controller = controller

        self.active_bean_stat = 0

        self.x = x
        self.y = y

        self.id = "health_display"

        self.background = gui_components.Fill(self.x, self.y, 200, 209, constants.GUI_BACKING)

        self.bean_stats = [gui_components.Fill(self.x+5, self.y+5+35*n, 190, 30, constants.GUI_FILL)
                           for n in range(len(self.player.beans))]
        self.health_bars = [gui_components.ProgressBar(self.x+9, self.y+27+36*n, 182, 5,
                                                       (constants.HEALTH_BAR_RED, constants.HEALTH_BAR_GREEN))
                            for n in range(len(self.player.beans))]
        self.bean_labels = [gui_components.Label(self.x+9, self.y+3+40*n, "{}{} Bean".format(
            self.player.beans[n].bean[0].upper(), self.player.beans[n].bean[1:]),
                                                 False, 20, constants.BLACK)
                            for n in range(len(self.player.beans))]

        self.xp_bar = gui_components.ProgressBar(self.x+9, self.y+37+34*self.active_bean_stat, 182, 5,
                                                 (constants.XP_BAR_BLUE, constants.XP_BAR_CYAN))

        self.level_label = gui_components.Label(self.x, self.y+41+35*self.active_bean_stat, "Level {}".format(
            self.player.beans[self.active_bean_stat].meta.level), False, 20, constants.BLACK)

        self.components = [self.background] + self.bean_stats + self.health_bars + self.bean_labels +\
                          [self.xp_bar, self.level_label]

        self.update_required = True

    def update(self):

        for panel in self.bean_stats:
            if panel.rect.collidepoint(pygame.mouse.get_pos()):
                if not self.bean_stats.index(panel) == self.active_bean_stat:
                    self.active_bean_stat = self.bean_stats.index(panel)
                    self.update_required = True
                else:
                    self.update_required = False

        self.update_components()
        self.fix_positions()

    def update_components(self):

        bean_no = 0
        for bar in self.health_bars:
            bar.update(self.player.beans[bean_no].meta.hp/self.player.beans[bean_no].meta.max_hp)

            bean_no += 1

        self.xp_bar.update(
            self.player.beans[self.active_bean_stat].meta.xp/int((constants.level_up_base *
                                                                 (constants.level_up_multiplier **
                                                                  self.player.beans[self.active_bean_stat].meta.level)))
        )

        self.level_label.update("Level {}".format(self.player.beans[self.active_bean_stat].meta.level))

    def fix_positions(self):

        if self.update_required:
            panel_idx = 0
            for stat_panel in self.bean_stats:

                if panel_idx == self.active_bean_stat:
                    stat_panel.resize(stat_panel.rect.width, 60)

                else:
                    stat_panel.resize(stat_panel.rect.width, 30)
                if panel_idx == 0:
                    stat_panel.rect.top = self.x+5
                    self.health_bars[panel_idx].rect.top = self.x+27
                    self.bean_labels[panel_idx].rect.top = self.x+3
                else:
                    stat_panel.rect.top = self.bean_stats[panel_idx-1].rect.bottom + 5
                    self.health_bars[panel_idx].rect.top = self.bean_stats[panel_idx-1].rect.bottom + 27
                    self.bean_labels[panel_idx].rect.top = self.bean_stats[panel_idx - 1].rect.bottom + 3

                self.xp_bar.rect.top = self.y+34 + 35 * self.active_bean_stat

                self.level_label.rect.top = self.y+41 + 35 * self.active_bean_stat
                self.level_label.rect.right = self.background.rect.right - 7

                panel_idx += 1
            self.update_required = False

    def draw(self, display):

        [component.draw(display) for component in self.components]


class BeanSelectPopup:

    def __init__(self, player, master, controller, x, y):

        self.player = player
        self.master = master
        self.controller = controller

        self.x = x
        self.y = y

        self.id = "bean_select"

        self.selected_option = 0

        self.background = gui_components.Fill(self.x, self.y, 366, 176, constants.GUI_BACKING)
        self.background_fill = gui_components.Fill(self.x+5, self.y+5, 356, 166, constants.GUI_FILL)

        self.title = [
            gui_components.Label(self.x+9, self.y+3, "You have been challenged to fight!", False, 20, constants.BLACK),
            gui_components.Label(self.x+9, self.y+21, "Which bean accepts the challenge?", False, 20, constants.BLACK)
        ]

        self.options = [gui_components.Label(self.x+35, self.y+39+18*n, "{}{} Bean".format(
            self.player.beans[n].bean[0].upper(), self.player.beans[n].bean[1:]),
                                             False, 20, constants.BLACK) for n in range(len(self.player.beans))]
        self.options.append(gui_components.Label(self.x+35, self.y+39+18*len(self.options), "I decline the challenge",
                                                 False, 20, constants.BLACK))

        self.space_label = gui_components.Label(self.background.rect.centerx, self.y+159, "<Space to Select>",
                                                True, 20, (79, 80, 68))

        self.arrow = icons.ArrowPointer(self.x+23, self.y+44+18*self.selected_option)

        self.components = [
            self.background,
            self.background_fill,
            self.space_label,
            self.arrow
        ] + self.title + self.options

    def update(self):

        self.arrow.realign(self.x+23, self.y+44+18*self.selected_option)

    def set_position(self, x, y):

        self.x, self.y = x, y

    def handle_event(self, e):

        if e.type == KEYUP:

            if e.key in (K_UP, K_w):
                self.selected_option = (self.selected_option-1) % 6

            elif e.key in (K_DOWN, K_s):
                self.selected_option = (self.selected_option+1) % 6

            elif e.key == K_SPACE:

                if self.selected_option == 5:
                    self.master.hud.close_widget("bean_select")
                    self.master.enemy_to_duel = None

                    self.master.bean_select_popup_open = False
                else:
                    self.master.start_duel(self.selected_option)

    def draw(self, display):

        [component.draw(display) for component in self.components]


class SaveSelect:

    def __init__(self, master, controller, x, y):

        self.master = master
        self.controller = controller

        self.save_engine = self.master.master.save_engine

        self.x = x
        self.y = y

        self.id = "save_select"

        self.selected_save = 0

        self.images = menu_image_loader.load_images()

        self.saves = self.save_engine.saves

        self.background = gui_components.Fill(self.x, self.y, 482, 362, constants.GUI_BACKING)
        self.background_fill = gui_components.Fill(self.x+212, self.y+6, 264, 350, constants.GUI_FILL)

        self.save_labels = [gui_components.Label(self.x+235, self.y+2+(44*n), self.saves[n], False, 36, constants.BLACK)
                            for n in range(len(self.saves))]

        self.arrow = icons.ArrowPointer(self.x+222, self.y+18+(44*self.selected_save))

        self.new_save_button = gui_components.Button(self.images["new_save_button"], self.x+7, self.y+7,
                                                     lambda: self.callback(0))
        self.load_save_button = gui_components.Button(self.images["load_save_button"], self.x+7, self.y+95,
                                                      lambda: self.callback(1))
        self.delete_save_button = gui_components.Button(self.images["delete_save_button"], self.x+7, self.y+183,
                                                        lambda: self.callback(2))
        self.cancel_button = gui_components.Button(self.images["cancel_save_button"], self.x+7, self.y+271,
                                                   lambda: self.callback(3))

        self.buttons = [
            self.new_save_button,
            self.load_save_button,
            self.delete_save_button,
            self.cancel_button
        ]

        self.components = [
            self.background,
            self.background_fill,
            self.arrow
        ] + self.save_labels + self.buttons

    def update(self):

        self.arrow.realign(self.x+222, self.y+18+(44*self.selected_save))
        if not len(self.saves):
            self.arrow.off()
            self.load_save_button.set_off()
            self.delete_save_button.set_off()
        else:
            self.arrow.on()
            self.load_save_button.set_on()
            self.delete_save_button.set_on()

        if len(self.saves) >= 8:
            self.new_save_button.set_off()
        else:
            self.new_save_button.set_on()

        [button.update() for button in self.buttons]

    def handle_event(self, e):

        if e.type == KEYUP:

            if e.key in (K_UP, K_w):
                self.selected_save = (self.selected_save-1) % len(self.saves)

            elif e.key in (K_DOWN, K_s):
                self.selected_save = (self.selected_save+1) % len(self.saves)

    def callback(self, button_id):

        if button_id == 0:
            self.master.master.load_save("save{}".format(len(self.saves)+1))

        elif button_id == 1:
            self.master.master.load_save(self.saves[self.selected_save])

        elif button_id == 2:
            self.master.master.delete_save(self.saves[self.selected_save])
            self.refresh()

            if self.selected_save >= len(self.saves):
                self.selected_save -= 1

        elif button_id == 3:
            self.controller.close_widget(self.id)
            self.master.save_select_open = False

    def refresh(self):

        self.save_engine.refresh()
        self.saves = self.save_engine.saves

        self.save_labels = [gui_components.Label(self.x+235, self.y+2+(44*n), self.saves[n], False, 36, constants.BLACK)
                            for n in range(len(self.saves))]

        self.components = [
                              self.background,
                              self.background_fill,
                              self.arrow
                          ] + self.save_labels + self.buttons

    def draw(self, display):

        [component.draw(display) for component in self.components]


class Taskbar:

    def __init__(self, master, controller, x, y):

        self.master = master
        self.controller = controller

        self.x = x
        self.y = y

        self.id = "taskbar"

        self.inventory_button = gui_components.Button(hud_image_loader.load_images("inventory_button"),
                                                      self.x, self.y, lambda: self.callback(0))
        self.journal_button = gui_components.Button(hud_image_loader.load_images("journal_button"),
                                                    self.x, self.y+60, lambda: self.callback(1))
        self.map_button = gui_components.Button(hud_image_loader.load_images("map_button"),
                                                self.x, self.y+112, lambda: self.callback(2))

        self.components = [
            self.inventory_button,
            self.journal_button,
            self.map_button
        ]

    def callback(self, button_id):

        if button_id == 0:

            if not self.controller.has_component("inventory_display"):
                self.controller.open_widget("inventory_display")

    def update(self):

        [component.update() for component in self.components]

    def draw(self, display):

        [component.draw(display) for component in self.components]


class InventoryDisplay:

    def __init__(self, master, controller, x, y):

        self.master = master
        self.controller = controller

        self.x = x
        self.y = y

        self.id = "inventory_display"

        self.background = gui_components.Image("src/resources/tasks_backing", self.x, self.y)

        self.components = [
            self.background
        ]

    def draw(self, display):

        [component.draw(display) for component in self.components]
