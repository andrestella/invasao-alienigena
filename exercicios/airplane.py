import pygame

class Airplane():

    def __init__(self, screen):
        """ Inicializa o avião e define sua posição inicial. """
        self.screen = screen

        # Carrega a imagem do avião e obtém seu rect
        # self.image = pygame.image.load('jumbo-jet.bmp')
        self.image = pygame.image.load('jumbo-jet.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia cada novo avião no centro da tela
        self.rect.center = self.screen_rect.center
       
    def blitme(self):
        """ Desenha o avião em sua posição atual. """
        self.screen.blit(self.image, self.rect)