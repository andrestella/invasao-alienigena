import pygame

def ceu_azul():
    pygame.init()
    screen = pygame.display.set_mode((1000,600))
    pygame.display.set_caption("Céu Azul")
    bg_color = (0, 0, 255)
    screen.fill(bg_color)
    pygame.display.flip()

ceu_azul()