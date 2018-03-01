"""
story_tracker.py

This file holds information about
the players current tasks and inventory
"""


class StoryTracker:

    def __init__(self):

        self.inventory = {}
        self.quests = {}

    def load_from_save(self, inventory, quests):

        self.inventory = inventory
        self.quests = quests
