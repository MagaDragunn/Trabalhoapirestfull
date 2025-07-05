#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Const import ENTITY_SPEED, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_MAGIC, WIN_WIDTH
from code.PlayerMagic import PlayerMagic
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)


    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < 1064:
            self.rect.centerx += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        pass

    def magic(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_MAGIC[self.name]]:
           return PlayerMagic(name=f'{self.name}Magic', position=(self.rect.centerx, self.rect.centery))
