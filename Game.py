#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author : Aurelien De Ryck
# version : 0.01

import Board
import Player
import logging

logging.basicConfig(level=logging.DEBUG)


class Game(object):
    """all data about the game"""

    def __init__(self):
        logging.info("Initialization")
        self.finish = False
        self.turn = 0
        # init all cases
        self.board = Board.Board()

        self.red = Player.Player("Red", self.board)
        self.black = Player.Player("Black", self.board)

        self.playerTurn = self.red

        self.display()

        self.startGame()

    def startGame(self):
        logging.info("The game begins")
        logging.debug(self.board.forests[2])
        logging.debug(self.board.neighbors(self.board.forests[2]))

        while not self.finish:
            self.playerTurn.start()
            if self.playerTurn == self.red:
                self.playerTurn = self.black
            else:
                self.playerTurn = self.red
            self.turn += 1
            if self.turn > 10:  # exit after 10 turns
                break
        logging.info("End of the game")

    def display(self):
        msg = "\n"
        w = 0
        while w <= self.board.wsize:
            l = 0
            while l <= self.board.lsize:
                msg += str(self.board.cases[(w, l)])
                l += 1
            msg += "|\n"
            w += 1
        msg += "\n"
        msg += str(self.red) + "\n"
        msg += str(self.black) + "\n"
        logging.info(msg)


if __name__ == '__main__':
    game = Game()


