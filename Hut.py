#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author : Aurelien De Ryck
# version : 0.01


class Hut(object):
    def __init__(self):
        self.name = "Huts"


class EconomicHut(Hut):
    def __init__(self):
        self.name = "EconomicHut"
        self.level = 1

    def upgrade(self):
        if self.level <= 3:
            self.level += 1
            return True
        else:
            return False

    def downgrade(self):
        if self > 0:
            self.level -= 1
            return True
        else:
            return False


class TrainingHut(Hut):
    def __init__(self):
        self.name = "TrainingHut"

    def recrute(self):
        pass


class WarriorHut(TrainingHut):
    def __init__(self):
        self.name = "WarriorHut"


class EnchanterHut(TrainingHut):
    def __init__(self):
        self.name = "EnchanterHut"


class PyromancerHut(TrainingHut):
    def __init__(self):
        self.name = "PyromancerHut"


class Tower(Hut):
    def __init__(self):
        self.name = "Tower"


class SpiritLodge(Hut):
    def __init__(self):
        self.name = "SpiritLodge"


class SacrificialPit(Hut):
    def __init__(self):
        self.name = "SacrificialPit"





