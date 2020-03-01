import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """ Inicializa a espaçonave e define sua posição inicial. """
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Armazena um valor decimal para o centro da espaçonave
        self.center = float(self.rect.centerx)
        # Usamos valores decimais para a configuração da velocidade para 
        # que possamos ter um controle mais preciso da mesma quando
        # aumentarmos o ritmo do jogo. No entanto, os atributos de retângulo
        # como 'centerx' armazenam apenas valores inteiros, portanto 
        # precisamos fazer algumas modificações.

        # Flags de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Atualiza a posição da espaçonave de acordo com as flags de movimento."""
        # Atualiza o valor do centro da espaçonave, e não o retângulo
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
            # self.rect.centerx += 1   
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
            # self.rect.centerx -= 1

        # Atualiza o objeto rect de acordo com self.center
        self.rect.centerx = self.center
        # Somente a parte inteira de self.center será armazenada em
        # self.rect.centerx, mas isso não é problema para exibir a 
        # espaçonave

    def blitme(self):
        """ Desenha a espaçonave em sua posição atual. """
        self.screen.blit(self.image, self.rect)