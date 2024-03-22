import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./assets/images/menuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)  # pega a imagem (surface) e atribui a uma pos no rect

    def run(self):
        pygame.mixer_music.load('./assets/sounds/menuSong2.mp3')  # carrega música do menu
        pygame.mixer_music.play(-1)  # roda a música infinitamente
        pygame.mixer_music.set_volume(0.2)  # define volume
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # desenha a imagem na surface
            self.menu_text(50, "Moutain", (255, 128, 0), ((WIN_WIDTH / 2), 70))
            pygame.display.flip()  # atualiza a tela

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Cascadia Mono", size=text_size)  # definindo fonte
        text_surf: Surface = text_font.render(text, True, text_color)  # Renderizando fonte
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)  # pegando pos do text
        self.window.blit(source=text_surf, dest=text_rect)  # desenhando tudo
