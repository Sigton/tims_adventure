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
        self.speech_channel = pygame.mixer.Channel(9)
        self.pickup_channel = pygame.mixer.Channel(10)
        self.splat_channel = pygame.mixer.Channel(11)
        self.impact_channel = pygame.mixer.Channel(12)
        self.potion_fizz_channel = pygame.mixer.Channel(13)
        self.freeze_channel = pygame.mixer.Channel(14)

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
        self.speech1 = pygame.mixer.Sound("src/resources/speech1.ogg")
        self.speech2 = pygame.mixer.Sound("src/resources/speech2.ogg")
        self.speech3 = pygame.mixer.Sound("src/resources/speech3.ogg")
        self.speech4 = pygame.mixer.Sound("src/resources/speech4.ogg")
        self.pickup = pygame.mixer.Sound("src/resources/pickup.ogg")
        self.splat = pygame.mixer.Sound("src/resources/splat.ogg")
        self.impact = pygame.mixer.Sound("src/resources/impact.ogg")
        self.potion_fizz = pygame.mixer.Sound("src/resources/potion_fizz.ogg")
        self.freeze = pygame.mixer.Sound("src/resources/freeze.ogg")

        self.music = ["music2",
                      "music3",
                      "music4"]

        self.speech = ["speech1",
                       "speech2",
                       "speech3",
                       "speech4"]

        # Link the sounds to the channels they should play in
        self.channel_linkup = {"music1": self.music_channel,
                               "music2": self.music_channel,
                               "music3": self.music_channel,
                               "music4": self.music_channel,
                               "music": self.music_channel,
                               "punch": self.punch_channel,
                               "burn": self.burn_channel,
                               "footstep": self.footstep_channel,
                               "footstep2": self.footstep2_channel,
                               "footstep3": self.footstep3_channel,
                               "footstep4": self.footstep4_channel,
                               "drinking": self.drinking_channel,
                               "click": self.click_channel,
                               "speech1": self.speech_channel,
                               "speech2": self.speech_channel,
                               "speech3": self.speech_channel,
                               "speech4": self.speech_channel,
                               "speech": self.speech_channel,
                               "pickup": self.pickup_channel,
                               "splat": self.splat_channel,
                               "impact": self.impact_channel,
                               "potion_fizz": self.potion_fizz_channel,
                               "freeze": self.freeze_channel}

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
                             "click": self.click,
                             "speech1": self.speech1,
                             "speech2": self.speech2,
                             "speech3": self.speech3,
                             "speech4": self.speech4,
                             "pickup": self.pickup,
                             "splat": self.splat,
                             "impact": self.impact,
                             "potion_fizz": self.potion_fizz,
                             "freeze": self.freeze}

        # This is all the sounds that need to be played
        self.queued_sounds = []

        # Mix the volumes
        self.music2.set_volume(0.6)
        self.music3.set_volume(0.5)
        self.music4.set_volume(0.65)
        self.punch.set_volume(0.3)
        self.burn.set_volume(0.15)
        self.footstep.set_volume(0.8)
        self.footstep2.set_volume(0.6)
        self.footstep3.set_volume(0.8)
        self.footstep4.set_volume(0.6)
        self.drinking.set_volume(0.5)
        self.click.set_volume(1)
        [self.sound_linkup[s].set_volume(0.35) for s in self.speech]
        self.pickup.set_volume(1)
        self.splat.set_volume(0.6)
        self.impact.set_volume(0.5)
        self.potion_fizz.set_volume(0.4)
        self.freeze.set_volume(1)

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
