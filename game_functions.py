import sys
import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ Responde a pressionamentos de techa. """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """ Responde a solturas de techa. """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """ Responde a eventos de pressionamento de teclas e de mouse. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """ Atualiza as imagens na tela e alterna para a nova tela. """
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    # Redesenha todos os projéteis atrás da espaçonave e dos alienígenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # Deixa a tela mais recente visível
    pygame.display.flip()

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """ Atualiza a posição dos projéteis e se livra dos projéteis antigos. """
    # Atualiza a posição dos projéteis
    bullets.update() # quando chamamos update() em um grupo, ele
        # chamará update() para cada sprite do grupo
    # Livra-se dos projéteis que desapareceram
    for bullet in bullets.copy(): # não devemos remover itens de
    # uma lista ou de um grupo em um laço 'for', portanto precisamos
    # usar uma cópia do grupo no laço
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """ Responde a colisões entre projéteis e alienígenas. """
    # Verifica se algum projétil atingiu os alienígenas
    # Em caso afirmativo, livra-se do projétil e do alienígena
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # O método 'sprite.groupcollide()' compara o 'rect' de cada projétil 
    # com o 'rect' de cada alienígena e devolve um dicionário contendo os
    # projéteis e os alienígenas que colidiram
    if len(aliens) == 0:
        # Destrói os projéteis existentes e cria uma nova frota
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

def fire_bullet(ai_settings, screen, ship, bullets):
    """ Dispara um projétil se o limite ainda não foi alcançado. """
    # Cria um novo projétil e o adiciona ao grupo de projéteis.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
    """ Determina o número de alienígenas que cabem em uma linha. """
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """ Determina o número de linhas com alienígenas que cabem na tela. """
    available_space_y = (ai_settings.screen_height - 
        (3 * alien_height) - ship_height) # o cálculo está entre
    # parênteses para que o resultado possa ser separado em duas linhas
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """ Cria um alienígena e o posiciona na linha. """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """ Cria uma frota completa de alienígenas. """
    # Cria um alienígena e calcula o número de alienígenas em uma linha
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Cria a frota de alienígenas
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
    """ Responde apropriadamente se algum alienígena alcançou a borda. """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """ Faz toda a frota descer e mudar a sua direção. """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, ship, aliens):
    """ 
    Verifica se a frota está em uma das bordas e então atualiza
    as posições de todos os alienígenas da frota.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Verifica se houve colisões entre alienígenas e a espaçonave
    if pygame.sprite.spritecollideany(ship, aliens):
    # O método 'spritecollideany()' aceita dois argumentos: um sprite e
    # um grupo. O método verifica se algum membro do grupo colidiu com o
    # sprite e para de percorrer o grupo assim que encontrar um membro
    # que tenha colidido com o sprite. Se nenhuma colisão ocorrer, o método
    # devolve 'None'. Se ocorrer colisão, o método devolve o elemento do
    # grupo que colidiu com o sprite.
        print("Ship hit!!!")