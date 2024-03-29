import sys

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./assets/images/menuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)  # pega a imagem (surface) e atribui a uma pos no rect

    def run(self):
        pygame.mixer_music.load('./assets/sounds/menuSong.mp3')  # carrega música do menu
        pygame.mixer_music.play(-1)  # roda a música infinitamente
        pygame.mixer_music.set_volume(0.2)  # define volume
        menu_option = 0

        #  desenhar na tela
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # desenha a imagem na surface
            self.menu_text(70, "Moutain", COLOR_ORANGE, ((WIN_WIDTH / 2), 40))
            self.menu_text(70, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 90))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(25, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 200 + 35 * i))
                else:
                    self.menu_text(25, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 35 * i))
            pygame.display.flip()  # atualiza a tela

            #  eventos do game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # comando para fechar a janelo do jogo corretamente
                    sys.exit()  # encera o console
                if event.type == pygame.KEYDOWN:  # se a tecla for pressionada
                    if event.key == pygame.K_DOWN:  # se para baixo for pressionada
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # se para cima for pressionada
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Consolas", size=text_size)  # definindo fonte
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()  # Renderizando fonte
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)  # pegando pos do text
        self.window.blit(source=text_surf, dest=text_rect)  # desenhando tudo
