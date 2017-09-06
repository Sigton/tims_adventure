"""
containers.py

Here I create my own container classes
that run more efficiently than python's dicts
"""


class Seed(object):

    # Using __slots__ to maximise memory efficiency
    __slots__ = ["tiles", "decs", "entities"]
