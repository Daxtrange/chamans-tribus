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
        # todo change to dynamic size
        self.wsize = 7
        self.lsize = 9

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
                        case = Cell(int(c), actualcoord)
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

    def neighbors(self, case):
        """
        :return list of all adjacent cells
        """
        listneighboors = []
        if case.coordinate[1] + 1 <= self.lsize:
            r = (case.coordinate[0], case.coordinate[1] + 1)
            listneighboors.append(r)
        if case.coordinate[1] - 1 >= 0:
            l = (case.coordinate[0], case.coordinate[1] - 1)
            listneighboors.append(l)

        if case.coordinate[0] % 2 == 0:  # even
            if case.coordinate[0] - 1 >= 0:
                tl = (case.coordinate[0] - 1, case.coordinate[1])
                listneighboors.append(tl)

                if case.coordinate[1] + 1 <= self.lsize:
                    tr = (case.coordinate[0] - 1, case.coordinate[1] + 1)
                    listneighboors.append(tr)

            if case.coordinate[0] + 1 <= self.wsize:
                bl = (case.coordinate[0] + 1, case.coordinate[1])
                listneighboors.append(bl)

                if case.coordinate[1] + 1 <= self.lsize:
                    br = (case.coordinate[0] + 1, case.coordinate[1] + 1)
                    listneighboors.append(br)

        else:  # odd
            if case.coordinate[0] - 1 >= 0:
                if case.coordinate[1] - 1 >= 0:
                    tl = (case.coordinate[0] - 1, case.coordinate[1] - 1)
                    listneighboors.append(tl)

                tr = (case.coordinate[0] - 1, case.coordinate[1])
                listneighboors.append(tr)

            if case.coordinate[0] + 1 <= self.wsize:
                if case.coordinate[1] - 1 >= 0:
                    bl = (case.coordinate[0] + 1, case.coordinate[1] - 1)
                    listneighboors.append(bl)

                br = (case.coordinate[0] + 1, case.coordinate[1])
                listneighboors.append(br)

        return listneighboors


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
        self.occupied = []
        self.coordinate = (coordinate[0], coordinate[1])

    def __str__(self):
        return "case : " + str(self.coordinate)

    def __repr__(self):
        return str(self.type)





