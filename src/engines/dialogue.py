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
            "fisherman_duel1": self.update_duel_fisherman2,
            "villager1": self.set_unimportant,
            "villager2": self.set_unimportant,
            "villager3": self.set_unimportant,
            "villager4": self.set_unimportant,
            "fisherman_duel2": self.update_old_man,
            "old_man2": self.update_north,
            "north_bean": self.set_unimportant
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

    def update(self):

        for event in pygame.event.get():

            if event.type == QUIT:
                self.master.close_save()

                self.master.game_exit = True

            if event.type == KEYUP:

                if event.key == K_SPACE:
                    if self.scene_progress >= len(self.current_scene)-1:
                        if self.scene in self.scene_updates:
                            self.scene_updates[self.scene]()
                        if self.exit_func is not None:
                            exec(self.exit_func)
                        self.master.switch_to(self.after_controller)
                    else:
                        self.scene_progress += 1
                        self.render_next()

                elif event.key == K_LEFT:
                    if not self.scene_progress == 0:
                        self.scene_progress -= 1
                        self.render_next()

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

        self.master.sound_engine.queue_sound([random.choice(self.master.sound_engine.speech), 0])

    def draw(self, display):

        display.blit(self.background, (0, 0))

        self.player.shadow.draw(display)
        self.other_bean.shadow.draw(display)

        display.blit(self.player.image, (75, 368))
        display.blit(self.other_bean.image, (640, 53))

        [component.draw(display) for component in self.components]
        [text.draw(display) for text in self.text]

    def update_fisherman(self):

        e = self.master.chunk_controller.locate_entity(13)\

        e.meta.interaction = \
            """self.master.dialogue_controller.start_scene(self.player.beans[0], self.enemy_to_duel, 'fisherman2', None,
0);self.master.switch_to(3)"""
        e.set_important()

        self.master.chunk_controller.locate_entity(14).meta.interaction = \
            """self.master.dialogue_controller.start_scene(self.player.beans[0], self.enemy_to_duel, 'fisherman_duel1', 
'self.master.duel_controller.begin_duel(self.player_ref, self.other_bean_ref)', 1);self.master.switch_to(3)"""

        self.set_unimportant()

    def update_duel_fisherman(self):

        self.master.chunk_controller.locate_entity(14).meta.interaction = \
            """self.master.dialogue_controller.start_scene(self.player.beans[0], self.enemy_to_duel, 'fisherman_duel2', 
'self.master.duel_controller.begin_duel(self.player_ref, self.other_bean_ref)', 1);self.master.switch_to(3)"""

        self.master.chunk_controller.locate_entity(14).set_important()
        self.set_unimportant()

    def update_old_man(self):

        e = self.master.chunk_controller.locate_entity(3)\

        e.meta.interaction = \
            """self.master.dialogue_controller.start_scene(self.player.beans[0], self.enemy_to_duel, 'old_man2', None, 0)
self.master.switch_to(3)"""
        e.set_important()

    def update_duel_fisherman2(self):

        self.update_duel_fisherman()
        self.update_old_man()

    def update_north(self):

        self.set_unimportant()
        e = self.master.chunk_controller.locate_entity(5)\

        e.meta.interaction = \
            """self.master.dialogue_controller.start_scene(self.player.beans[0], self.enemy_to_duel, 'north_bean', None, 
0);self.master.switch_to(3)"""
        e.set_important()

    def set_unimportant(self):

        self.other_bean_ref.set_unimportant()
