#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.background import Background

from code.player import Player
from code.enemy import Enemy

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bgr':
                list_bg = []
                for i in range(4):
                    WIN_WIDTH * i
                    list_bg.append(Background(f'Level1Bgr{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bgr{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level2Bgr':
                list_bg = []
                for i in range(5):
                    WIN_WIDTH * i
                    list_bg.append(Background(f'Level2Bgr{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bgr{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Knight':
                return Player('Knight', (3, 450))
            case 'Mage':
                return Player('Mage', (3, 450))
            case 'Rogue':
                return Player('Rogue', (3, 450))
            case 'Enemy1':
                return Enemy('Enemy1', (random.randint(WIN_WIDTH + 2, WIN_WIDTH + 200), 450))
            case 'Enemy2':
                return Enemy('Enemy2', (random.randint(WIN_WIDTH + 4, WIN_WIDTH + 200), 450))
            case 'Enemy3':
                return Enemy('Enemy3', (random.randint(WIN_WIDTH + 6, WIN_WIDTH + 200), 450))
