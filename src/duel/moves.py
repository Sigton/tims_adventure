"""
moves.py

This file holds all of
the information about
the different moves that
a player can make.
"""

moves = [
    {"name": "Tackle", "str_mod": 1, "effects":
        "self.start_shake(18, 10, 10, {}1);self.master.sound_engine.queue_sound(('punch', 0))",
     "energy": 6, "xp": 6},
    {"name": "Burn", "str_mod": 1.4, "effects":
        """self.particle_engine.create_particle_spread('fire', 30, {}, {}, 175, 25, 20, 25, 5)
self.master.sound_engine.queue_sound(('burn', 0))""",
     "energy": 14, "xp": 14},
    {"name": "Freeze", "str_mod": 1.5, "effects":
        """self.particle_engine.create_particle_spread('snow', 50, {}, {}, 175, 20, 5, 45, 7)
self.master.sound_engine.queue_sound(('freeze', 0))""",
     "energy": 16, "xp": 16},
    {"name": "Chili Chuck", "str_mod": 0.7, "effects":
        """self.particle_engine.create_particle_spread('chili', 45, {}, {}, 175, 15, 10, 10, 10)
self.master.sound_engine.queue_sound(('impact', 0))""",
     "energy": 5, "xp": 5},
    {"name": "Punch", "str_mod": 1.2, "effects":
        """self.start_shake(18, 10, 10, {}1);self.master.sound_engine.queue_sound(('punch', 0))""",
     "energy": 12, "xp": 12},
    {"name": "Snowball", "str_mod": 0.8, "effects":
        """self.particle_engine.create_particle_spread('snowball', 15, {}, {}, 175, 15, 10, 30, 2)
self.master.sound_engine.queue_sound(('impact', 0))""",
     "energy": 4, "xp": 4},
    {"name": "Feathers", "str_mod": 0.9, "effects":
        """self.particle_engine.create_particle_spread('feather', 45, {}, {}, 175, 35, 10, 5, 5)
self.master.sound_engine.queue_sound(('impact', 0))""",
     "energy": 6, "xp": 6},
    {"name": "Sneak Attack", "str_mod": 1.3, "effects":
        """self.particle_engine.create_particle_spread('leaf', 60, {}, {}, 250, 45, 10, 10, 10)
self.start_shake(18, 10, 10, {}1);self.master.sound_engine.queue_sound(('punch', 0))""",
     "energy": 13, "xp": 13},
    {"name": "Poison Spit", "str_mod": 1.7, "effects":
        """self.particle_engine.create_particle_spread('venom', 20, {}, {}, 175, 10, 10, 40, 4)
self.master.sound_engine.queue_sound(('splat', 0))""",
     "energy": 18, "xp": 18},
    {"name": "Citrus Spray", "str_mod": 1.2, "effects":
        """self.particle_engine.create_particle_spread('lemon', 25, {}, {}, 175, 20, 10, 10, 10)
self.master.sound_engine.queue_sound(('splat', 0))""",
     "energy": 10, "xp": 10},
    {"name": "Stone Throw", "str_mod": 1.4, "effects":
        """self.particle_engine.create_particle_spread('stone', 15, {}, {}, 150, 20, 10, 10, 10)
self.master.sound_engine.queue_sound(('impact', 0))""",
     "energy": 17, "xp": 17},
]
