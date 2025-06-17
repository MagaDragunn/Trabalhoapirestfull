#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as py
from code.menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT

class Game:
    def __init__(self):
        py.init()
        self.window = py.display.set_mode(size=(WIN_WIDTH,WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass