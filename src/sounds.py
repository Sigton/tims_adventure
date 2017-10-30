import pygame

# This deals with the loading and playing of sounds.
# Each sound has it's own channel so that we don't
# run out of channels.


class SoundEngine:

    def __init__(self):

        # Create a channel for each sound
        self.ambient1_channel = pygame.mixer.Channel(0)

        # Load all the sounds
        self.ambient1_sound = pygame.mixer.Sound("src/resources/ambient1.mp3")
