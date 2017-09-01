import pygame

import math
import operator

from src import constants, bean_image_loader

"""
player.py

This is the player you see on screen.
"""


class Player(pygame.sprite.Sprite):

    chunk_controller = None

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.beans = [Bean(True)] + [Bean(False) for n in range(4)]

        self.trail = [[0, 0],
                      [-1, 0],
                      [-2, 0],
                      [-3, 0],
                      [-4, 0]]

        self.move_history = ["R", "R", "R", "R", "R"]
        self.movement_intervals = [(0, 0), (0, 0), (0, 0), (0, 0)]

    def update(self, direction):

        [bean.set_image(direction) for bean in self.beans]

        if self.chunk_controller.moving:
            n = 0
            for bean in self.beans:
                if not bean.large:
                    move_x = self.movement_intervals[n-1][0]
                    move_y = self.movement_intervals[n-1][1]
                    if abs(self.trail[n][0] + move_x) // 48 > constants.max_trail_offset[n-1]:
                        move_x = 0
                    if abs(self.trail[n][1] + move_y) // 48 > constants.max_trail_offset[n-1]:
                        move_y = 0
                    bean.rect.x += move_x
                    bean.rect.y += move_y

                n += 1

        n = 0
        head_bean = self.beans[0]
        for bean in self.beans:
            bean.rect.centerx = head_bean.rect.centerx + 30*self.trail[n][0]
            n += 1

    def draw(self, display):

        for bean in self.beans:
            wobble_x = math.cos((((self.chunk_controller.world_offset_y + (bean.rect.x % 13)) % 48) + 180) * 2) * 4
            wobble_y = math.sin(((self.chunk_controller.world_offset_x - 24 + (bean.rect.x % 13)) % 48) * 2) * 4
            display.blit(bean.image,
                         (bean.rect.x+(wobble_x if bean.large else wobble_x/2),
                          bean.rect.y+(wobble_y if bean.large else wobble_y/2)))

    def create_movement_intervals(self):

        n = 0
        for direction in self.move_history[-4:]:
            if direction is not "":
                if len(direction) == 1:
                    movement = constants.dir_to_movements[direction]
                else:
                    movements = [constants.dir_to_movements[d] for d in list(direction)]
                    movement = tuple(map(operator.add, movements[0], movements[1]))
                self.movement_intervals[n] = tuple(map(operator.floordiv,
                                                       movement,
                                                       [-constants.movement_speed for x in range(len(movement))]))
            n += 1


class Bean(pygame.sprite.Sprite):

    def __init__(self, large):

        pygame.sprite.Sprite.__init__(self)

        self.large = large

        self.images = {}

        self.create_images(bean_image_loader.pink())

        self.image = self.images["R"] if self.large else self.images["SR"]

        self.rect = self.image.get_rect()
        self.rect.center = constants.DISPLAY_CENTER

        if not self.large:
            self.rect.y += 8

    def set_image(self, direction):

        if direction in ("R", "RU", "UR", "RD", "DR"):
            self.image = self.images["R"] if self.large else self.images["SR"]
        elif direction in ("L", "LD", "DL", "LU", "UL"):
            self.image = self.images["L"] if self.large else self.images["SL"]

    def create_images(self, main_image):

        self.images.clear()

        self.images["R"] = main_image
        self.images["L"] = pygame.transform.flip(main_image, True, False)
        self.images["SR"] = pygame.transform.scale(main_image, (20, 20))
        self.images["SL"] = pygame.transform.flip(self.images["SR"], True, False)
