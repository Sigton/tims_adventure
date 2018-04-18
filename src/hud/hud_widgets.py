import pygame
from pygame.locals import *

from src.etc import gui_components, constants
from src.entities import icons, entity_meta
from src.menu import menu_image_loader
from src.hud import hud_image_loader
from src.etc import tools

"""
hud_widgets.py

This file defines classes for various widgets
displayed in the heads-up display
"""


class Backing:

    def __init__(self, master, x, y):

        self.master = master

        self.x = x
        self.y = y

        self.id = "backing"

        self.background = gui_components.Fill(self.x, self.y, 200, 277, constants.GUI_BACKING)
        self.my_beans = gui_components.Label(self.x+5, self.y, "My Beans", False, 30, constants.WHITE)
        self.other_beans = gui_components.Label(self.x+5, self.y+239, "Other Beans", False, 30, constants.WHITE)
        self.open_hud_button = gui_components.Button(hud_image_loader.load_images("open_hud_button"),
                                                     self.x, self.y+225, lambda: self.callback(0))

        self.close_hud_button = gui_components.Button(hud_image_loader.load_images("close_hud_button"),
                                                      self.x+200, self.y+225, lambda: self.callback(1))
        self.compass = gui_components.Image(hud_image_loader.load_images("compass")[0], 802, 10, False)

        self.open_components = [
            self.my_beans,
            self.other_beans,
            self.close_hud_button,
            self.compass
        ]

        self.close_components = [
            self.open_hud_button,
            self.compass
        ]

        self.components = self.open_components

        self.hud_open = True

    def callback(self, button_id):

        self.master.master.sound_engine.queue_sound(["click", 0])

        if button_id == 0:
            self.components = self.open_components
            self.hud_open = True
        else:
            self.components = self.close_components
            self.hud_open = False
            self.open_hud_button.rect.centery = (self.background.rect.height // 2) + self.y

    def update(self):

        if self.hud_open:
            self.close_hud_button.update()
            self.close_hud_button.rect.centery = (self.background.rect.height//2)+self.y
        else:
            self.open_hud_button.update()

    def draw(self, display):

        if self.hud_open:
            tools.blit_alpha(display, self.background.image, self.background.rect.topleft, 128)

        [component.draw(display) for component in self.components]

    def resize(self, num_beans):

        self.background.resize(200, 277+(num_beans*65))


class HealthDisplay:

    def __init__(self, player, master, controller, x, y):

        self.player = player
        self.master = master
        self.controller = controller

        self.active_bean_stat = 0

        self.x = x
        self.y = y

        self.id = "health_display"

        self.bean_stats = [gui_components.Fill(self.x+5, self.y+5+35*n, 190, 30, constants.GUI_FILL)
                           for n in range(len(self.player.beans))]
        self.health_bars = [gui_components.ProgressBar(self.x+9, self.y+27+36*n, 182, 5,
                                                       (constants.HEALTH_BAR_RED, constants.HEALTH_BAR_GREEN))
                            for n in range(len(self.player.beans))]
        self.bean_labels = [gui_components.Label(self.x+9, self.y+3+40*n, self.player.beans[n].meta.display_name,
                                                 False, 20, constants.BLACK)
                            for n in range(len(self.player.beans))]

        self.xp_bar = gui_components.ProgressBar(self.x+9, self.y+37+34*self.active_bean_stat, 182, 5,
                                                 (constants.XP_BAR_BLUE, constants.XP_BAR_CYAN))

        self.level_label = gui_components.Label(self.x, self.y+41+35*self.active_bean_stat, "Level {}".format(
            self.player.beans[self.active_bean_stat].meta.level), False, 20, constants.BLACK)

        self.components = self.bean_stats + self.health_bars + self.bean_labels + [self.xp_bar, self.level_label]

        self.update_required = True

    def update(self):

        if self.controller.get_component("backing").hud_open:
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
                    stat_panel.rect.top = self.y+5
                    self.health_bars[panel_idx].rect.top = self.y+27
                    self.bean_labels[panel_idx].rect.top = self.y+3
                else:
                    stat_panel.rect.top = self.bean_stats[panel_idx-1].rect.bottom + 5
                    self.health_bars[panel_idx].rect.top = self.bean_stats[panel_idx-1].rect.bottom + 27
                    self.bean_labels[panel_idx].rect.top = self.bean_stats[panel_idx - 1].rect.bottom + 3

                self.xp_bar.rect.top = self.y+34 + 35 * self.active_bean_stat

                self.level_label.rect.top = self.y+41 + 35 * self.active_bean_stat
                self.level_label.rect.right = self.x + 193

                panel_idx += 1
            self.update_required = False

    def refresh(self):

        self.active_bean_stat = 0

        self.bean_stats = [gui_components.Fill(self.x + 5, self.y + 5 + 35 * n, 190, 30, constants.GUI_FILL)
                           for n in range(len(self.player.beans))]
        self.health_bars = [gui_components.ProgressBar(self.x + 9, self.y + 27 + 36 * n, 182, 5,
                                                       (constants.HEALTH_BAR_RED, constants.HEALTH_BAR_GREEN))
                            for n in range(len(self.player.beans))]
        self.bean_labels = [
            gui_components.Label(self.x + 9, self.y + 3 + 40 * n, self.player.beans[n].meta.display_name,
                                 False, 20, constants.BLACK)
            for n in range(len(self.player.beans))]

        self.xp_bar = gui_components.ProgressBar(self.x + 9, self.y + 37 + 34 * self.active_bean_stat, 182, 5,
                                                 (constants.XP_BAR_BLUE, constants.XP_BAR_CYAN))

        self.level_label = gui_components.Label(self.x, self.y + 41 + 35 * self.active_bean_stat, "Level {}".format(
            self.player.beans[self.active_bean_stat].meta.level), False, 20, constants.BLACK)

        self.components = self.bean_stats + self.health_bars + self.bean_labels + [self.xp_bar, self.level_label]

        self.update_required = True

    def draw(self, display):

        if self.controller.get_component("backing").hud_open:
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

        self.options = [gui_components.Label(self.x+35, self.y+39+18*n, self.player.beans[n].meta.display_name,
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
                self.selected_option = (self.selected_option-1) % (len(self.master.player.beans)+1)

            elif e.key in (K_DOWN, K_s):
                self.selected_option = (self.selected_option+1) % (len(self.master.player.beans)+1)

            elif e.key == K_SPACE:

                if self.selected_option == len(self.master.player.beans):
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

        if not self.master.can_click:
            return

        self.master.master.sound_engine.queue_sound(["click", 0])

        if button_id == 0:
            self.master.master.load_save("save{}".format(len(self.saves)+1))

        elif button_id == 1:
            self.master.master.load_save(self.saves[self.selected_save])

        elif button_id == 2:
            self.master.master.delete_save(self.saves[self.selected_save])
            self.refresh()

            if self.selected_save >= len(self.saves):
                self.selected_save = len(self.saves)-1

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
        self.health_button = gui_components.Button(hud_image_loader.load_images("health_button"),
                                                   self.x, self.y+168, lambda: self.callback(3))

        self.inventory_tooltip = gui_components.Tooltip("Inventory", 0, 0, 20, constants.BLACK, "L")
        self.journal_tooltip = gui_components.Tooltip("Journal", 0, 0, 20, constants.BLACK, "L")
        self.map_tooltip = gui_components.Tooltip("Map", 0, 0, 20, constants.BLACK, "L")
        self.health_tooltip = gui_components.Tooltip("Healing", 0, 0, 20, constants.BLACK, "L")

        self.exclamation = icons.ArrowIndicator(self.x-24, self.y+68)
        self.exclamation.off()

        self.buttons = [
            self.inventory_button,
            self.journal_button,
            self.map_button,
            self.health_button
        ]

        self.components = [
            self.inventory_button,
            self.journal_button,
            self.map_button,
            self.health_button,
            self.exclamation,
            self.inventory_tooltip,
            self.journal_tooltip,
            self.map_tooltip,
            self.health_tooltip
        ]

    def callback(self, button_id):

        self.master.master.sound_engine.queue_sound(["click", 0])

        if button_id == 0:
            current_display = "inventory_display"
            other_displays = ("journal_display", "map_display", "healing_display")
            current_button = self.inventory_button
        elif button_id == 1:
            current_display = "journal_display"
            other_displays = ("inventory_display", "map_display", "healing_display")
            current_button = self.journal_button
        elif button_id == 2:
            current_display = "map_display"
            other_displays = ("inventory_display", "journal_display", "healing_display")
            current_button = self.map_button
        else:
            current_display = "healing_display"
            other_displays = ("inventory_display", "journal_display", "map_display")
            current_button = self.health_button

        if self.controller.has_component(current_display):
            self.controller.close_widget(current_display)
            current_button.no_force_active()
        else:

            [button.no_force_active() for button in self.buttons]
            for display in other_displays:
                if self.controller.has_component(display):
                    self.controller.close_widget(display)

            self.controller.open_widget(current_display)
            current_button.force_active()

    def update(self):

        [component.update() for component in self.components]

        if self.inventory_button.active:
            self.inventory_tooltip.set_on()
            self.inventory_tooltip.reposition(pygame.mouse.get_pos())
        else:
            self.inventory_tooltip.set_off()

        if self.journal_button.active:
            self.journal_tooltip.set_on()
            self.journal_tooltip.reposition(pygame.mouse.get_pos())
        else:
            self.journal_tooltip.set_off()

        if self.map_button.active:
            self.map_tooltip.set_on()
            self.map_tooltip.reposition(pygame.mouse.get_pos())
        else:
            self.map_tooltip.set_off()

        if self.health_button.active:
            self.health_tooltip.set_on()
            self.health_tooltip.reposition(pygame.mouse.get_pos())
        else:
            self.health_tooltip.set_off()

        if self.master.master.story_tracker.to_see_quests():
            self.exclamation.on()
        else:
            self.exclamation.off()

    def draw(self, display):

        [component.draw(display) for component in self.components]


class TaskGUI:

    def __init__(self, master, controller, x, y, widget_id):

        self.master = master
        self.controller = controller

        self.x = x
        self.y = y

        self.id = widget_id

        self.background = gui_components.Image("src/resources/tasks_background.png", self.x, self.y)

        self.components = [
            self.background,
        ]

    def update(self):

        pass

    def draw(self, display):

        [component.draw(display) for component in self.components]


class InventoryDisplay(TaskGUI):

    def __init__(self, master, controller, x, y):

        TaskGUI.__init__(self, master, controller, x, y, "inventory_display")

        self.title = gui_components.Label(self.x+9, self.y, "Inventory", False, 32, constants.BLACK)

        self.items = list(self.master.master.story_tracker.inventory.items())
        self.labels = [gui_components.Label(self.x+45, self.y+(40*n)+44, "x{} Potion of {}".format(self.items[n][1][0],
                                                                                                   self.items[n][1][1]),
                                            False, 32, constants.BLACK)
                       for n in range(len(self.items))]
        image_data = lambda x: constants.item_images[self.items[x][0]]
        self.item_images = [gui_components.Image(icons.sprite_sheet.get_image(image_data(n)[0],
                                                                              image_data(n)[1],
                                                                              image_data(n)[2],
                                                                              image_data(n)[3]),
                                                 self.x+13, self.y+(40*n)+50, False)
                            for n in range(len(self.items))]

        self.components += [self.title] + self.labels + self.item_images


class JournalDisplay(TaskGUI):

    def __init__(self, master, controller, x, y):

        TaskGUI.__init__(self, master, controller, x, y, "journal_display")

        self.title = gui_components.Label(self.x+9, self.y, "Journal", False, 32, constants.BLACK)

        self.quests = list(self.master.master.story_tracker.quests.items())
        self.completed_quests = list(self.master.master.story_tracker.completed_quests.items())

        self.labels = [gui_components.Label(self.x+50, self.y+(40*(n+len(self.completed_quests)))+44, self.quests[n][1],
                                            False, 32, constants.BLACK)
                       for n in range(len(self.quests))]

        self.labels += [gui_components.Label(self.x+50, self.y+(40*n)+44, self.completed_quests[n][1],
                                             False, 32, constants.HEALTH_BAR_GREEN)
                        for n in range(len(self.completed_quests))]

        self.quests = self.completed_quests + self.quests

        image_data = lambda x: constants.quest_images[self.quests[x][0]]
        self.quest_images = [gui_components.Image(icons.sprite_sheet.get_image(image_data(n)[0],
                                                                               image_data(n)[1],
                                                                               image_data(n)[2],
                                                                               image_data(n)[3]),
                                                  self.x+13, self.y+(40*n)+50, False)
                             for n in range(len(self.quests))]

        self.components += [self.title] + self.labels + self.quest_images

        self.master.master.story_tracker.set_quests_seen()
        self.master.master.story_tracker.purge_completed()


class MapDisplay(TaskGUI):

    def __init__(self, master, controller, x, y):

        TaskGUI.__init__(self, master, controller, x, y, "map_display")

        self.title = gui_components.Label(self.x+9, self.y, "Map", False, 32, constants.BLACK)

        self.components.append(self.title)


class ItemSelect(InventoryDisplay):

    def __init__(self, master, controller, x, y):

        InventoryDisplay.__init__(self, master, controller, x, y)

        self.id = "item_select"

        self.selected_item = 0

        self.pointer = icons.ArrowPointer(self.x+10, self.y+59+(40*self.selected_item))

        self.title = gui_components.Label(self.x+9, self.y, "Item Select", False, 32, constants.BLACK)
        self.press_space = gui_components.Label(self.x+211, self.y, "<Space to Select>", False, 32, constants.BLACK)

        self.components = [
            self.background,
            self.title,
            self.press_space,
            self.pointer
        ] + self.labels + self.item_images

    def handle_event(self, e):

        if e.type == KEYUP:

            if e.key in (K_UP, K_w):
                self.selected_item = (self.selected_item-1) % len(self.items)

            elif e.key in (K_DOWN, K_s):
                self.selected_item = (self.selected_item+1) % len(self.items)

            elif e.key == K_SPACE:
                self.master.use_item(self.items[self.selected_item])

    def refresh(self):

        self.items = list(self.master.master.story_tracker.inventory.items())
        self.labels = [
            gui_components.Label(self.x + 45, self.y + (40 * n) + 44, "x{} Potion of {}".format(self.items[n][1][0],
                                                                                                self.items[n][1][1]),
                                 False, 32, constants.BLACK)
            for n in range(len(self.items))]
        image_data = lambda x: constants.item_images[self.items[x][0]]
        self.item_images = [gui_components.Image(icons.sprite_sheet.get_image(image_data(n)[0],
                                                                              image_data(n)[1],
                                                                              image_data(n)[2],
                                                                              image_data(n)[3]),
                                                 self.x + 13, self.y + (40 * n) + 50, False)
                            for n in range(len(self.items))]

        self.components = [
                              self.background,
                              self.title,
                              self.press_space,
                              self.pointer
                          ] + self.labels + self.item_images

    def update(self):

        self.pointer.realign(self.x+10, self.y+59+(40*self.selected_item))
        if len(self.items) == 0:
            self.pointer.off()
        else:
            self.pointer.on()

        if self.selected_item > len(self.items)-1:
            self.selected_item = len(self.items)-1


class EnemyStat:

    def __init__(self, entity, x, y):

        self.x = x
        self.y = y

        self.id = "enemy_stats"

        self.enemy_meta = entity.meta

        self.background = gui_components.Fill(self.x, self.y, 190, 60, constants.GUI_FILL)

        self.health_bar = gui_components.ProgressBar(self.x+4, self.y+24, 182, 5,
                                                     (constants.HEALTH_BAR_RED, constants.HEALTH_BAR_GREEN))
        self.xp_bar = gui_components.ProgressBar(self.x+4, self.y+32, 182, 5,
                                                 (constants.XP_BAR_BLUE, constants.XP_BAR_CYAN))
        self.bean_name = gui_components.Label(self.x+4, self.y-2, self.enemy_meta.display_name,
                                              False, 20, constants.BLACK)
        self.bean_level = gui_components.Label(self.x+152, self.y+36, "Level {}".format(self.enemy_meta.level),
                                               False, 20, constants.BLACK)
        self.bean_level.rect.topright = [self.x+188, self.y+36]

        self.components = [
            self.background,
            self.health_bar,
            self.xp_bar,
            self.bean_name,
            self.bean_level
        ]

        self.on = True

    def move(self, x, y):

        self.x = x
        self.y = y

        self.background.rect.topleft = [x, y]
        self.health_bar.rect.topleft = [x+4, y+22]
        self.xp_bar.rect.topleft = [x+4, y+30]
        self.bean_name.rect.topleft = [x+4, y-2]
        self.bean_level.rect.topright = [x+188, y+36]

    def update(self):

        if self.enemy_meta is not None:
            self.health_bar.update(round(self.enemy_meta.hp/self.enemy_meta.max_hp, 1))
            self.xp_bar.update(round(self.enemy_meta.xp/self.enemy_meta.get_level_up_threshold(), 1))

    def draw(self, display):

        if self.on:
            [component.draw(display) for component in self.components]

    def set_on(self):

        self.on = True

    def set_off(self):

        self.on = False


class HealingDisplay(ItemSelect):

    def __init__(self, master, controller, player, x, y):

        ItemSelect.__init__(self, master, controller, x, y)

        self.id = "healing_display"
        self.player_ref = player
        self.player = player.beans[self.controller.get_component("health_display").active_bean_stat]

        self.hint_arrow = gui_components.Label(self.x - 29, self.y - 138, "<-", False, 48, constants.BLACK)
        self.hint_text1 = gui_components.Label(self.x + 28, self.y - 150, "Hover over the Bean",
                                               False, 32, constants.BLACK)
        self.hint_text2 = gui_components.Label(self.x + 28, self.y - 111, "you want to heal!",
                                               False, 32, constants.BLACK)

        self.components += [self.hint_arrow,
                            self.hint_text1,
                            self.hint_text2]

        self.refresh()
        self.master.stop_moving()

    def refresh(self):

        self.items = [item for item in list(self.master.master.story_tracker.inventory.items())
                      if item[0] in constants.healing_items]

        self.labels = [
            gui_components.Label(self.x + 45, self.y + (40 * n) + 44, "x{} Potion of {}".format(self.items[n][1][0],
                                                                                                self.items[n][1][1]),
                                 False, 32, constants.BLACK)
            for n in range(len(self.items))]
        image_data = lambda x: constants.item_images[self.items[x][0]]
        self.item_images = [gui_components.Image(icons.sprite_sheet.get_image(image_data(n)[0],
                                                                              image_data(n)[1],
                                                                              image_data(n)[2],
                                                                              image_data(n)[3]),
                                                 self.x + 13, self.y + (40 * n) + 50, False)
                            for n in range(len(self.items))]

        self.components = [
                              self.background,
                              self.title,
                              self.press_space,
                              self.pointer
                          ] + self.labels + self.item_images

        if len(self.controller.player.beans) > 1:
            self.hint_arrow = gui_components.Label(self.x - 29, self.y - 138, "<-", False, 48, constants.BLACK)
            self.hint_text1 = gui_components.Label(self.x + 28, self.y - 150, "Hover over the Bean",
                                                   False, 32, constants.BLACK)
            self.hint_text2 = gui_components.Label(self.x + 28, self.y - 111, "you want to heal!",
                                                   False, 32, constants.BLACK)

            self.components += [self.hint_arrow,
                                self.hint_text1,
                                self.hint_text2]

    def handle_event(self, e):

        if not len(self.items):
            return

        if e.type == KEYUP:

            if e.key in (K_UP, K_w):
                self.selected_item = (self.selected_item - 1) % len(self.items)

            elif e.key in (K_DOWN, K_s):
                self.selected_item = (self.selected_item + 1) % len(self.items)

            elif e.key == K_SPACE:
                self.player = self.player_ref.beans[self.controller.get_component("health_display").active_bean_stat]
                self.master.master.story_tracker.use_item(self.items[self.selected_item][0], 1)
                exec(entity_meta.item_effects[self.items[self.selected_item][0]])
                if self.items[self.selected_item][0] in constants.drinking_items:
                    self.master.master.sound_engine.queue_sound(["drinking", 0])
                self.refresh()

                self.master.master.particle_engine.create_particle_spread(
                    'pink_bubbles', 8, self.player.rect.centerx, self.player.rect.centery, 35, 1, 0, 30, 30
                )


class OptionsMenu:

    def __init__(self, master, controller, x, y):

        self.master = master
        self.controller = controller

        self.x = x
        self.y = y

        self.id = "options_menu"

        self.selected_button = 0

        self.images = menu_image_loader.load_images()

        self.background = gui_components.Fill(self.x, self.y, 260, 500, constants.GUI_BACKING)
        self.background_fill = gui_components.Fill(self.x+5, self.y+5, 250, 490, constants.GUI_FILL)

        self.smoothest_button = gui_components.Button(self.images["smoothest_button"], self.x+21, self.y + (97 * 0) + 10,
                                                      lambda: self.callback(0))
        self.smooth_button = gui_components.Button(self.images["smooth_button"], self.x + 21, self.y + (97 * 1) + 10,
                                                   lambda: self.callback(1))
        self.fast_button = gui_components.Button(self.images["fast_button"], self.x + 21, self.y + (97 * 2) + 10,
                                                 lambda: self.callback(2))
        self.fastest_button = gui_components.Button(self.images["fastest_button"], self.x + 21, self.y + (97 * 3) + 10,
                                                    lambda: self.callback(3))
        self.close_button = gui_components.Button(self.images["close_button"], self.x + 21, self.y + (97 * 4) + 10,
                                                   lambda: self.callback(4))

        self.buttons = [
            self.smoothest_button,
            self.smooth_button,
            self.fast_button,
            self.fastest_button,
            self.close_button
        ]

        self.components = [
            self.background,
            self.background_fill
        ] + self.buttons

    def update(self):

        n = 0
        for button in self.buttons:
            if self.selected_button == n:
                button.force_active()
            else:
                button.no_force_active()

            button.update()

            n += 1

    def callback(self, button_id):

        if not self.master.can_click:
            return

        self.master.master.sound_engine.queue_sound(["click", 0])

        if button_id < 4:

            if not button_id == self.selected_button:

                self.selected_button = button_id
                constants.load_performance_profile(button_id)

                self.master.master.chunk_controller.set_movement_speed(constants.movement_speed)

        else:

            self.controller.close_widget(self.id)
            self.master.options_menu_open = False

    def set_button(self):

        if constants.FPS == 60:
            self.selected_button = 0
        elif constants.FPS == 45:
            self.selected_button = 1
        elif constants.FPS == 30:
            self.selected_button = 2
        else:
            self.selected_button = 3

    def draw(self, display):

        [component.draw(display) for component in self.components]
