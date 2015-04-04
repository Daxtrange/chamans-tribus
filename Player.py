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

    def __init__(self, color, board, window):

        self.color = color
        self.board = board
        self.window = window

        self.population = 0
        self.limitpopulation = 10
        self.finish = True

        # initial state
        if self.color == "Red":
            self.wood = 1
            self.mana = 1
            self.initcase = self.board.circles[1]

            self.shaman = Token.Shaman(self.board.circles[1])
            self.braves = [Token.Brave(self.board.circles[1]), Token.Brave(self.board.circles[1])]
            self.warrior = []
            self.pyromancer = []
            self.enchanter = []
            self.population = 2

        else:
            self.wood = 0
            self.mana = 0
            self.initcase = self.board.circles[0]

            self.shaman = Token.Shaman(self.board.circles[0])
            self.braves = [Token.Brave(self.board.circles[0]),
                           Token.Brave(self.board.circles[0]),
                           Token.Brave(self.board.circles[0])]
            self.warrior = []
            self.pyromancer = []
            self.enchanter = []
            self.population = 3

    def start(self):
        """
        all phases during the turn
        """
        logging.info("Player " + self.color + "'s turn")
        print("Player " + self.color + "'s turn")
        self.finish = False
        self.allMoves()
        self.reincarnating()
        self.harvesting()
        # self.action()
        # self.healing()
        print self.__str__()

    def reincarnating(self):
        """
            reincarnation of the Shaman
        """
        logging.debug("reincarnating phase")
        if self.shaman is None:
            self.shaman = Token.Shaman(self.initcase)

    def harvesting(self):
        logging.debug("harvesting phase")

        for brave in self.braves:
            # todo what's happen if two tokens on one cell?
            if brave.case in self.board.forests:
                self.wood += 1
            elif brave.case in self.board.sanctuaries:
                self.mana += 1

    def action(self):
        logging.debug("action phase")
        """
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
        """

    def healing(self):
        logging.debug("healing phase")
        # alltoken = self.tokens.values()


    def possibleActions(self):
        pass

    def newToken(self, names, coords):
        if self.population + names.length <= self.limitpopulation:
            self.population += names.length
            i = 0
            while i < names.length:
                if names[i] == BRAVE:
                    self.braves.append(Token.Brave(coords[i]))
                elif names[i] == WARRIOR:
                    self.warrior.append(Token.Warrior(coords[i]))
                elif names[i] == PYROMANCER:
                    self.pyromancer.append(Token.Pyromancer(coords[i]))
                elif names[i] == ENCHANTER:
                    self.enchanter.append(Token.Enchanter(coords[i]))
                else:
                    logging.warn("Unknown token : " + names[i])
                    self.population -= 1
                i += 1
        else:
            logging.warn("Population's limit!")

    def __str__(self):
        msg = "Player " + self.color + ":\n"

        msg += str(self.shaman) + " \n"

        for i in self.braves:
            msg += str(i) + " \n"
        for i in self.warrior:
            msg += str(i) + " \n"
        for i in self.enchanter:
            msg += str(i) + " \n"
        for i in self.pyromancer:
            msg += str(i) + " \n"

        msg += "Wood : " + str(self.wood) + " & Mana : " + str(self.mana) + "\n"
        return msg

    def displayTokens(self):

        self.window.blit(self.shaman.sprite, self.get_center(self.shaman))

        for i in self.braves:
            self.window.blit(i.sprite, self.get_center(i))
        for i in self.warrior:
            self.window.blit(i.sprite, self.get_center(i))
        for i in self.pyromancer:
            self.window.blit(i.sprite, self.get_center(i))
        for i in self.enchanter:
            self.window.blit(i.sprite, self.get_center(i))

    def get_center(self, token):
        pos = token.sprite.get_rect()
        pos.center = token.case.pygame_coord
        return pos

    def allMoves(self):

        self.shaman.move(self.board)

        for b in self.braves:
            b.move(self.board)
        for e in self.enchanter:
            e.move(self.board)
        for p in self.pyromancer:
            p.move(self.board)
        for w in self.warrior:
            w.move(self.warrior)







