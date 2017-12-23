import pygame

from src.etc import gui_components, constants

"""
hud.py

This file manages the
games heads-up display
"""


class HUD:

    def __init__(self, player, x=0, y=0):

        self.player = player

        self.active_bean_stat = 0

        self.x = x
        self.y = y

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

    def update(self):

        for panel in self.bean_stats:
            if panel.rect.collidepoint(pygame.mouse.get_pos()):
                self.active_bean_stat = self.bean_stats.index(panel)

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

        panel_idx = 0
        for stat_panel in self.bean_stats:

            if panel_idx == self.active_bean_stat:
                if not stat_panel.rect.height == 60:
                    stat_panel.resize(stat_panel.rect.width, 60)

            else:
                if not stat_panel.rect.height == 30:
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

    def draw(self, display):

        [component.draw(display) for component in self.components]
