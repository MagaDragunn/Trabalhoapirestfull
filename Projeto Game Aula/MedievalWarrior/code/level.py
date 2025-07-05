#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font
from random import choice

from code.Const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME
from code.EntityMediator import EntityMediator
from code.entityFactory import EntityFactory
from code.entity import Entity


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.timeout = 20000  # 20 Segundos
        self.game_mode = game_mode #Modulo de Jogo
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bgr'))
        if game_mode in [MENU_OPTION[0]]:
            self.entity_list.append(EntityFactory.get_entity('Knight'))
        elif game_mode in [MENU_OPTION[1]]:
            self.entity_list.append(EntityFactory.get_entity('Mage'))
        elif game_mode in [MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Rogue'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self, ):
        pygame.mixer_music.load('./asset/Musiclevel1.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice =random.choice(('Enemy1', 'Enemy2', 'Enemy3'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps {clock.get_fps() :.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT- 20))
            pygame.display.flip()
            #Verificador de Colisoes
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)


    def level_text(self, text_size: int, text: str , text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name= 'Arial Black', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
