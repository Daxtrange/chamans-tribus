#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author : Aurelien De Ryck
# version : 0.01

import Board
import Player


class Game(object):
    """all data about the game"""

    def __init__(self):
        # init all cases
        self.board = Board.Board()

        self.red = Player.Player("Red", self.board)
        self.black = Player.Player("Black", self.board)

        self.playerTurn = self.red

        self.display()

    def startGame(self):
        self.playerTurn.start()



    def display(self):
        print self.board
        print self.red
        print self.black

if __name__ == '__main__':
    game = Game()


