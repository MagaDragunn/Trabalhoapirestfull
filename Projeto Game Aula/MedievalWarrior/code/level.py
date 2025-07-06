#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import (
    C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY,
    SPAWN_TIME, C_GREEN
)
from code.EntityMediator import EntityMediator
from code.entityFactory import EntityFactory
from code.entity import Entity
from code.player import Player, AnimatedEntity


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.timeout = 20000  # 20 segundos
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []

        # Fundo
        self.entity_list.extend(EntityFactory.get_entity('Level1Bgr'))

        # Adiciona o personagem com base no modo de jogo
        if game_mode in [MENU_OPTION[0]]:
            self.entity_list.append(EntityFactory.get_entity('Knight'))
        elif game_mode in [MENU_OPTION[1]]:
            self.entity_list.append(EntityFactory.get_entity('Mage'))
        elif game_mode in [MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Rogue'))

        # Salva referência do personagem
        if isinstance(self.entity_list[-1], Player):
            self.player = self.entity_list[-1]

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

        self.last_magic_time = 0
        self.magic_cooldown = 400  # em ms

    def run(self):
        pygame.mixer_music.load('./asset/Musiclevel1.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            # Atualiza e desenha as entidades
            to_remove = []
            for ent in self.entity_list:
                if hasattr(ent, 'update_animation'):
                    ent.update_animation(clock.get_time())

                self.window.blit(ent.surf, ent.rect)
                ent.move()

                if hasattr(ent, 'finished') and ent.finished:
                    to_remove.append(ent)

            for ent in to_remove:
                self.entity_list.remove(ent)

            # Eventos do jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == EVENT_ENEMY:
                    choice_enemy = random.choice(('Enemy1', 'Enemy2', 'Enemy3'))
                    self.entity_list.append(EntityFactory.get_entity(choice_enemy))

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        now = pygame.time.get_ticks()
                        if now - self.last_magic_time > self.magic_cooldown:
                            self.last_magic_time = now
                            if hasattr(self, 'player'):
                                pos = (self.player.rect.centerx, self.player.rect.top)
                                magic_name = self.player.name + 'Magic'
                                magic = AnimatedEntity(magic_name, pos)
                                self.entity_list.append(magic)

            # Mostra vida do personagem selecionado
            if hasattr(self, 'player'):
                self.level_text(
                    14,
                    f'{self.player.name} - Health: {self.player.health}',
                    C_GREEN,
                    (10, 20)
                )

            # Outros textos na tela
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_WHITE, (10, 5))
            self.level_text(14, f'fps {clock.get_fps() :.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()

            # Colisões e remoções
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Arial Black', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(text_surf, text_rect)

