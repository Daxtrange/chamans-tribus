#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author : Aurelien De Ryck
# version : 0.01

import pygame
import random
import operator

DIRECTIONS = [
    [(1, 0), (1, -1), (0, -1), (-1, 0), (0, 1), (1, 1)],
    [(1, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]
              ]

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
        q, r = 0, 0

        with open("Map/"+self.map) as f:
            for l in f.readlines():
                q = 0  # start a new line
                for c in l:
                    if c != '\n':
                        case = Cell(int(c), (q, r))
                        self.cases[(q, r)] = case

                        if int(c) == 1:
                            self.circles.append(case)
                        elif int(c) == 2:
                            self.forests.append(case)
                        elif int(c) == 3:
                            self.sanctuaries.append(case)

                        self.lsize = q
                        q += 1

                self.wsize = r
                r += 1

    def neighbors(self, case):
        """
        :return list of all adjacent cells
        """
        q, r = case.coordinate
        parity = r & 1

        listneighboors = []

        for i in range(0,6):
            dir = DIRECTIONS[parity][i]
            coord = tuple(map(operator.add, (q, r), dir))

            if coord in self.cases:
                listneighboors.append(coord)

        return listneighboors

    def loadboard(self, window):
        self.window = window
        right_shift = 48.5
        r = 0
        while r <= self.wsize:
            q = 0
            while q <= self.lsize:
                if r % 2 == 0:
                    # todo : dynamic change
                    self.cases[(q, r)].pygame_coord = (q*97+right_shift+128, r*85+128)
                else:
                    self.cases[(q, r)].pygame_coord = (q*97+128, r*85+128)
                q += 1
            r += 1

    def displayboard(self, accessible_cases):
        for c in self.cases.values():
            pos = c.sprite.get_rect()
            pos.center = c.pygame_coord

            if c.building:
                self.window.blit(c.building.sprite, pos)

            if c.coordinate in accessible_cases:
                self.window.blit(c.sprite_s, pos)
            else:
                self.window.blit(c.sprite, pos)

    def cube_distance(self, a, b):
        a = self.cases[a]
        b = self.cases[b]
        return (abs(a.hex[0] - b.hex[0]) +
                abs(a.hex[1] - b.hex[1]) +
                abs(a.hex[2] - b.hex[2]) / 2)


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

        self.sprite_str = ""
        if self.type == 0:
            self.sprite_str = random.choice(["sprites/WWT-01.png",
                                             "sprites/WWT-02.png",
                                             "sprites/WWT-03.png",
                                             "sprites/WWT-04.png",
                                             "sprites/WWT-05.png",
                                             "sprites/WWT-06.png"])
        elif self.type == 1:
            self.sprite_str = "sprites/WWT-26.png"
        elif self.type == 2:
            self.sprite_str = "sprites/WWT-07.png"
        elif self.type == 3:
            self.sprite_str = "sprites/WWT-11.png"

        self.sprite_str_select = self.sprite_str[:-4]+"_s"+".png"

        self.sprite = pygame.image.load(self.sprite_str).convert_alpha()
        self.sprite_s = pygame.image.load(self.sprite_str_select).convert_alpha()
        self.sprite_center = self.sprite.get_rect().center

        self.pygame_coord = None

        self.hex = self.hex_to_cube()

        self.building = None

    def addBuilding(self, building):
        self.building = building

    def removeBuilding(self):
        self.building = None

    def __str__(self):
        return "| " + str(self.type) + " " + str(self.coordinate)+" "

    def __repr__(self):
        return str(self.type)

    def hex_to_cube(self):
        # convert even-r offset to cube
        x = self.coordinate[0] - (self.coordinate[1] + (self.coordinate[1] & 1)) / 2
        z = self.coordinate[1]
        y = -x-z
        return x, y, z

    def cube_to_hex(self, x, y, z):
        q = x + (z + (z&1)) / 2
        r = z
        return q, r


