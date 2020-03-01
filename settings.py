class Settings():
    """ Uma classe para armazenar todas as configurações da Invasão Alienígena. """


    def __init__(self):
        """ Inicializa as configurações do jogo. """
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (230, 230, 230)

        # Configurações da espaçonave
        self.ship_speed_factor = 1.5