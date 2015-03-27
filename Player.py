#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author : Aurelien De Ryck
# version : 0.01

import Token


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
            self.tokens = [Token.Shaman(self.board.circles[1]), Token.Brave(self.board.circles[1]),
                           Token.Brave(self.board.circles[1])]
        else:
            self.wood = 0
            self.mana = 0
            self.tokens = [Token.Shaman(self.board.circles[0]), Token.Brave(self.board.circles[0]),
                           Token.Brave(self.board.circles[0]), Token.Brave(self.board.circles[0])]

    def start(self):
        """
        all phases during the turn
        """
        self.reincarnating()
        self.harversting()
        self.action()
        self.healing()

    def reincarnating(self):
        pass

    def harversting(self):
        pass

    def action(self):
        pass

    def healing(self):
        pass

    def possibleActions(self):
        pass

    def newToken(self):
        pass

    def __str__(self):
        return "Player " + self.color + " : " + str(self.tokens) + " \n wood : " + \
               str(self.wood) + " & mana : " + str(self.mana)

