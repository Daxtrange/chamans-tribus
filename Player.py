#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author : Aurelien De Ryck
# version : 0.01

import Token
import logging

SHAMAN = 0
BRAVE = 1
WARRIOR = 2
PYROMANCER = 3
ENCHANTER = 4


class Player(object):
    """
    Generic player
    can be manipulate by AI
    """

    def __init__(self, color, board):

        self.color = color
        self.board = board
        self.population = 0
        self.limitpopulation = 10

        # initial state
        if self.color == "Red":
            self.wood = 1
            self.mana = 1
            self.initcase = self.board.circles[1]
            self.tokens = {SHAMAN: [Token.Shaman(self.board.circles[1])],
                           BRAVE: [Token.Brave(self.board.circles[1]),
                                   Token.Brave(self.board.circles[1])],
                           WARRIOR: None,
                           PYROMANCER: None,
                           ENCHANTER: None}
            self.population = 2

        else:
            self.wood = 0
            self.mana = 0
            self.initcase = self.board.circles[0]
            self.tokens = {SHAMAN: [Token.Shaman(self.board.circles[0])],
                           BRAVE: [Token.Brave(self.board.circles[0]),
                                   Token.Brave(self.board.circles[0]),
                                   Token.Brave(self.board.circles[0])],
                           WARRIOR: None,
                           PYROMANCER: None,
                           ENCHANTER: None}
            self.population = 3

    def start(self):
        """
        all phases during the turn
        """
        logging.info("Player " + self.color + "'s turn")
        print("Player " + self.color + "'s turn")

        self.reincarnating()
        self.harvesting()
        self.action()
        self.healing()

    def reincarnating(self):
        """
            reincarnation of the Shaman
        """
        logging.debug("reincarnating phase")
        if SHAMAN not in self.tokens or self.tokens[SHAMAN] is None:
            self.tokens[SHAMAN] = [Token.Shaman(self.initcase)]

    def harvesting(self):
        logging.debug("harvesting phase")
        braves = self.tokens.get(BRAVE)
        for brave in braves:
            # todo what's happen if two tokens on one cell?
            if brave in self.board.forests:
                self.wood += 1
            elif brave in self.board.sanctuaries:
                self.mana += 1

    def action(self):
        logging.debug("action phase")
        print("move shaman ->")
        while True:
            x = raw_input("enter x : ")
            y = raw_input("enter y : ")
            try:
                newCoord = (int(x), int(y))
                if self.board.cases[newCoord] is not None:
                    self.tokens[SHAMAN][0].case = self.board.cases[newCoord]
                    break
                else:
                    print("invalid input")
            except:
                print("invalid input")

    def healing(self):
        logging.debug("healing phase")
        #self.tokens.

    def possibleActions(self):
        pass

    def newToken(self, names, coords):
        if self.population + names.length <= self.limitpopulation:
            self.population += names.length
            i = 0
            while i < names.length:
                if names[i] == BRAVE:
                    self.tokens.get(BRAVE).happend(Token.Brave(coords[i]))
                elif names[i] == WARRIOR:
                    self.tokens.get(WARRIOR).happend(Token.Warrior(coords[i]))
                elif names[i] == PYROMANCER:
                    self.tokens.get(PYROMANCER).happend(Token.Pyromancer(coords[i]))
                elif names[i] == ENCHANTER:
                    self.tokens.get(ENCHANTER).happend(Token.Enchanter(coords[i]))
                else:
                    logging.warn("Unknown token : " + names[i])
                    self.population -= 1
                i += 1
        else:
            logging.warn("Population's limit!")

    def __str__(self):
        msg = "Player " + self.color + ":\n"

        for k in self.tokens.keys():
            if self.tokens[k] is not None:
                if type(self.tokens[k]) == list:
                    for i in self.tokens[k]:
                        msg += str(i) + " \n"
                else:
                    msg += str(self.tokens[k]) + " \n"
        msg += "Wood : " + str(self.wood) + " & Mana : " + str(self.mana) + "\n"
        return msg
