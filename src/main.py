import sys
import os
import random

import pygame

from src.engines import sounds, particles, save, dialogue, story_tracker
from src.menu import menu
from src.etc import constants, gui_components, tools
from src.terrain import chunks
from src.entities import bean_image_loader, icons
from src.duel import duel_controller
from src.hud import hud_image_loader

"""
main.py

This is where the magic happens.
"""


class Main:

    def __init__(self):

        # Initiate pygame
        pygame.mixer.pre_init(22050, -16, 1, 512)
        pygame.mixer.init()
        pygame.init()

        pygame.mixer.set_num_channels(16)

        # Create the display
        self.display = pygame.display.set_mode(constants.DISPLAY_SIZE)

        # Set the title on the window
        pygame.display.set_caption("Tim's Adventure")

        icon_img = pygame.image.load("src/resources/icon.png")

        icon = pygame.Surface([32, 32], flags=pygame.SRCALPHA)
        icon = icon.convert_alpha()
        icon.blit(icon_img, (0, 0))
        pygame.display.set_icon(icon)

        self.clock = pygame.time.Clock()

        self.load_components()
        constants.load_performance_profile(1)

        self.loading_screen = gui_components.Image(tools.combine_images((gui_components.Fill(0, 0, 960, 720,
                                                                                             constants.BLACK),
                                                                        gui_components.Label(340, 322, "Loading...",
                                                                                             False, 64))),
                                                   0, 0, False)

        self.loading_screen.draw(self.display)
        pygame.display.update()

        self.fade_screen = gui_components.Fade()
        self.fade_screen.set_opacity(0)

        self.sound_engine = sounds.SoundEngine()
        self.particle_engine = particles.ParticleEngine()
        self.save_engine = save.SaveEngine()
        self.story_tracker = story_tracker.StoryTracker(self)

        self.game_exit = False

        self.chunk_controller = chunks.ChunkController(self)
        self.duel_controller = duel_controller.DuelController(self)
        self.dialogue_controller = dialogue.DialogueController(self)

        self.menu = menu.MainMenu(self)

        self.show_loading = False

        self.game_mode = 2
        self.full_screen = False

        self.fade = 0
        self.new_game_mode = -1
        self.loading_screen_time = constants.LOADING_SCREEN_TIME

        self.controllers = [
            self.chunk_controller,
            self.duel_controller,
            self.menu,
            self.dialogue_controller
        ]

        self.load_function = None
        self.after_load = -1

        self.current_save = ""

        self.last_song = ""

    def load_components(self):

        constants.load_font()
        bean_image_loader.load_sprite_sheet()
        particles.load_sprite_sheet()
        icons.load_sprite_sheet()
        hud_image_loader.load_sprite_sheet()

    def set_full_screen(self):

        if not self.full_screen:
            self.display = pygame.display.set_mode(constants.DISPLAY_SIZE, pygame.FULLSCREEN)
            self.full_screen = True
        else:
            self.display = pygame.display.set_mode(constants.DISPLAY_SIZE)
            self.full_screen = False

    def run(self):

        music = random.choice(self.sound_engine.music)
        self.sound_engine.queue_sound([music, 0])
        self.last_song = music

        pygame.time.set_timer(constants.MUSIC_START_EVENT, 7000)

        self.fade = 0

        while not self.game_exit:

            if self.fade > 0:
                self.fade -= 1

                if self.fade == self.loading_screen_time//2 and self.new_game_mode >= 0:
                    self.switch_game_mode()

            else:

                if self.show_loading:

                    if self.load_function is not None:
                        self.load_function()

                        self.load_function = None

                    self.switch_to(self.after_load)
                    self.after_load = -1

                if self.fade_screen.opacity > 0:
                    self.fade_screen.set_opacity(0)

                self.controllers[self.game_mode].update()

            self.particle_engine.update()

            self.display.fill(constants.WHITE)

            self.controllers[self.game_mode].draw(self.display)

            if self.fade > self.loading_screen_time//2:
                self.fade_screen.set_opacity(int((((self.loading_screen_time//2) -
                                                   (self.fade-(self.loading_screen_time//2)))
                                                  / (self.loading_screen_time//2))*255))
            elif self.fade > 0:
                self.fade_screen.set_opacity(int((self.fade/(self.loading_screen_time//2))*255))

            if self.show_loading:
                self.loading_screen.draw(self.display)

            self.fade_screen.draw(self.display)

            self.sound_engine.play_sounds()

            pygame.display.update()
            self.clock.tick(constants.FPS)

    def switch_game_mode(self):

        if self.new_game_mode == -1:
            return

        if self.new_game_mode == 4:
            self.show_loading = True
            self.new_game_mode = -1

            return
        else:
            self.show_loading = False

        self.game_mode = self.new_game_mode
        self.new_game_mode = -1

        self.controllers[self.game_mode].update()

    def switch_to(self, game_mode, force_controller_change=True):

        if force_controller_change:
            self.new_game_mode = game_mode
        self.fade = self.loading_screen_time

    def load_save(self, save_dir):

        self.switch_to(4)

        if save_dir in self.save_engine.saves:
            self.load_function = lambda: self.chunk_controller.load_from_save(os.path.join(self.save_engine.save_dir,
                                                                                           save_dir))
        else:

            def load_function():
                self.save_engine.create_save(save_dir)
                self.chunk_controller.load_from_save(os.path.join(self.save_engine.save_dir, save_dir))
            self.load_function = load_function
        self.after_load = 0

        self.current_save = save_dir

    def exit_to_menu(self):

        self.switch_to(4)

        self.load_function = lambda: self.close_save()
        self.after_load = 2

    def delete_save(self, save_dir):

        self.save_engine.delete_save(save_dir)

    def update_save(self):

        save_data = self.chunk_controller.close_save()

        self.save_engine.dump_to_save(self.current_save, save_data)

    def close_save(self):

        self.update_save()
        self.current_save = ""
        if self.after_load == 2:
            self.menu.hud.get_component("save_select").refresh()
            self.menu.hud.update()


if __name__ == "__main__":
    game = Main()
    game.run()

    pygame.quit()
    sys.exit(0)
