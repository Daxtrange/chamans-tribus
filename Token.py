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
        return self.name + "["+str(self.life)+"] : " + str(self.case.coordinate) + " type case : " + str(self.case.type)

    def __repr__(self):
        return self.name + " : " + str(self.case.coordinate)


class Brave(Token):
    """docstring for Brave"""
    def __init__(self, case):
        self.name = "Brave"
        self.case = case
        self.life = 1
        self.sprite = pygame.image.load("sprites/s.png").convert_alpha()

    def build(self):
        pass


class Shaman(Token):
    """docstring for Shaman"""
    def __init__(self, case):
        self.name = "Shaman"
        self.case = case
        self.life = 2
        self.sprite = pygame.image.load("sprites/s.png").convert_alpha()

    def sendSpell(self):
        pass


class Pyromancer(Token):
    """docstring for Pyromancer"""
    def __init__(self, case):
        self.name = "Pyromancer"
        self.case = case
        self.lifepoint = 3
        self.sprite = pygame.image.load("sprites/s.png").convert_alpha()

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


class Enchanter(Token):
    """docstring for Enchanter"""
    def __init__(self, case):
        self.name = "Enchanter"
        self.case = case
        self.lifepoint = 2
        self.sprite = pygame.image.load("sprites/s.png").convert_alpha()

    def attack(self):
        pass