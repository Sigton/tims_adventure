import pygame
from pygame.locals import *

import random

from src.duel import duel_players
from src.etc import gui_components, constants, story_data

"""
dialogue.py

Handles interactions between characters.
"""


class DialogueController:

    def __init__(self, master):

        self.master = master

        self.scenes = story_data.scenes

        self.scene_updates = {
            "old_man": self.update_fisherman,
            "fisherman2": self.update_duel_fisherman,
            "fisherman_duel1": self.update_duel_fisherman,
            "villager1": self.set_unimportant,
            "villager2": self.set_unimportant,
            "villager3": self.set_unimportant,
            "villager4": self.set_unimportant,
            "villager5": self.set_unimportant,
            "villager6": self.set_unimportant,
            "villager7": self.set_unimportant,
            "villager8": self.set_unimportant,
            "old_man2": self.update_north,
            "north_bean": self.update_village_attack,
            "help_village_bean": self.update_evil_beans_village,
            "dan": self.add_dan_to_team,
            "hermit": self.update_hermit,
            "lake_warning": self.update_lake_warning,
            "wizard": self.update_wizard
        }

        self.background = pygame.image.load("src/resources/dialogue_background.png").convert()

        self.body_font = constants.load_font(20, False)

        self.player = None
        self.other_bean = None

        self.player_ref = None
        self.other_bean_ref = None

        self.other_text_x = 197
        self.other_text_y = 48

        self.player_text_x = 429
        self.player_text_y = 392

        self.text_x = self.other_text_x
        self.text_y = self.other_text_y

        self.text_box_background = gui_components.Fill(self.text_x, self.text_y, 350, 262, constants.GUI_BACKING)
        self.text_box_fill = gui_components.Fill(self.text_x+10, self.text_y+10, 330, 242, constants.GUI_FILL)

        self.press_space = gui_components.Label(self.text_x+51, self.text_y+199, "Press Space to Continue",
                                                False, 20, constants.BLACK)
        self.press_left = gui_components.Label(self.text_x+63, self.text_y+223, "Left Arrow to go Back",
                                               False, 20, constants.BLACK)

        self.components = [
            self.text_box_background,
            self.text_box_fill,
            self.press_space,
            self.press_left
        ]

        self.text = [

        ]

        self.scene = ""
        self.current_scene = []
        self.scene_progress = 0

        self.exit_func = None
        self.after_controller = -1

        self.first = True

    def load_scenes(self, scenes):

        self.scenes = scenes

    def start_scene(self, entity1, entity2, scene, exit_func, after_controller):

        self.player = duel_players.DuelPlayer(entity1, "R")
        self.other_bean = duel_players.DuelPlayer(entity2, "L")

        self.player_ref = entity1
        self.other_bean_ref = entity2

        self.scene = scene
        self.current_scene = self.scenes[scene]
        self.scene_progress = 0

        self.text = [

        ]

        self.exit_func = exit_func
        self.after_controller = after_controller

        self.master.story_tracker.check_complete(['scene', scene])

        self.render_next()

    def reset(self):

        self.player = None
        self.other_bean = None

        self.player_ref = None
        self.other_bean_ref = None

        self.current_scene = []
        self.scene_progress = 0

        self.text = [

        ]

        self.exit_func = None
        self.after_controller = -1

        self.first = True

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

            if event.type == KEYUP:

                if event.key == K_SPACE:
                    if self.scene_progress >= len(self.current_scene)-1:
                        self.first = True
                        if self.scene in self.scene_updates:
                            self.scene_updates[self.scene]()
                        if self.exit_func is not None:
                            exec(self.exit_func)
                        self.master.switch_to(self.after_controller)
                    else:
                        self.scene_progress += 1
                        self.render_next()
                        self.master.sound_engine.queue_sound([random.choice(self.master.sound_engine.speech), 0])

                elif event.key == K_LEFT:
                    if not self.scene_progress == 0:
                        self.scene_progress -= 1
                        self.render_next()
                        self.master.sound_engine.queue_sound([random.choice(self.master.sound_engine.speech), 0])

        if self.first and not self.scene_progress >= len(self.current_scene)-1:
            self.master.sound_engine.queue_sound([random.choice(self.master.sound_engine.speech), 0])
            self.first = False

    def render_next(self):

        current_dialogue, speaker = self.current_scene[self.scene_progress]

        if speaker:
            self.text_x = self.other_text_x
            self.text_y = self.other_text_y
        else:
            self.text_x = self.player_text_x
            self.text_y = self.player_text_y

        self.text_box_background.rect.topleft = [self.text_x, self.text_y]
        self.text_box_fill.rect.topleft = [self.text_x+10, self.text_y+10]
        self.press_space.rect.topleft = [self.text_x+51, self.text_y+199]
        self.press_left.rect.topleft = [self.text_x+63, self.text_y+223]

        dialogue_in_words = current_dialogue.split(" ")

        sorted_lines = []

        n = len(dialogue_in_words)
        while n > 0:
            if self.body_font.size(" ".join(dialogue_in_words[0:n]))[0] < 310:

                sorted_lines.append(" ".join(dialogue_in_words[0:n]))
                dialogue_in_words = dialogue_in_words[n:len(dialogue_in_words)]

                n = len(dialogue_in_words)+1

            n -= 1

        bean = self.other_bean.meta.display_name if speaker else self.player.meta.display_name

        self.text = [gui_components.Label(self.text_x+20, n*self.body_font.get_linesize()+self.text_y+49,
                                          sorted_lines[n], False, 20, constants.BLACK)
                     for n in range(len(sorted_lines))
                     ] + [gui_components.Label(self.text_x+20, self.text_y+10,
                                               bean,
                                               False, 32, constants.BLACK)]

    def draw(self, display):

        display.blit(self.background, (0, 0))

        self.player.shadow.draw(display)
        self.other_bean.shadow.draw(display)

        display.blit(self.player.image, (75, 368))
        display.blit(self.other_bean.image, (640, 53))

        [component.draw(display) for component in self.components]
        [text.draw(display) for text in self.text]

        self.master.particle_engine.draw(display)

    def update_fisherman(self):

        e = self.master.chunk_controller.locate_entity(13)

        e.meta.interaction = \
            """self.master.dialogue_controller.start_scene(self.player.beans[0], self.enemy_to_duel, 'fisherman2', None,
0);self.master.switch_to(3)"""
        e.set_important()

        self.master.chunk_controller.locate_entity(14).meta.interaction = \
            """self.master.dialogue_controller.start_scene(self.player.beans[0], self.enemy_to_duel, 'fisherman_duel1', 
'self.master.duel_controller.begin_duel(self.player_ref, self.other_bean_ref)', 1);self.master.switch_to(3)"""

        self.set_unimportant()

    def update_duel_fisherman(self):

        self.master.chunk_controller.locate_entity(13).set_unimportant()
        self.master.chunk_controller.locate_entity(14).meta.interaction = \
            """self.master.dialogue_controller.start_scene(self.player.beans[0], self.enemy_to_duel, 'fisherman_duel2', 
'self.master.duel_controller.begin_duel(self.player_ref, self.other_bean_ref)', 1);self.master.switch_to(3)"""

        self.master.chunk_controller.locate_entity(14).set_important()

    def update_north(self):

        self.set_unimportant()
        e = self.master.chunk_controller.locate_entity(5)

        e.meta.interaction = \
            """self.master.dialogue_controller.start_scene(self.player.beans[0], self.enemy_to_duel, 'north_bean', None, 
0);self.master.switch_to(3)"""
        e.set_important()

    def update_village_attack(self):

        self.set_unimportant()
        e = self.master.chunk_controller.locate_entity(12)

        e.meta.interaction = \
            """self.master.dialogue_controller.start_scene(self.player.beans[0], self.enemy_to_duel,
'help_village_bean', None, 0);self.master.switch_to(3)"""
        e.set_important()

    def update_evil_beans_village(self):

        for n in range(6, 12):
            e = self.master.chunk_controller.locate_entity(n)
            e.set_important()
            e.meta.interaction = None

    def add_dan_to_team(self):

        self.master.chunk_controller.player.add_bean(self.master.chunk_controller.locate_entity(12).meta)
        self.master.chunk_controller.remove_stat_panel(self.master.chunk_controller.locate_entity(12))
        self.master.chunk_controller.delete_entity(12)

        e = self.master.chunk_controller.locate_entity(19)

        e.meta.interaction = \
            """self.master.dialogue_controller.start_scene(self.player.beans[0], self.enemy_to_duel,
'hermit', None, 0);self.master.switch_to(3)"""
        e.set_important()

    def update_hermit(self):

        e = self.master.chunk_controller.locate_entity(21)
        e.meta.interaction = \
            """self.master.dialogue_controller.start_scene(self.player.beans[0], self.enemy_to_duel,
'lake_warning', None, 0);self.master.switch_to(3)"""
        e.set_important()

        self.set_unimportant()

    def update_lake_warning(self):

        self.set_unimportant()

        for n in range(22, 26):
            e = self.master.chunk_controller.locate_entity(n)
            e.set_important()
            e.meta.interaction = None

    def update_wizard(self):

        e = self.master.chunk_controller.locate_entity(20)

        e.meta.level = 3
        self.master.chunk_controller.player.add_bean(e.meta)
        self.master.chunk_controller.remove_stat_panel(e)
        self.master.chunk_controller.delete_entity(20)

    def set_unimportant(self):

        self.other_bean_ref.set_unimportant()
