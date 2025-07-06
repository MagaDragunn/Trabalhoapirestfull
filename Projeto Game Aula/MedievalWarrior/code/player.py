#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Const import ENTITY_SPEED, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_MAGIC, WIN_WIDTH, ENTITY_DAMAGE
from code.PlayerMagic import PlayerMagic
import pygame
import os
from code.Const import ENTITY_HEALTH
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
        pass

class AnimatedEntity(Entity):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.frames = []
        self.current_frame = 0
        self.animation_timer = 0
        self.animation_speed = 100  # milissegundos entre frames
        self.finished = False
        self.position = position
        self.speed = 8  # velocidade horizontal da magia
        self.health = ENTITY_HEALTH.get(self.name, 1)
        self.damage = ENTITY_DAMAGE.get(self.name, 5)

        self.surf = pygame.Surface((32, 32), pygame.SRCALPHA)  # fallback padrão
        self.rect = self.surf.get_rect(topleft=position)

        self.load_animation_frames()

    def load_animation_frames(self):
        index = 0
        while True:
            path = f'./magic/{self.name}{index}.png'  # <- garante caminho correto
            if not os.path.isfile(path):
                break
            frame = pygame.image.load(path).convert_alpha()
            self.frames.append(frame)
            index += 1

        if self.frames:
            self.surf = self.frames[0]
            self.rect = self.surf.get_rect(topleft=self.position)
        else:
            # Fallback: retém surface e rect padrão (32x32 transparente)
            print(f'[AnimatedEntity] ⚠ Nenhum frame encontrado para {self.name}')

    def update_animation(self, dt):
        if len(self.frames) <= 1 or self.finished:
            return

        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_frame += 1

            if self.current_frame >= len(self.frames):
                self.current_frame = len(self.frames) - 1
                self.finished = True
        self.surf = self.frames[int(self.current_frame)]
    def move(self):
        # Move a magia para a direita (pode ajustar direção)
        self.rect.x += self.speed