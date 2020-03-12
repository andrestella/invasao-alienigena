import pygame
import sys

class Star():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('estrela.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect_width = self.rect.width
        self.rect.y = self.rect.height
        self.rect_height = self.rect.height

def desenhar_estrelas():
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))   
    screen.fill((245, 245, 245)) 
    screen_rect = screen.get_rect()
    pygame.display.set_caption("Estrelas")
    
    star = Star(screen)
    available_space_x = screen_rect.width - 2 * star.rect_width
    number_stars_x = int(available_space_x / (2 * star.rect_width))
    available_space_y = screen_rect.height - 2 * star.rect_height
    number_rows = int(available_space_y / (2 * star.rect_height))

    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            star = Star(screen)
            star.x = star.rect_width + 2 * star.rect_width * star_number
            star.rect.x = star.x
            star.rect.y = star.rect_height + 2 * star.rect_height * row_number
            screen.blit(star.image, star.rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()    
        pygame.display.flip()

desenhar_estrelas()