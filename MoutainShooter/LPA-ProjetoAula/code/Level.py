import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option  # opção do MENU
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))  # extends- a minha lista com base nesse elementos
        self.entity_list.append(EntityFactory.get_entity('Player1'))

    def run(self, ):
        pygame.mixer_music.load(f'./assets/sounds/{self.name}.mp3')  # carrega música do level
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.2)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)  # define uma taxa de FPS fixa
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)  # desenha as entidades
                self.level_text(14, f'FPS: {clock.get_fps() :.0f}', COLOR_WHITE, (10, 10))
                ent.move()  # faz a imagem se mover

            for event in pygame.event.get():  # kit fechar janela
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Consolas", size=text_size)  # definindo fonte
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()  # Renderizando fonte
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])  # pegando pos do text
        self.window.blit(source=text_surf, dest=text_rect)  # desenhando tudo
