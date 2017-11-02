import pygame

'''
shadows.py

This file defines the shadow class,
which is an on-screen shadow displayed
under some decorations and entities.
'''


class Shadow:

    def __init__(self, parent):

        # A shadow generates its size based
        # off of its parents dimensions.
        self.parent = parent
