#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author : Aurelien De Ryck
# version : 0.01

import Board
import Player
import logging

logging.basicConfig(level=logging.WARN)

RED = None
BLACK = None


class Game(object):
    """all data about the game"""

    def __init__(self):
        global RED, BLACK

        logging.info("Initialization")
        self.finish = False
        self.turn = 0
        # init all cases
        self.board = Board.Board()

        RED = Player.Player("Red", self.board)
        BLACK = Player.Player("Black", self.board)

        self.playerTurn = RED

        self.display()

        self.startGame()

    def startGame(self):
        logging.info("The game begins")

        while not self.finish:
            self.playerTurn.start()
            self.display()
            if self.playerTurn == RED:
                self.playerTurn = BLACK
            else:
                self.playerTurn = RED
            self.turn += 1
            if self.turn > 5:  # exit after 10 turns
                break
        logging.info("End of the game")

    def display(self):
        msg = "\n"
        w = 0
        while w <= self.board.wsize:
            l = 0
            if w % 2 == 0:
                msg += "    "
            while l <= self.board.lsize:
                msg += str(self.board.cases[(w, l)])
                l += 1
            msg += "|\n"
            w += 1
        msg += "\n"
        msg += str(RED) + "\n"
        msg += str(BLACK) + "\n"
        print(msg)


if __name__ == '__main__':
    game = Game()


