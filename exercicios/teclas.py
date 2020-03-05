import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))   
pygame.display.set_caption("Testando teclas...")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(event.key)