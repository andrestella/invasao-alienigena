import sys
import pygame

class Rocket():

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("rocket.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = self.screen_rect.center
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1   
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1


def check_keydown_events(event, rocket):
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True

def check_keyup_events(event, rocket):
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False

def check_events(rocket):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)

def update_screen(bg_color, screen, rocket):
    screen.fill(bg_color)
    rocket.blitme()
    pygame.display.flip()

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Rocket")
    bg_color = (255, 255, 255)
    rocket = Rocket(screen)

    while True:
        check_events(rocket)
        rocket.update()
        update_screen(bg_color, screen, rocket)       

run_game()