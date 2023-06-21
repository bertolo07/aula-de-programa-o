import pygame

# Configurações do cronômetro
LARGURA_TELA = 400
ALTURA_TELA = 200
COR_FUNDO = (255, 255, 203) #erro está aqui, a combinação de números está errada, deveria ser 255 para a cor vermelha, 192 para a cor verde, e 203 para a cor azul.
COR_TEXTO = (0, 0, 0)
TAMANHO_TEXTO = 80

# Inicialização do Pygame
pygame.init()
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Cronômetro")
clock = pygame.time.Clock()

# Variáveis do cronômetro
tempo = 0
rodando = False

# Função para formatar o tempo
def formatar_tempo(tempo):
    minutos = tempo // 600
    segundos = (tempo // 10) % 60
    centesimos = tempo % 10
    return f"{minutos:02}:{segundos:02}.{centesimos}"

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rodando = not rodando
            elif event.key == pygame.K_r:
                tempo = 0

    if rodando:
        tempo += 1

    tela.fill(COR_FUNDO)
    texto = pygame.font.SysFont(None, TAMANHO_TEXTO).render(formatar_tempo(tempo), True, COR_TEXTO)
    tela.blit(texto, (LARGURA_TELA // 2 - texto.get_width() // 2, ALTURA_TELA // 2 - texto.get_height() // 2))
    pygame.display.flip()
    clock.tick(100)  # Limite de quadros por segundo


pygame.quit()

#O erro desse arquivo está na cor, pois pedi o fundo com a cor rosa e ele ficou amarelo.