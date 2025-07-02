#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.background import Background

from code.player import Player

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position= (0, 0)):
        match entity_name:
            case 'Level1Bgr':
                list_bg = [] # Fundos fixos - Level1Bgr0 até Level1Bgr3
                for i in range(4):
                    WIN_WIDTH * i
                    list_bg.append(Background(f'Level1Bgr{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bgr{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Knight':
                return Player( 'Knight',(2, WIN_WIDTH / 2))


