#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author : Aurelien De Ryck
# version : 0.01

import Board
import Player
import logging
import pygame
from pygame.locals import *


logging.basicConfig(level=logging.WARN)

RED = None
BLACK = None

WINDOWS_SIZE = (1200, 800)


class Game(object):
    """all data about the game"""

    def __init__(self):
        global RED, BLACK

        logging.info("Initialization")
        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(WINDOWS_SIZE)

        self.finish = False
        self.turn = 0
        # init all cases
        self.board = Board.Board()

        RED = Player.Player("Red", self.board, self.window)
        BLACK = Player.Player("Black", self.board, self.window)

        self.playerTurn = BLACK

        # self.display()

        logging.debug("launch window")

        pygame.display.set_caption("Chaman et Tribus")

        self.board.loadboard(self.window)

        # Remplissage de l'arrière-plan
        self.background = pygame.Surface(self.window.get_size()).convert()
        self.background.fill((100, 30, 10))

        font = pygame.font.Font(None, 36)
        text = font.render("Welcome to Chaman & Tribus", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.background.get_rect().centerx
        textpos.centery = 30
        self.background.blit(text, textpos)

        RED.displayTokens()
        BLACK.displayTokens()
        pygame.display.flip()

        self.startGame()

    def startGame(self):
        logging.info("The game begins")
        i = 0
        while not self.finish:
            self.window.blit(self.background, (0, 0))
            self.board.displayboard()
            RED.displayTokens()
            BLACK.displayTokens()

            for event in pygame.event.get():   # list of events
                if event.type == QUIT:
                    self.finish = True
                    logging.info("End of the game")
                if event.type == MOUSEBUTTONDOWN:
                    # self.playerTurn.shaman.case = self.board.cases[(i, 0)]
                    i += 1
                elif event.type == KEYDOWN:
                    cursor = self.playerTurn.shaman.case.coordinate
                    if event.key == K_RIGHT:
                        if cursor[1] + 1 <= self.board.lsize:
                            self.playerTurn.shaman.case = self.board.cases[(cursor[0], cursor[1]+1)]
                    elif event.key == K_LEFT:
                        if cursor[1] - 1 >= 0:
                            self.playerTurn.shaman.case = self.board.cases[(cursor[0], cursor[1]-1)]
                    elif event.key == K_UP:
                        if cursor[0] - 1 >= 0:
                            self.playerTurn.shaman.case = self.board.cases[(cursor[0]-1, cursor[1])]
                    elif event.key == K_DOWN:
                        if cursor[0] + 1 <= self.board.wsize:
                            self.playerTurn.shaman.case = self.board.cases[(cursor[0]+1, cursor[1])]

            if self.playerTurn == RED and self.playerTurn.finish is True:
                self.playerTurn = BLACK
                self.playerTurn.start()

            elif self.playerTurn == BLACK and self.playerTurn.finish is True:
                self.playerTurn = RED
                self.playerTurn.start()
            else:
                pass

            self.turn += 1

            pygame.display.flip()

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


