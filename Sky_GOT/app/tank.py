#! /usr/bin/env python3
# Author: Diren Gunasekera
# Description: This script will demo
"""
    Docstring:
"""

class Tank:
    # Class has 2 components = Attributes/Data + Behaviour/Methods

    def __init__(self, country, model):
        country = country
        model = model
        speed = 0
        health = 100
        location = {'x':0, 'y':0, 'z':0}
        direction = 0
        shells = 20
        # No EXPLICIT RETURN as called implicitly

    def accel(self, increase):
        self._speed += increase
        return None

    def decel(self, decrease):
        self._speed -= decrease
        return None

    def rotate_left(self, degrees):
        self._direction -= degrees % 360
        return None

    def rotate_right(self, degrees):
        self._direction += degrees % 360
        return None

    def shoot(self):
        self._shells -= 1
        return None

    def take_damage(self, damage):
        self._health -= damage
        return None