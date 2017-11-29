import pygame
from pygame.locals import *

from src.duel.duel_gui import load_images
from src.etc import gui_components, constants
from src.entities import shadows

"""
duel.py

This deals with the game mechanics and GUI of duelling
"""


class DuelController:

    particle_engine = None

    def __init__(self, master, player, enemy):

        self.master = master

        self.player = player.meta
        self.enemy = enemy.meta

        self.images = load_images()

        self.background = self.images["background"]

        self.attack_main_button = gui_components.Button(self.images["attack_main_button"], 508, 584,
                                                        lambda: self.callback(0))
        self.attack_alt_button = gui_components.Button(self.images["attack_alt_button"], 730, 584,
                                                       lambda: self.callback(1))
        self.item_button = gui_components.Button(self.images["item_button"], 508, 645,
                                                 lambda: self.callback(2))
        self.retreat_button = gui_components.Button(self.images["retreat_button"], 730, 645,
                                                    lambda: self.callback(3))

        self.buttons = [
            self.attack_main_button,
            self.attack_alt_button,
            self.item_button,
            self.retreat_button
        ]

        self.player_image = pygame.transform.scale(self.player.images["R"], (300, 300))
        self.enemy_image = pygame.transform.scale(self.enemy.images["L"], (230, 230))

        class PlayerShadow:
            rect = self.player_image.get_rect()
            rect.topleft = (75, 368)
            tile_code = "duel_player"

        class EnemyShadow:
            rect = self.enemy_image.get_rect()
            rect.topleft = (640, 53)
            tile_code = "duel_enemy"

        self.player_shadow = shadows.Shadow(PlayerShadow())
        self.enemy_shadow = shadows.Shadow(EnemyShadow())

        self.player_hp_bar = gui_components.ProgressBar(563, 449, 232, 30, [constants.HEALTH_BAR_RED,
                                                                            constants.HEALTH_BAR_GREEN])
        self.enemy_hp_bar = gui_components.ProgressBar(81, 38, 232, 30, [constants.HEALTH_BAR_RED,
                                                                         constants.HEALTH_BAR_GREEN])

        self.player_xp_bar = gui_components.ProgressBar(563, 519, 232, 30, [constants.XP_BAR_BLUE,
                                                                            constants.XP_BAR_CYAN])
        self.enemy_xp_bar = gui_components.ProgressBar(81, 108, 232, 30, [constants.XP_BAR_BLUE,
                                                                          constants.XP_BAR_CYAN])

        self.progress_bars = [
            self.player_hp_bar,
            self.enemy_hp_bar,
            self.player_xp_bar,
            self.enemy_xp_bar
        ]

        self.player_hp_label = gui_components.Label(807, 429, "{}/{}".format(self.player.hp, self.player.max_hp))
        self.enemy_hp_label = gui_components.Label(323, 18, "{}/{}".format(self.enemy.hp, self.enemy.max_hp))

        self.player_xp_label = gui_components.Label(807, 500, "{}/{}".format(self.player.xp,
                                                                             int((constants.level_up_base *
                                                                                 (constants.level_up_multiplier **
                                                                                  self.player.level)))))
        self.enemy_xp_label = gui_components.Label(323, 89, "{}/{}".format(self.enemy.xp,
                                                                           int((constants.level_up_base *
                                                                               (constants.level_up_multiplier **
                                                                                self.enemy.level)))))

        self.player_level_label = gui_components.Label(624, 499, "Level {}".format(self.player.level))
        self.enemy_level_label = gui_components.Label(135, 88, "Level {}".format(self.enemy.level))

        self.text = [
            self.player_hp_label,
            self.enemy_hp_label,
            self.player_xp_label,
            self.enemy_xp_label,
            self.player_level_label,
            self.enemy_level_label
        ]

        self.turn = 0
        self.turn_cool_down = 50

    def update(self):

        for event in pygame.event.get():
            if event.type == QUIT:
                self.master.game_exit = True

        [button.update(not self.turn and not self.turn_cool_down) for button in self.buttons]

        if self.turn_cool_down > 0:
            self.turn_cool_down -= 1

        if self.turn == 1 and not self.turn_cool_down:
            self.player.hp -= self.enemy.attack
            if self.player.hp < 0:
                self.player.hp = 0

            self.turn = 0
            self.turn_cool_down = 50

        self.update_gui_components()

    def callback(self, button_id):

        if self.turn == 1 or self.turn_cool_down:
            return

        if button_id == 0:
            if self.player.moves[0] == 0:

                self.enemy.hp -= self.player.attack
                if self.enemy.hp < 0:
                    self.enemy.hp = 0

                self.turn = 1
                self.turn_cool_down = 50

                self.particle_engine.create_particle_spread("fire", 30, 750, 170, 120, 100, 30, 15, 20)

    def update_gui_components(self):

        self.player_hp_bar.update(self.player.hp / self.player.max_hp)
        self.player_xp_bar.update(self.player.xp / (constants.level_up_base *
                                                    (constants.level_up_multiplier ** self.player.level)))

        self.enemy_hp_bar.update(self.enemy.hp / self.enemy.max_hp)
        self.enemy_xp_bar.update(self.enemy.xp / (constants.level_up_base *
                                                  (constants.level_up_multiplier ** self.enemy.level)))

        self.player_hp_label.update("{}/{}".format(self.player.hp, self.player.max_hp))
        self.enemy_hp_label.update("{}/{}".format(self.enemy.hp, self.enemy.max_hp))

        self.player_xp_label.update("{}/{}".format(self.player.xp,
                                                   int((constants.level_up_base *
                                                        (constants.level_up_multiplier **
                                                         self.player.level)))))
        self.enemy_xp_label.update("{}/{}".format(self.enemy.xp,
                                                  int((constants.level_up_base *
                                                       (constants.level_up_multiplier **
                                                        self.enemy.level)))))
        self.player_level_label.update("Level {}".format(self.player.level))
        self.enemy_level_label.update("Level {}".format(self.enemy.level))

    def draw(self, display):

        display.blit(self.background, (0, 0))

        self.player_shadow.draw(display)
        self.enemy_shadow.draw(display)

        display.blit(self.player_image, (75, 368))
        display.blit(self.enemy_image, (640, 53))

        [button.draw(display) for button in self.buttons]
        [bar.draw(display) for bar in self.progress_bars]
        [label.draw(display) for label in self.text]
