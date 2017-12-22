from src.etc import gui_components, constants

"""
hud.py

This file manages the
games heads-up display
"""


class HUD:

    def __init__(self, player):

        self.player = player

        self.background = gui_components.Fill(0, 0, 200, 209, constants.GUI_BACKING)

        self.bean_stats = [gui_components.Fill(5, 5+35*n, 190, 30, constants.GUI_FILL) for n in range(5)]
        self.health_bars = [gui_components.ProgressBar(9, 27+36*n, 182, 4,
                                                       (constants.HEALTH_BAR_RED, constants.HEALTH_BAR_GREEN))
                            for n in range(5)]

        self.components = [self.background] + self.bean_stats + self.health_bars

        self.active_bean_stat = 0

    def update(self):

        self.update_components()
        self.fix_positions()

    def update_components(self):

        for bar in self.health_bars:
            bar.update(0)

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
                stat_panel.rect.top = 5
                self.health_bars[panel_idx].rect.top = 27
            else:
                stat_panel.rect.top = self.bean_stats[panel_idx-1].rect.bottom + 5
                self.health_bars[panel_idx].rect.top = self.bean_stats[panel_idx-1].rect.bottom + 27

            panel_idx += 1

    def draw(self, display):

        [component.draw(display) for component in self.components]
