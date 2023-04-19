import pygames

# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()


#pygame.init() - serve para iniciar a biblioteca
#clock relogio interno q dita quantas vezes você quer que a janela autalize = quantas imagens que você quer que apareça na tela por segundo
#na documentação tem várias abas que falam sobre coisas diferentes
#tela desenha em display - tela do computador
# scren cria uma janela = pygames.display.set...
#clock = dentro da biblioteca time e dentro da biblioteca pygames
#greysgrama = preto e branco
#set_mode = tamanho das coordenadas que você tem

