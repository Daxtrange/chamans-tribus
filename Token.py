#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author : Aurelien De Ryck
# version : 0.01


class Token(object):
    """Generic token"""
    def __init__(self, coord):
        self.name = "Token"
        self.coordinate = coord
        self.movepoint = 3
        self.lifepoint = 1

    def move(self):
        pass

    def attack(self):
        pass

    def destroy(self):
        pass

    def possibleActions(self):
        """
        list all possible actions for this token
        :return: array
        """
        pass

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name + " : " + str(self.coordinate)


class Brave(Token):
    """docstring for Brave"""
    def __init__(self, coord):
        self.name = "Brave"
        self.coordinate = coord
        self.life = 1

    def build(self):
        pass


class Shaman(Token):
    """docstring for Shaman"""
    def __init__(self, coord):
        self.name = "Shaman"
        self.coordinate = coord
        self.life = 2

    def sendSpell(self):
        pass


class Pyromancer(Token):
    """docstring for Pyromancer"""
    def __init__(self, coord):
        self.name = "Pyromancer"
        self.coordinate = coord
        self.lifepoint = 3

    def sendFireball(self):
        pass


class Warrior(Token):
    """docstring for Warrior"""
    def __init__(self, coord):
        super(Warrior, self).__init__()
        self.name = "Warrior"
        self.coordinate = coord
        self.lifepoint = 4

class Enchanter(Token):
    """docstring for Enchanter"""
    def __init__(self, coord):
        self.name = "Enchanter"
        self.coordinate = coord
        self.lifepoint = 2

    def attack(self):
        pass