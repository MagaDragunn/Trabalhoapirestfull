#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH
from code.background import Background

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bgr':
                list_bg = []
                # Fundos fixos - Level1Bgr0 até Level1Bgr3
                for i in range(4):
                    WIN_WIDTH * i
                    list_bg.append(Background(f'Level1Bgr{i}', (0, 0)))
                # Fundos que entram após os fixos - Level1Bgr4, depois 5 e 6
                # list_bg.append(Background('Level1Bgr4', (WIN_WIDTH * 4, 0)))
                # list_bg.append(Background('Level1Bgr5', (WIN_WIDTH * 5, 0)))
                # list_bg.append(Background('Level1Bgr6', (WIN_WIDTH * 6, 0)))
                return list_bg


