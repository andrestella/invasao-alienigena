import sys

import pygame

def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    # O objeto 'screen' é chamado de superfície. Uma superfície no Pygame 
    # é uma parte da tela em que exibimos um elemento do jogo. Cada 
    # elemento do jogo, por exemplo, os alienígenas ou a espaçonave, é
    # uma superfície. A superfície devolvida por 'display.set_mode()'
    # representa a janela inteira do jogo. Quando ativamos o laço de 
    # animação do jogo, essa superfície é automaticamente redesenhada
    # a cada passagem pelo laço.
    pygame.display.set_caption("Alien Invasion")

    # Define a cor de fundo
    bg_color = (230, 230, 230)
    # As cores no Pygame são especificadas como cores RGB

    # Inicia o laço principal do jogo
    while True:
    # O jogo é controlado por uma laço 'while' que contém um laço de 
    # eventos e o código que administra as atualizações de tela.
    # Um evento é uma ação realizada pelo usuário enquanto joga, por 
    # exemplo, pressionar uma tecla ou mover o mouse. Para fazer nosso
    # programa responder aos eventos, escreveremos um laço de eventos
    # para ouvir um evento e executar uma tarefa apropriada de acordo 
    # com o tipo de evento ocorrido. O laço 'for' abaixo é um laço
    # de eventos.

        # Observa eventos de teclado e de mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redesenha a tela a cada passagem pelo laço
        screen.fill(bg_color)

        # Deixa a tela mais recente visível
        pygame.display.flip()

run_game()