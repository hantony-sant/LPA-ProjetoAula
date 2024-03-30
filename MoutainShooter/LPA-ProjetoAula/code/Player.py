import pygame

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_DOWN
from code.Entity import Entity

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        pressed_key = pygame.key.get_pressed()  # enquanto estiver pressionada Value = True

        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:  # a menos que chegue ao limite da tela
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:  # a menos que chegue ao limite da tela
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:  # a menos que chegue ao limite da tela
            self.rect.centerx -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:  # a menos que chegue ao limite da tela
            self.rect.centerx += ENTITY_SPEED[self.name]