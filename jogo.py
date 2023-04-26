import pygame


pygame.init()

def __init__(self, x, y, radius, color, mass):
    self.x = x
    self.y = y
    self.radius = radius
    self.color = color
    self.mass = mass

    self.orbit = []
    self.sun = False
    self.distance_to_sun = 0.

    self.x_vel = 0
    self.x_vel = 0

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    pygame.display.flip()

    clock.tick(60)  

pygame.quit()


#pygame.init() - serve para iniciar a biblioteca
#clock relogio interno q dita quantas vezes você quer que a janela autalize = quantas imagens que você quer que apareça na tela por segundo
#na documentação tem várias abas que falam sobre coisas diferentes
#tela desenha em display - tela do computador
# scren cria uma janela = pygames.display.set...
#clock = dentro da biblioteca time e dentro da biblioteca pygames
#greysgrama = preto e branco
#set_mode = tamanho das coordenadas que você tem
#WIN = janela
#pygame.display.set_caption ("nome do bagulho")
#FONT = pygame.font.SysFont("nome da fonte", 16)
# Class Planet: = nome de uma classe, é uma categoria de dados q ele criou
#sempre que formos criar uma classecolocamos -> def __init__
#self vai ta sempre na classe, para puxar as caraterísticas de fora pra dentro
# x e y = posição
#radius = raio; color = cor; mass= massa




