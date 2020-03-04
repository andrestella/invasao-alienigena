import sys
import pygame

class Rocket():

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("rocket.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Rocket")

    bg_color = (255, 255, 255)

    rocket = Rocket(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        rocket.blitme()
        pygame.display.flip()
        

run_game()