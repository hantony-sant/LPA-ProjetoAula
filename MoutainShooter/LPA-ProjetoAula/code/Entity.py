from abc import ABC, abstractmethod

import pygame.image

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./assets/images/' + name + '.png').convert_alpha()  # carrega e associa imagens
        self.rect = self.surf.get_rect(left=position[0], top=position[1])  # de onde vai começar a desnhar o Bg
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'Nome'

    @abstractmethod
    def move(self):
        pass

