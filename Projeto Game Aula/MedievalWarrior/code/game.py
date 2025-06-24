#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as py
from code.menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level

class Game:
    def __init__(self):
        py.init()
        self.window = py.display.set_mode(size=(WIN_WIDTH,WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, "Level1", menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                py.quit() #Close Window
                quit() # End Pygame
            else:
                pass
