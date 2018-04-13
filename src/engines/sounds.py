import pygame

from src.etc import constants

# This deals with the loading and playing of sounds.
# Each sound has it's own channel so that we don't
# run out of channels.


class SoundEngine:

    def __init__(self):

        # Create a channel for each sound (and a dedicated music channel)
        self.music_channel = pygame.mixer.Channel(0)
        self.punch_channel = pygame.mixer.Channel(1)
        self.burn_channel = pygame.mixer.Channel(2)
        self.footstep_channel = pygame.mixer.Channel(3)
        self.footstep2_channel = pygame.mixer.Channel(4)
        self.footstep3_channel = pygame.mixer.Channel(5)
        self.footstep4_channel = pygame.mixer.Channel(6)
        self.drinking_channel = pygame.mixer.Channel(7)
        self.click_channel = pygame.mixer.Channel(8)

        # Load all the sounds
        self.music1 = pygame.mixer.Sound("src/resources/ambient1.ogg")
        self.music2 = pygame.mixer.Sound("src/resources/ambient2.ogg")
        self.music3 = pygame.mixer.Sound("src/resources/ambient3.ogg")
        self.music4 = pygame.mixer.Sound("src/resources/ambient4.ogg")
        self.punch = pygame.mixer.Sound("src/resources/punch.ogg")
        self.burn = pygame.mixer.Sound("src/resources/burn.ogg")
        self.footstep = pygame.mixer.Sound("src/resources/footstep.ogg")
        self.footstep2 = pygame.mixer.Sound("src/resources/footstep2.ogg")
        self.footstep3 = pygame.mixer.Sound("src/resources/footstep3.ogg")
        self.footstep4 = pygame.mixer.Sound("src/resources/footstep4.ogg")
        self.drinking = pygame.mixer.Sound("src/resources/drinking.ogg")
        self.click = pygame.mixer.Sound("src/resources/click.ogg")

        self.music = ["music2",
                      "music3",
                      "music4"]

        # Link the sounds to the channels they should play in
        self.channel_linkup = {"music1": self.music_channel,
                               "music2": self.music_channel,
                               "music3": self.music_channel,
                               "music4": self.music_channel,
                               "punch": self.punch_channel,
                               "burn": self.burn_channel,
                               "footstep": self.footstep_channel,
                               "footstep2": self.footstep2_channel,
                               "footstep3": self.footstep3_channel,
                               "footstep4": self.footstep4_channel,
                               "drinking": self.drinking_channel,
                               "click": self.click_channel}

        self.sound_linkup = {"music1": self.music1,
                             "music2": self.music2,
                             "music3": self.music3,
                             "music4": self.music4,
                             "punch": self.punch,
                             "burn": self.burn,
                             "footstep": self.footstep,
                             "footstep2": self.footstep2,
                             "footstep3": self.footstep3,
                             "footstep4": self.footstep4,
                             "drinking": self.drinking,
                             "click": self.click}

        # This is all the sounds that need to be played
        self.queued_sounds = []

        # When the music channel stops playing it should que another sound to be played
        self.music_channel.set_endevent(constants.MUSIC_END_EVENT)

        # Mix the volumes
        [self.sound_linkup[m].set_volume(0.7) for m in self.music]
        self.punch.set_volume(0.1)
        self.burn.set_volume(0.1)
        self.footstep.set_volume(0.5)
        self.footstep2.set_volume(0.2)
        self.footstep3.set_volume(0.5)
        self.footstep4.set_volume(0.23)
        self.drinking.set_volume(0.4)
        self.click.set_volume(0.3)

    def play_sounds(self):

        # Plays all the queued sounds
        [self.channel_linkup[sound[0]].play(self.sound_linkup[sound[0]], sound[1]) for sound in self.queued_sounds]

        # And empty the queue
        self.queued_sounds = []

    def queue_sound(self, sound):

        # Add a sound to the queue
        self.queued_sounds += [sound]

    def stop_sound(self, sound):

        self.channel_linkup[sound].stop()

    def playing_sound(self, sound):

        return self.channel_linkup[sound].get_busy()
