#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author : Aurelien De Ryck
# version : 0.01


class Board(object):
    def __init__(self, map="map1.txt"):
        self.cases = []
        self.map = map
        self.circles = []
        self.forests = []
        self.sanctuaries = []

        self.readMap()

    def __str__(self):
        toreturn = ""
        for i in self.cases:
             toreturn += str(i) + "\n"
        return toreturn

    def readMap(self):
        actualcoord = [0, 0]

        with open("Map/"+self.map) as f:
            for l in f.readlines():
                actualcoord[1] = 0  # start a new line
                line = []
                for c in l:
                    if c != '\n':
                        case = Case(int(c), actualcoord)
                        line.append(case)

                        if int(c) == 1:
                            self.circles.append(case)
                        elif int(c) == 2:
                            self.forests.append(case)
                        elif int(c) == 3:
                            self.sanctuaries.append(case)

                        actualcoord[1] += 1
                self.cases.append(line)
                actualcoord[0] += 1


class Case(object):
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
        self.occupied = []
        self.coordinate = (coordinate[0], coordinate[1])

    def __str__(self):
        return "case : " + str(self.coordinate)

    def __repr__(self):
        return str(self.type)


