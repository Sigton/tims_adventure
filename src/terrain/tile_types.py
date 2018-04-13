"""
tile_types.py

This defines how the player
interacts with the tiles in
the game.
"""

solid_tiles = [
    "0017",
    "0018",
    "0019",
    "0020",
    "0021",
    "0022",
    "0023",
    "0024",
    "0025",
    "0026",
    "0027",
    "0028",
    "0029",
    "0030",
    "0044",
    "0063",
    "0072"
]

animated_tiles = [
    "0030",
    "0072",
    "0073"
]

shadowed_decs = [
    "0031",
    "0040",
    "0043",
    "0045",
    "0046",
    "0047",
    "0048",
    "0049",
    "0076"
]

# Vertical distance from sprite to shadow
shadow_height_ratios = {
    "duel_player": 0.8,
    "duel_enemy": 0.8,
    "0031": 0.85,
    "0040": 0.6,
    "0043": 0.85,
    "0045": 0.55,
    "0046": 0.71,
    "0047": 0.68,
    "0048": 0.72,
    "0049": 0.7
}

# Thickness of the shadow
shadow_width_ratios = {
    "duel_player": 0.2,
    "duel_enemy": 0.2,
    "0043": 0.15,
    "0046": 0.45
}

# Width of shadow compared to width of parent
shadow_width_to_parent_ratios = {
    "duel_player": 1.2,
    "duel_enemy": 1.2,
    "0043": 1.2,
    "0045": 1.3,
    "0046": 0.63,
    "0047": 0.9,
    "0048": 0.9,
    "0049": 1.1
}

# x offset of shadow from parent center
shadow_x_offset = {
    "duel_player": -35,
    "duel_enemy": -10
}


spawn_tiles = [
    "0000",
    "0041",
    "0042",
    "0050"
]

no_layer_decs = [
    "0074",
    "0075",
    "0064",
    "0065",
    "0066",
    "0067",
    "0068",
    "0069",
    "0070",
    "0071",
    "0032",
    "0033",
    "0034",
    "0035",
    "0036",
    "0037",
    "0038",
    "0039",
    "0077",
    "0079"
]

no_fade_decs = [
    "0078"
]
