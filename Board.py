#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author : Aurelien De Ryck
# version : 0.01

import pygame
import random


class Board(object):
    def __init__(self, map="map1.txt"):
        self.cases = {}
        self.map = map
        self.circles = []
        self.forests = []
        self.sanctuaries = []

        self.window = None

        self.readMap()

    def __str__(self):
        msg = ""
        for i in self.cases:
            msg += str(i) + "\n"
        return msg

    def readMap(self):
        self.cases = {}
        actualcoord = [0, 0]

        with open("Map/"+self.map) as f:
            for l in f.readlines():
                actualcoord[1] = 0  # start a new line
                for c in l:
                    if c != '\n':
                        case = Cell(int(c), actualcoord)
                        self.cases[(actualcoord[0], actualcoord[1])] = case

                        if int(c) == 1:
                            self.circles.append(case)
                        elif int(c) == 2:
                            self.forests.append(case)
                        elif int(c) == 3:
                            self.sanctuaries.append(case)

                        self.lsize = actualcoord[1]
                        actualcoord[1] += 1

                self.wsize = actualcoord[0]
                actualcoord[0] += 1

    def neighbors(self, case):
        """
        :return list of all adjacent cells
        """
        listneighboors = []
        if case.coordinate[1] + 1 <= self.lsize:
            r = self.cases[(case.coordinate[0], case.coordinate[1] + 1)]
            listneighboors.append(r)
        if case.coordinate[1] - 1 >= 0:
            l = self.cases[(case.coordinate[0], case.coordinate[1] - 1)]
            listneighboors.append(l)

        if case.coordinate[0] % 2 == 0:  # even
            if case.coordinate[0] - 1 >= 0:
                tl = self.cases[(case.coordinate[0] - 1, case.coordinate[1])]
                listneighboors.append(tl)

                if case.coordinate[1] + 1 <= self.lsize:
                    tr = self.cases[(case.coordinate[0] - 1, case.coordinate[1] + 1)]
                    listneighboors.append(tr)

            if case.coordinate[0] + 1 <= self.wsize:
                bl = self.cases[(case.coordinate[0] + 1, case.coordinate[1])]
                listneighboors.append(bl)

                if case.coordinate[1] + 1 <= self.lsize:
                    br = self.cases[(case.coordinate[0] + 1, case.coordinate[1] + 1)]
                    listneighboors.append(br)

        else:  # odd
            if case.coordinate[0] - 1 >= 0:
                if case.coordinate[1] - 1 >= 0:
                    tl = self.cases[(case.coordinate[0] - 1, case.coordinate[1] - 1)]
                    listneighboors.append(tl)

                tr = self.cases[(case.coordinate[0] - 1, case.coordinate[1])]
                listneighboors.append(tr)

            if case.coordinate[0] + 1 <= self.wsize:
                if case.coordinate[1] - 1 >= 0:
                    bl = self.cases[(case.coordinate[0] + 1, case.coordinate[1] - 1)]
                    listneighboors.append(bl)

                br = self.cases[(case.coordinate[0] + 1, case.coordinate[1])]
                listneighboors.append(br)

        return listneighboors

    def loadboard(self, window):
        self.window = window
        right_shift = 48.5
        w = 0
        while w <= self.wsize:
            l = 0
            while l <= self.lsize:
                if w % 2 == 0:
                    # todo : dynamic change
                    self.cases[(w, l)].pygame_coord = (l*97+right_shift+128, w*85+128)
                else:
                    self.cases[(w, l)].pygame_coord = (l*97+128, w*85+128)
                l += 1
            w += 1

    def displayboard(self):
        for c in self.cases.values():
            pos = c.sprite.get_rect()
            pos.center = c.pygame_coord
            self.window.blit(c.sprite, pos)


class Cell(object):
    """
    type :
        0 : empty
        1 : circle
        2 : forest
        3 : Sanctuary
    occupied : list of all token on it
    coordinate : hexagonal coord
    """
    def __init__(self, type, coordinate):
        self.type = type
        self.building = None
        self.coordinate = (coordinate[0], coordinate[1])

        sprite_str = ""
        if self.type == 0:
            sprite_str = random.choice(["sprites/WWT-01.png", "sprites/WWT-02.png", "sprites/WWT-03.png", "sprites/WWT-04.png",
                           "sprites/WWT-05.png", "sprites/WWT-06.png"])
        elif self.type == 1:
            sprite_str = "sprites/WWT-26.png"
        elif self.type == 2:
            sprite_str = "sprites/WWT-07.png"
        elif self.type == 3:
            sprite_str = "sprites/WWT-11.png"

        self.sprite = pygame.image.load(sprite_str).convert_alpha()
        self.sprite_center = self.sprite.get_rect().center

        self.pygame_coord = None

    def addBuilding(self, building):
        self.building = building

    def removeBuilding(self):
        self.building = None

    def __str__(self):
        return "| " + str(self.type) + " " + str(self.coordinate)+" "

    def __repr__(self):
        return str(self.type)