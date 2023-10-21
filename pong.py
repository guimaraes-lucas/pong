import pygame, sys, random


def animacao_bola():
    global velocidade_bola_x, velocidade_bola_y
    # Física da bola
    bola.x += velocidade_bola_x
    bola.y += velocidade_bola_y

    # Colisões da bola
    if bola.top <= 0 or bola.bottom >= altura_tela:
        velocidade_bola_y *= -1
    elif bola.left <= 0 or bola.right >= comprimento_tela:
        reinicia_bola()

    if bola.colliderect(jogador) or bola.colliderect(oponente):
        velocidade_bola_x *= -1


def animacao_jogador():
    # Movimento do Jogador
    jogador.y += velocidade_jogador

    if jogador.top <= 0:
        jogador.top = 0
    elif jogador.bottom >= altura_tela:
        jogador.bottom = altura_tela


def animacao_oponente():
    # Movimento do Oponente
    if oponente.top < bola.y:
        oponente.y += velocidade_oponente
    elif oponente.bottom > bola.y:
        oponente.y -= velocidade_oponente

    if oponente.top <= 0:
        oponente.top = 0
    elif oponente.bottom >= altura_tela:
        oponente.bottom = altura_tela


def reinicia_bola():
    global velocidade_bola_y, velocidade_bola_x
    bola.center = (comprimento_tela/2, altura_tela/2)
    velocidade_bola_y *= random.choice((1, -1))
    velocidade_bola_x *= random.choice((1, -1))

# Configuração Inicial
pygame.init()
clock = pygame.time.Clock()

# Configuração da tela principal
comprimento_tela = 1280
altura_tela = 960
window = pygame.display.set_mode((comprimento_tela, altura_tela))
pygame.display.set_caption('Pong')

# Objetos do Jogo
bola = pygame.Rect(comprimento_tela / 2 - 15, altura_tela / 2 - 15, 30, 30)
oponente = pygame.Rect(comprimento_tela - 20, altura_tela / 2 - 70, 10, 140)
jogador = pygame.Rect(10, altura_tela / 2 - 70, 10, 140)

cor_fundo = pygame.Color('grey12')
cinza_claro = (200, 200, 200)

# Velocidade dos Objetos
velocidade_bola_x = 7 * random.choice((1, -1))
velocidade_bola_y = 7 * random.choice((1, -1))
velocidade_jogador = 0
velocidade_oponente = 6

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                velocidade_jogador -= 6
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                velocidade_jogador += 6

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                velocidade_jogador += 6
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                velocidade_jogador -= 6

    animacao_bola()
    animacao_jogador()
    animacao_oponente()

    # Visuais
    window.fill(cor_fundo)
    pygame.draw.rect(window, cinza_claro, jogador)
    pygame.draw.rect(window, cinza_claro, oponente)
    pygame.draw.ellipse(window, cinza_claro, bola)
    pygame.draw.aaline(window, cinza_claro, (comprimento_tela / 2, 0), (comprimento_tela / 2, altura_tela))

    pygame.display.flip()
    clock.tick(60)
