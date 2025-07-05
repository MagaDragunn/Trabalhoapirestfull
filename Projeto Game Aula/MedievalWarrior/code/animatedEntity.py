import pygame
import os
from code.Const import ENTITY_HEALTH
from code.entity import Entity

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
            print(f'[AnimatedEntity] ⚠️ Nenhum frame encontrado para {self.name}')

    def update_animation(self, dt):
        if len(self.frames) <= 1 or self.finished:
            return

        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_frame += 1
            if self.current_frame >= len(self.frames):
                self.finished = True
            else:
                self.surf = self.frames[self.current_frame]

    def move(self):
        # Move a magia para a direita (pode ajustar direção)
        self.rect.x += self.speed
