import math
import operator
import random

import pygame

from src.entities import shadows, bean_image_loader, entities
from src.etc import constants

"""
player.py

This is the player you see on screen.
"""


class Player(pygame.sprite.Sprite):

    chunk_controller = None

    def __init__(self, beans=None):

        pygame.sprite.Sprite.__init__(self)

        self.beans = [Bean(None, bean) for bean in beans]

        self.trail = [[0, 0],
                      [-1, 0],
                      [-2, 0],
                      [-3, 0],
                      [-4, 0]]

        self.move_history = ["R", "R", "R", "R", "R"]
        self.movement_intervals = [(0, 0), (0, 0), (0, 0), (0, 0)]

        n = 0
        head_bean = self.beans[0]
        for bean in self.beans:
            bean.rect.centerx = head_bean.rect.centerx + 48 * self.trail[n][0]
            n += 1

        self.drawn = False

    def load_player(self, trail, move_history):

        self.trail = trail
        self.move_history = move_history

    def update(self, direction):

        [self.beans[n].set_image(self.move_history[n]) for n in range(len(self.beans))]

        if self.chunk_controller.moving:

            n = 0
            for bean in self.beans:
                if not self.beans.index(bean) == 0:
                    bean.rect.x += self.movement_intervals[n][0]
                    bean.rect.y += self.movement_intervals[n][1]
                    n += 1

        [bean.update() for bean in self.beans]

    def create_movement_intervals(self):

        for n in range(len(self.movement_intervals)):
            current_move = self.move_history[0]
            old_move = self.move_history[n+1]

            new_movement = constants.dir_to_movements[current_move]
            old_movement = constants.dir_to_movements[old_move]

            new_movement = tuple(map(operator.sub, (0, 0), new_movement))
            old_movement = tuple(map(operator.sub, (0, 0), old_movement))

            movement = tuple(map(operator.sub, old_movement, new_movement))
            self.movement_intervals[n] = tuple(map(operator.floordiv, movement,
                                                   [constants.movement_speed for x in range(len(movement))]))

    def set_chunk_controller(self, ref):

        self.chunk_controller = ref
        for bean in self.beans:
            bean.chunk_controller = ref

    def add_bean(self):

        pass

    def remove_bean(self):

        pass

    def draw(self, display):

        [bean.draw(display) for bean in self.beans]


class Bean(pygame.sprite.Sprite):

    def __init__(self, bean=None, meta=None):

        pygame.sprite.Sprite.__init__(self)
        self.chunk_controller = None

        if meta is not None:
            self.bean = meta.bean
        else:
            self.bean = bean

        self.images = bean_image_loader.beans[self.bean]

        self.image = self.images["R"]

        self.rect = self.image.get_rect()
        self.rect.center = constants.DISPLAY_CENTER

        if self.bean in constants.bean_image_offset.keys():
            self.image_offset_x, self.image_offset_y = constants.bean_image_offset[self.bean]
        else:
            self.image_offset_x, self.image_offset_y = (0, 0)

        if meta is not None:
            self.meta = meta
            self.meta.images = self.images
        else:
            self.meta = entities.EntityMeta(self)

        self.shadow = shadows.Shadow(self)

        self.wobble_x = 0
        self.wobble_y = 0

    def update(self):

        self.wobble_x = math.cos((self.chunk_controller.world_offset_x-(self.rect.x*100))/10)*3
        self.wobble_y = math.sin((self.chunk_controller.world_offset_y-(self.rect.y*100))/10)*3

        self.shadow.update()

    def set_image(self, direction):

        if direction == "R":
            self.image = self.images["R"]
        elif direction == "L":
            self.image = self.images["L"]

    def create_images(self, main_image):

        self.images.clear()

        self.images["R"] = main_image
        self.images["L"] = pygame.transform.flip(main_image, True, False)

    def draw(self, display):

        self.shadow.draw(display)

        display.blit(self.image,
                     (self.rect.x + self.wobble_x - self.image_offset_x,
                      self.rect.y + self.wobble_y - self.image_offset_y))


def create_json_from_player(player):

    return {
        "bean": player.meta.bean,
        "max_hp": player.meta.max_hp,
        "moves": player.meta.moves,
        "attack": player.meta.attack,
        "energy": player.meta.energy,
        "hp": player.meta.hp,
        "xp": player.meta.xp,
        "level": player.meta.level,
        "interaction": player.meta.interaction,
        "important": player.meta.important
    }
