import pygame
from pygame.locals import *

from src.duel import duel_players
from src.etc import gui_components, constants

"""
dialogue.py

Handles interactions between characters.
"""


class DialogueController:

    def __init__(self, master):

        self.master = master

        self.scenes = {
            "test_scene": [
                            ("Wow I can speak!", 0),
                            ("Ayy me too!", 1),
                            ("That crazy man...", 0),
                            ("Sure is bruh", 1),
                            ("This is some really really long text just to test out having it over multiple lines", 0)
                          ]
        }

        self.background = pygame.image.load("src/resources/dialogue_background.png").convert()

        self.body_font = constants.load_font(20, False)

        self.player = None
        self.other_bean = None

        self.other_text_x = 197
        self.other_text_y = 48

        self.player_text_x = 429
        self.player_text_y = 392

        self.text_x = self.other_text_x
        self.text_y = self.other_text_y

        self.text_box_background = gui_components.Fill(self.text_x, self.text_y, 350, 262, constants.GUI_BACKING)
        self.text_box_fill = gui_components.Fill(self.text_x+10, self.text_y+10, 330, 242, constants.GUI_FILL)

        self.components = [
            self.text_box_background,
            self.text_box_fill
        ]

        self.text = [

        ]

        self.current_scene = []
        self.scene_progress = 0

        self.exit_func = None
        self.after_controller = -1

    def start_scene(self, entity1, entity2, scene, exit_func, after_controller):

        self.player = duel_players.DuelPlayer(entity1, "R")
        self.other_bean = duel_players.DuelPlayer(entity2, "L")

        self.current_scene = self.scenes[scene]
        self.scene_progress = 0

        self.text = [

        ]

        self.exit_func = exit_func
        self.after_controller = after_controller

        self.render_next()

    def reset(self):

        self.player = None
        self.other_bean = None

        self.current_scene = []
        self.scene_progress = 0

        self.text = [

        ]

        self.exit_func = None
        self.after_controller = -1

    def update(self):

        for event in pygame.event.get():

            if event.type == QUIT:
                self.master.game_exit = True

            if event.type == KEYUP:

                if event.key == K_SPACE:
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

        dialogue_in_words = current_dialogue.split(" ")

        sorted_lines = []

        n = len(dialogue_in_words)
        while n > 0:
            if self.body_font.size(" ".join(dialogue_in_words[0:n]))[0] < 310:
                
                sorted_lines.append(" ".join(dialogue_in_words[0:n]))
                dialogue_in_words = dialogue_in_words[n:len(dialogue_in_words)]

                n = len(dialogue_in_words)+1

            n -= 1

        self.text = [gui_components.Label(self.text_x+20, n*self.body_font.get_linesize()+self.text_y+49,
                                          sorted_lines[n], False, 20, constants.BLACK)
                     for n in range(len(sorted_lines))
                     ]

        self.scene_progress += 1
        
    def draw(self, display):

        display.blit(self.background, (0, 0))

        self.player.shadow.draw(display)
        self.other_bean.shadow.draw(display)

        display.blit(self.player.image, (75, 368))
        display.blit(self.other_bean.image, (640, 53))

        [component.draw(display) for component in self.components]
        [text.draw(display) for text in self.text]
