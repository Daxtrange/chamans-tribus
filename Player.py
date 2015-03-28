#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author : Aurelien De Ryck
# version : 0.01

import Token
import logging


class Player(object):
    """
    Generic player
    can be manipulate by AI
    """
    def __init__(self, color, board):

        self.color = color
        self.board = board

        # initial state
        if self.color == "Red":
            self.wood = 1
            self.mana = 1
            self.initcase = self.board.circles[1]
            self.tokens = {"Shaman": Token.Shaman(self.board.circles[1]), "Braves": [Token.Brave(self.board.circles[1]),
                           Token.Brave(self.board.circles[1])]}
        else:
            self.wood = 0
            self.mana = 0
            self.initcase = self.board.circles[0]
            self.tokens = {"Shaman": Token.Shaman(self.board.circles[0]), "Braves": [Token.Brave(self.board.circles[0]),
                           Token.Brave(self.board.circles[0]), Token.Brave(self.board.circles[0])]}

    def start(self):
        """
        all phases during the turn
        """
        logging.info("Player " + self.color + "'s turn")
        self.reincarnating()
        self.harvesting()
        self.action()
        self.healing()

    def reincarnating(self):
        """
            reincarnation of the Shaman
        """
        logging.debug("reincarnating phase")
        if "Shaman" not in self.tokens:
            self.tokens["Shaman"] = Token.Shaman(self.initcase)

    def harvesting(self):
        logging.debug("harvesting phase")
        braves = self.tokens.get("Braves")
        for brave in braves:
            # todo what's happen if two tokens on one cell?
            if brave in self.board.forests:
                self.wood += 1
            elif brave in self.board.sanctuaries:
                self.mana += 1

    def action(self):
        logging.debug("action phase")

    def healing(self):
        logging.debug("healing phase")

    def possibleActions(self):
        pass

    def newToken(self):
        pass

    def __str__(self):
        return "Player " + self.color + " : " + str(self.tokens) + " \n wood : " + \
               str(self.wood) + " & mana : " + str(self.mana)

