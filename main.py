# Pong Simples em PYTHON 3 para Iniciantes

# Parte 1: Iniciando

import pygame

# Configuração Inicial
pygame.init()
clock = pygame.time.Clock()

# Configuração da tela principal
largura_tela = 1280
altura_tela = 960
window = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Pong')

# Objetos do Jogo
bola = pygame.Rect(largura_tela / 2 - 15, altura_tela / 2 - 15, 30, 30)
jogador = pygame.Rect(largura_tela - 20, altura_tela / 2 - 70, 10, 140)
oponente = pygame.Rect(10, largura_tela / 2 - 70, 10, 140)

cor_fundo = pygame.color('grey12')
cinza_claro = (200, 200, 200)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill("Black")
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
