import pygame

# This deals with the loading and playing of sounds.
# Each sound has it's own channel so that we don't
# run out of channels.


class SoundEngine:

    def __init__(self):

        # Create a channel for each sound
        self.ambient1_channel = pygame.mixer.Channel(0)

        # Load all the sounds
        self.ambient1_sound = pygame.mixer.Sound("src/resources/ambient1.ogg")

        # Link the sounds to the channels they should play in
        self.channel_linkup = {self.ambient1_sound: self.ambient1_channel}

        # This is all the sounds that need to be played
        self.queued_sounds = []

    def play_sounds(self):

        # Plays all the queued sounds
        [self.channel_linkup[sound[0]].play(sound[0], sound[1]) for sound in self.queued_sounds]

        # And empty the queue
        self.queued_sounds = []

    def queue_sound(self, sound):

        # Add a sound to the queue
        self.queued_sounds += [sound]
