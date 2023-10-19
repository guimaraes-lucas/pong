# Pong Simples em PYTHON 3 para Iniciantes
# Por @TokyoEdTech

# Parte 1: Iniciando

import pygame

pygame.init()
window = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill("Black")
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
