import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """ Inicializa a espaçonave e define sua posição inicial. """
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia cada nova espaçonave na parte central da lateral esquerda da tela
        self.rect.centery = self.screen_rect.centery
        self.rect.x = 0

        # Armazena um valor decimal para o centro da espaçonave
        self.center = float(self.rect.centery)

        # Flags de movimento
        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        """ Atualiza a posição da espaçonave de acordo com as flags de movimento."""
        if self.moving_top and self.rect.top > self.screen_rect.top:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.ship_speed_factor
           
        # Atualiza o objeto rect de acordo com self.center
        self.rect.centery = self.center

    def blitme(self):
        """ Desenha a espaçonave em sua posição atual. """
        self.screen.blit(self.image, self.rect)