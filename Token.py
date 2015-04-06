#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author : Aurelien De Ryck
# version : 0.01

import pygame


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
        # need move of 3
        q, r = self.case.coordinate
        listq = range(q - 3, q + 4)
        listr = range(r - 3, r + 4)

        for i in listq:
            for j in listr:
                if abs(i-q) + abs(j-r) <= 3:
                    if (i, j) in board.cases:
                        self.accessible_cases.append((i, j))

        # self.accessible_cases = board.neighbors(self.case)
        # self.accessible_cases.append(self.case)

        print self.accessible_cases

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

    def build(self):
        pass


class Shaman(Token):
    """docstring for Shaman"""

    def __init__(self, case):
        self.name = "Shaman"
        self.case = case
        self.life = 2
        self.sprite = pygame.image.load("sprites/s.png").convert_alpha()
        self.accessible_cases = []

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


class Enchanter(Token):
    """docstring for Enchanter"""

    def __init__(self, case):
        self.name = "Enchanter"
        self.case = case
        self.lifepoint = 2
        self.sprite = pygame.image.load("sprites/s.png").convert_alpha()
        self.accessible_cases = []

    def attack(self):
        pass