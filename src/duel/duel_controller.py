import pygame
from pygame.locals import *

from src.duel.duel_gui import load_images
from src.etc import gui_components, constants, story_data
from src.duel.duel_players import DuelPlayer
from src.duel.moves import moves
from src.engines import brain
from src.hud import hud
from src.entities import entity_meta

import math
import random

"""
duel.py

This deals with the game mechanics and GUI of duelling
"""


class DuelController:

    particle_engine = None
    controller = None

    def __init__(self, master):

        self.master = master

        self.brain = brain.Brain(12, 4)
        self.particle_engine = self.master.particle_engine

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

        self.player = None
        self.enemy = None

        self.player_hp_bar = gui_components.ProgressBar(563, 379, 282, 30, [constants.HEALTH_BAR_RED,
                                                                            constants.HEALTH_BAR_GREEN])
        self.enemy_hp_bar = gui_components.ProgressBar(81, 38, 282, 30, [constants.HEALTH_BAR_RED,
                                                                         constants.HEALTH_BAR_GREEN])

        self.player_xp_bar = gui_components.ProgressBar(563, 519, 282, 30, [constants.XP_BAR_BLUE,
                                                                            constants.XP_BAR_CYAN])
        self.enemy_xp_bar = gui_components.ProgressBar(81, 108, 282, 30, [constants.XP_BAR_BLUE,
                                                                          constants.XP_BAR_CYAN])

        self.player_energy_bar = gui_components.ProgressBar(563, 449, 282, 30, [constants.ENERGY_BAR_ORANGE,
                                                                                constants.ENERGY_BAR_YELLOW])

        self.progress_bars = [
            self.player_hp_bar,
            self.enemy_hp_bar,
            self.player_xp_bar,
            self.enemy_xp_bar,
            self.player_energy_bar
        ]

        self.player_hp_label = gui_components.Label(857, 359, "")
        self.enemy_hp_label = gui_components.Label(373, 18, "")

        self.player_xp_label = gui_components.Label(857, 500, "")
        self.enemy_xp_label = gui_components.Label(373, 89, "")
        self.player_energy_label = gui_components.Label(857, 429, "")

        self.player_level_label = gui_components.Label(649, 499, "")
        self.enemy_level_label = gui_components.Label(160, 88, "")

        self.attack_main_label = None
        self.attack_alt_label = None

        self.player_name_label = None
        self.enemy_name_label = None

        self.winner_label = None

        self.text = [
            self.player_hp_label,
            self.enemy_hp_label,
            self.player_xp_label,
            self.enemy_xp_label,
            self.player_energy_label,
            self.player_level_label,
            self.enemy_level_label
        ]

        self.turn = 0
        self.turn_cool_down = constants.turn_cool_down

        self.game_won = False
        self.game_won_counter = 0
        self.winner = ""
        self.shown_win = False
        self.retreat = False

        self.hud = hud.HUD(None, self)

        self.hud.save_hud("duel", ["item_select"])
        self.hud.load_saved_hud("duel")

        self.hud_open = False

    def reset(self):

        self.turn = 0
        self.turn_cool_down = constants.turn_cool_down

        self.game_won = False
        self.game_won_counter = 0
        self.winner = ""
        self.shown_win = False
        self.retreat = False

        try:
            self.text.remove(self.winner_label)
        except ValueError:
            pass

    def begin_duel(self, player, enemy):

        try:
            self.text.remove(self.attack_main_label)
            self.text.remove(self.attack_alt_label)

            self.text.remove(self.player_name_label)
            self.text.remove(self.enemy_name_label)
        except ValueError:
            pass

        self.player = DuelPlayer(player, "R")
        self.enemy = DuelPlayer(enemy, "L")

        self.attack_main_label = gui_components.Label(607, 603, moves[self.player.meta.moves[0]]["name"], True)
        self.attack_alt_label = gui_components.Label(831, 603, moves[self.player.meta.moves[1]]["name"], True)

        self.player_name_label = gui_components.Label(507, 312, "{} STATS".format(
            self.player.meta.display_name.upper()))
        self.enemy_name_label = gui_components.Label(28, 137, "{} STATS".format(
            self.enemy.meta.display_name.upper()))

        self.text.append(self.attack_main_label)
        self.text.append(self.attack_alt_label)

        self.text.append(self.player_name_label)
        self.text.append(self.enemy_name_label)

        self.reset()

    def update(self):

        for event in pygame.event.get():
            if event.type == QUIT:

                self.master.close_save()

                self.master.game_exit = True

            elif event.type == constants.MUSIC_START_EVENT:

                if not self.master.sound_engine.playing_sound("music"):

                    new_music = random.choice(self.master.sound_engine.music)

                    while new_music == self.master.last_song:
                        new_music = random.choice(self.master.sound_engine.music)

                    self.master.last_song = new_music

                    self.master.sound_engine.queue_sound((new_music, 0))

            elif event.type == KEYUP:

                if event.key == K_ESCAPE:
                    self.master.game_exit = True

                elif event.key == K_F11:
                    self.master.set_full_screen()

            if self.hud_open:
                self.hud.get_component("item_select").handle_event(event)

        if self.game_won:
            if self.game_won_counter > 0:
                self.game_won_counter -= 1
            else:
                if not self.shown_win:

                    self.shown_win = True
                    self.game_won_counter = 120

                    if not self.retreat:
                        self.winner_label = gui_components.Label(480, 280, "{} won!".format(self.winner),
                                                                 True, 72, constants.BLACK)
                    else:
                        if self.winner == "Player":
                            self.winner_label = gui_components.Label(480, 280, "The Opponent Retreated!",
                                                                     True, 72, constants.BLACK)
                        else:
                            self.winner_label = gui_components.Label(480, 280, "You Retreated!",
                                                                     True, 72, constants.BLACK)

                    self.text.append(self.winner_label)
                else:
                    self.master.switch_to(0)

        [button.set_on() for button in self.buttons]

        if self.hud_open:
            self.hud.update()

            self.attack_main_button.set_off()
            self.attack_alt_button.set_off()
            self.retreat_button.set_off()
        else:
            if self.player.energy - moves[self.player.meta.moves[0]]["energy"] < 0:
                self.attack_main_button.set_off()
            else:
                self.attack_main_button.set_on()
            if self.player.energy - moves[self.player.meta.moves[1]]["energy"] < 0:
                self.attack_alt_button.set_off()
            else:
                self.attack_alt_button.set_on()
            if not len(list(self.master.story_tracker.inventory.items())):
                self.item_button.set_off()
            else:
                self.item_button.set_on()

        [button.update(not self.turn and not self.turn_cool_down) for button in self.buttons]

        if self.turn_cool_down > 0:
            self.turn_cool_down -= 1

        if self.turn == 1 and not self.turn_cool_down and not self.game_won:

            possible_moves = [0, 1]

            if self.enemy.energy - moves[self.enemy.meta.moves[0]]["energy"] < 0:
                possible_moves.remove(0)
            if self.enemy.energy - moves[self.enemy.meta.moves[1]]["energy"] < 0:
                possible_moves.remove(1)

            if not len(possible_moves):
                self.end_duel("Player", True)
            else:

                move_no = random.choice([0, 1])

                self.player.meta.damage(self.enemy.meta.get_attack_damage(move_no))
                self.enemy.energy -= moves[self.enemy.meta.moves[move_no]]["energy"]

                if self.player.meta.hp <= 0:
                    self.player.meta.hp = 0

                    self.end_duel("Opponent", False)

                self.enemy.meta.xp_gain(moves[self.enemy.meta.moves[move_no]]["xp"])

                move = moves[self.enemy.meta.moves[move_no]]["effects"]

                if moves[self.enemy.meta.moves[move_no]]["name"] in constants.shake_moves:
                    move = move.format("-")
                elif moves[self.enemy.meta.moves[move_no]]["name"] in constants.positional_moves:
                    move = move.format(220, 520)
                elif moves[self.enemy.meta.moves[move_no]]["name"] in constants.both_moves:
                    move = move.format(750, 170, "-")
                exec(move)

                self.turn = 0
                self.turn_cool_down = constants.turn_cool_down

        self.shake_players()

        self.player.shadow.update()
        self.enemy.shadow.update()

        self.update_gui_components()

    def callback(self, button_id):

        if self.turn == 1 or self.turn_cool_down:
            return

        if self.game_won:
            return

        if button_id < 2:

            self.enemy.meta.damage(self.player.meta.get_attack_damage(button_id))
            self.player.energy -= moves[self.player.meta.moves[button_id]]["energy"]

            if self.enemy.meta.hp <= 0:
                self.enemy.meta.hp = 0

                self.end_duel("Player", False)

            self.player.meta.xp_gain(moves[self.player.meta.moves[button_id]]["xp"])

            move = moves[self.player.meta.moves[button_id]]["effects"]

            if moves[self.player.meta.moves[button_id]]["name"] in constants.shake_moves:
                move = move.format("")
            elif moves[self.player.meta.moves[button_id]]["name"] in constants.positional_moves:
                move = move.format(750, 170)
            elif moves[self.enemy.meta.moves[button_id]]["name"] in constants.both_moves:
                move = move.format(220, 520, "")
            exec(move)

        elif button_id == 3:

            self.end_duel("Opponent", True)
            self.master.sound_engine.queue_sound(["click", 0])

        if button_id == 2:
            self.master.sound_engine.queue_sound(["click", 0])

            if self.hud_open:
                self.hud_open = False
            else:
                self.hud_open = True
                self.hud.refresh()
        else:
            self.turn = 1
            self.turn_cool_down = constants.turn_cool_down

    def update_gui_components(self):

        self.player_hp_bar.update(self.player.meta.hp / self.player.meta.max_hp)
        self.player_xp_bar.update(round(self.player.meta.xp / self.player.meta.get_level_up_threshold(), 1))

        self.enemy_hp_bar.update(self.enemy.meta.hp / self.enemy.meta.max_hp)
        self.enemy_xp_bar.update(round(self.enemy.meta.xp / self.enemy.meta.get_level_up_threshold(), 1))

        self.player_energy_bar.update(self.player.energy / self.player.meta.energy)

        self.player_hp_label.update("{}%".format(int(self.player.meta.hp / self.player.meta.max_hp * 100)))
        self.enemy_hp_label.update("{}%".format(int(self.enemy.meta.hp / self.enemy.meta.max_hp * 100)))

        self.player_xp_label.update("{}%".format(int(self.player.meta.xp / self.player.meta.get_level_up_threshold()
                                                     * 100)))
        self.enemy_xp_label.update("{}%".format(int(self.enemy.meta.xp / self.enemy.meta.get_level_up_threshold()
                                                    * 100)))

        self.player_energy_label.update("{}%".format(int(self.player.energy / self.player.meta.energy * 100)))

        self.player_level_label.update("Level {}".format(self.player.meta.level))
        self.enemy_level_label.update("Level {}".format(self.enemy.meta.level))

    def draw(self, display):

        display.blit(self.background, (0, 0))

        self.player.shadow.draw(display)
        self.enemy.shadow.draw(display)

        display.blit(self.player.image, (self.player.rect.x, 368))
        display.blit(self.enemy.image, (self.enemy.rect.x, 53))

        [button.draw(display) for button in self.buttons]
        [bar.draw(display) for bar in self.progress_bars]
        [label.draw(display) for label in self.text]

        self.master.particle_engine.draw(display)

        if self.hud_open:
            self.hud.draw(display)

    def start_shake(self, duration, dx, w, direction):

        entity = self.player if direction > 0 else self.enemy

        entity.shake = duration
        entity.shake_distance = dx
        entity.shake_w = w
        entity.shake_timer = 0
        entity.shake_direction = direction

    def shake_players(self):

        for entity in (self.player, self.enemy):
            if entity.shake_timer < entity.shake:
                c = entity.shake_distance
                entity.rect.x += (c-(c/math.pow(entity.shake_w, 2))*math.pow(
                    entity.shake_timer, 2)) * entity.shake_direction
                entity.shake_timer += 1
            else:
                entity.rect.x = entity.default_x

    def end_duel(self, winner, retreat):

        self.game_won = True
        self.game_won_counter = 10

        self.winner = winner
        self.retreat = retreat

        entity = self.player if self.winner == "Player" else self.enemy

        if not retreat:
            entity.meta.xp_gain(entity.energy)

            if winner == "Player":

                self.enemy.meta.to_delete = True

        entity.energy = 0

        if winner == "Player":
            self.master.story_tracker.check_complete(['duel', str(self.enemy.meta.id)])

        self.enemy.terrain_entity.set_unimportant()

    def use_item(self, item):

        self.turn = 1
        self.turn_cool_down = constants.turn_cool_down
        self.hud_open = False

        exec(entity_meta.item_effects[item[0]])
        self.master.story_tracker.use_item(item[0], 1)
        if item[0] in constants.drinking_items:
            self.master.sound_engine.queue_sound(["drinking", 0])
        self.hud.refresh()

        if item[0] in constants.healing_items:
            self.particle_engine.create_particle_spread('pink_bubbles', 45, 220, 520, 150, 1, 0, 30, 30)
        elif item[0] in constants.damaging_items:
            self.particle_engine.create_particle_spread('blue_bubbles', 45, 750, 170, 150, 1, 0, 30, 30)

        if self.enemy.meta.hp <= 0:
            self.enemy.meta.hp = 0

            self.end_duel("Player", False)
