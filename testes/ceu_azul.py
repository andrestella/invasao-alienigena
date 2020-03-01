import sys
import pygame

from airplane import Airplane

def ceu_azul():
    pygame.init()
    screen = pygame.display.set_mode((1000,600))
    pygame.display.set_caption("Céu Azul")
    bg_color = (0, 0, 255)

    # Cria um avião
    airplane = Airplane(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        airplane.blitme()
        pygame.display.flip()

ceu_azul()