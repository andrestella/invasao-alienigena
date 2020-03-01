import pygame

class Ship():

    def __init__(self, screen):
        """ Inicializa a espaçonave e define sua posição inicial. """
        self.screen = screen

        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Flags de movimento
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """ Atualiza a posição da espaçonave de acordo com as flags de movimento."""
        if self.moving_right:
            self.rect.centerx += 1   
        if self.moving_left:
            self.rect.centerx -= 1
        # Usamos 'if' em vez de utilizar 'elif' para permitir que o valor rect.centerx
        # seja incrementado e decrementado se as duas teclas forem mantidas pressionadas.
        # Isso resulta na espaçonave parada. Se usássemos 'elif' para o movimento à
        # esquerda, a seta para a direita sempre teria prioridade. Fazer isso dessa 
        # maneira deixa os movimentos mais precisos ao alternarmos o movimento da 
        # esquerda para a direita, quando o jogador poderia momentaneamente manter
        # as duas teclas pressionadas.

    def blitme(self):
        """ Desenha a espaçonave em sua posição atual. """
        self.screen.blit(self.image, self.rect)