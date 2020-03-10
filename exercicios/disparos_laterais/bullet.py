import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ Uma classe que administra projéteis disparados pela espaçonave. """

    
    def __init__(self, ai_settings, screen, ship):
        """ Cria um objeto para o projétil na posição atual da espaçonave. """
        # super(Bullet, self).__init__() # sintaxe do Python 2.7
        super().__init__()
        self.screen = screen

        # Cria um retângulo para o projétil em (0, 0) e, em seguida, 
        # define a posição correta.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centery = ship.rect.centery
        self.rect.x = ship.rect.x

        # Armazena a posição do projétil como um valor decimal
        self.x = float(self.rect.x)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        """ Move o projétil para cima na tela. """
        # Atualiza a posição deicmal do projétil
        self.x += self.speed_factor
        # Atualiza a posição do rect
        self.rect.x = self.x


    def draw_bullet(self):
        """ Desenha o projétil na tela. """
        pygame.draw.rect(self.screen, self.color, self.rect)