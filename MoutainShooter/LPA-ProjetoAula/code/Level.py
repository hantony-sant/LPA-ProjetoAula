import sys
import random

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, MENU_OPTION, EVENT_ENEMY
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option  # opção do MENU
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))  # extends- a minha lista com base nesse elementos
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))

        # geração de inimigos
        pygame.time.set_timer(EVENT_ENEMY, 2000)

    def run(self, ):
        pygame.mixer_music.load(f'./assets/sounds/{self.name}.mp3')  # carrega música do level
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.2)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)  # define uma taxa de FPS fixa

            #  DESENHAR NA TELA
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)  # desenha as entidades
                ent.move()  # faz a imagem se mover
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)

            #  executar o print
            self.level_text(14, f'FPS: {clock.get_fps() :.0f}', COLOR_WHITE, (10, 10))
            self.level_text(14, f'Entidades: {len(self.entity_list)}', COLOR_WHITE, (10, 30))
            pygame.display.flip()

            # VERIFICAR RELACIONAMENTOS DE ENTIDADES
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            # CONFERIR EVENTOS
            for event in pygame.event.get():  # kit fechar janela
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Consolas", size=text_size)  # definindo fonte
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()  # Renderizando fonte
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])  # pegando pos do text
        self.window.blit(source=text_surf, dest=text_rect)  # desenhando tudo
