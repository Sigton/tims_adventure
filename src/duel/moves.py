"""
moves.py

This file holds all of
the information about
the different moves that
a player can make.
"""

moves = [
    {"name": "Tackle", "str_mod": 1, "effects": "self.start_shake_player(18, 10, 10, 1)"},
    {"name": "Burn", "str_mod": 1.4, "effects": """self.particle_engine.create_particle_spread
                                                   ('fire', 30, 750, 170, 130, 25, 20, 25, 5)"""}
]
