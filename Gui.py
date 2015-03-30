#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author : Aurelien De Ryck
# version : 0.01

import pygame
import logging


class Gui:
    def __init__(self, board):
        logging.debug("launch window")
        pygame.display.set_caption("Chaman et Tribut")
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((1050, 750))

        self.board = board
        self.loadboard()
        pygame.display.flip()

    def loadboard(self):
        self.board.cases
        w = 0
        while w <= self.board.wsize:
            l = 0
            while l <= self.board.lsize:
                cell = pygame.image.load(self.board.cases[(w, l)].sprite).convert_alpha()
                if w % 2 == 0:
                    self.window.blit(cell, (l*97+48.5, w*85))
                    self.board.cases[(w, l)].pygame_coord = (l*97+48.5, w*85)
                else:
                    self.window.blit(cell, (l*97, w*85))
                    self.board.cases[(w, l)].pygame_coord = (l*97, w*85)

                l += 1
            w += 1










