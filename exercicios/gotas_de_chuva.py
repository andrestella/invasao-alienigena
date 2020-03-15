import pygame
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group

class Gota(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('gota_de_chuva.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += 1
        self.rect.y = self.y   

def criar_gotas(screen, gotas):
    gota = Gota(screen)
    available_space_x = 1200 - gota.rect.width
    number_gotas_x = int(available_space_x / (2 * gota.rect.width))
    available_space_y = 750 - gota.rect.height
    number_rows = int(available_space_y / gota.rect.height)

    for row_number in range(number_rows):
        for gota_number in range(number_gotas_x):
            gota = Gota(screen)
            gota.x = gota.rect.width + 2 * gota.rect.width * gota_number
            gota.rect.x = gota.x
            gota.rect.y = gota.rect.height + 2 * gota.rect.height * row_number
            gotas.add(gota)

def desenhar_gotas():
    pygame.init()
    screen = pygame.display.set_mode((1200, 750))
    pygame.display.set_caption("Chovendo...")
    
    gotas = Group()

    criar_gotas(screen, gotas)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        gotas.update()
        screen.fill((255, 255, 255)) 
        gotas.draw(screen)
        pygame.display.flip()

desenhar_gotas()