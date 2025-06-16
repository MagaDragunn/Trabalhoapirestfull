#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as py
from code.menu import Menu

class Game:
    def __init__(self):
        self.window = None
        py.init()
        py.display.set_mode(size=(800, 600))
    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass



            # Check for all events
            #for event in py.event.get():
            #   if event.type == py.QUIT:
            #       py.quit()  # close Windows
            #       quit()  # end pygame