#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/MenuBg.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self,):
        pygame.mixer_music.load("./asset/Menu.wav")
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=80, text= "Medival Warriors", text_color=(255, 0, 0), text_center_pos=((WIN_WIDTH / 2),70))
            pygame.display.flip()
            # Check all Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # End Pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Arial Black", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)