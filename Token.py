#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author : Aurelien De Ryck
# version : 0.01

import pygame
import Hut


class Token(object):
    """Generic token"""

    def __init__(self, case):
        self.name = "Token"
        self.case = case
        self.movepoint = 3
        self.lifepoint = 1
        self.accessible_cases = []

    def move(self, board):
        self.accessible_cases = []
        x, y, z = self.case.hex
        N = self.movepoint

        for dx in range(-N, N+1):
            for dy in range(max(-N, -dx-N), min(N+1, -dx+N+1)):
                dz = -dx-dy
                if dx + dy + dz == 0:
                    q, r = self.case.cube_to_hex(x+dx, y+dy, z+dz)
                    if (q, r) in board.cases:
                        self.accessible_cases.append(
                            (q, r)
                        )

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
        return self.name + "[" + str(self.life) + "] : " + str(self.case.coordinate) + " type case : " + str(
            self.case.type)

    def __repr__(self):
        return self.name + " : " + str(self.case.coordinate)


class Brave(Token):
    """docstring for Brave"""

    def __init__(self, case):
        self.name = "Brave"
        self.case = case
        self.life = 1
        self.sprite = pygame.image.load("sprites/b.png").convert_alpha()
        self.accessible_cases = []
        self.movepoint = 3

    def build(self, hut_name):
        """
        Call build class
        :return:
        """
        self.case.building = Hut.EconomicHut()
        print "a economic hut is build"

class Shaman(Token):
    """docstring for Shaman"""

    def __init__(self, case):
        self.name = "Shaman"
        self.case = case
        self.life = 2
        self.sprite = pygame.image.load("sprites/s.png").convert_alpha()
        self.accessible_cases = []
        self.movepoint = 3

    def sendSpell(self):
        pass


class Pyromancer(Token):
    """docstring for Pyromancer"""

    def __init__(self, case):
        self.name = "Pyromancer"
        self.case = case
        self.lifepoint = 3
        self.sprite = pygame.image.load("sprites/s.png").convert_alpha()
        self.accessible_cases = []
        self.movepoint = 3

    def sendFireball(self):
        pass


class Warrior(Token):
    """docstring for Warrior"""

    def __init__(self, case):
        super(Warrior, self).__init__()
        self.name = "Warrior"
        self.case = case
        self.lifepoint = 4
        self.sprite = pygame.image.load("sprites/s.png").convert_alpha()
        self.accessible_cases = []
        self.movepoint = 3


class Enchanter(Token):
    """docstring for Enchanter"""

    def __init__(self, case):
        self.name = "Enchanter"
        self.case = case
        self.lifepoint = 2
        self.sprite = pygame.image.load("sprites/s.png").convert_alpha()
        self.accessible_cases = []
        self.movepoint = 3

    def attack(self):
        pass