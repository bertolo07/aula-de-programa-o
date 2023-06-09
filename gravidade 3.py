#programa não terminado programa não terminado programa não terminado programa não terminado programa não terminado programa não terminado 
import pygame
import math


pygame.init()

WIDTH, HEIGHT =  800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")
clock = pygame.time.Clock()

BLACK=(0,0,0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)

FONT = pygame.font.SysFont("comicsans", 16)

class Planet:
	AU = 149.6e6 * 1000
	G = 6.67428e-11
	SCALE = 250 / AU  # 1AU = 100 pixels
	TIMESTEP = 3600*24 # 1 day

	def __init__(self, x, y, radius, color, mass):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.mass = mass

		self.orbit = []
		self.sun = False
		self.distance_to_sun = 0

		self.x_vel = 0
		self.y_vel = 0
                
		self.acel_x=(G*other.mass)/self.distance_to_sun**2
		self.acel_y=(G*other.mass)/self.distance_to_sun**2
                
		self.x_vel = self.x_vel + self.acel_x
		self.y_vel = self.y_vel + self.acel_y
        

	
        
Sol=Planet(WIDTH/2,HEIGHT/2,20,YELLOW,10)					#Criar planetas
Mercurio=Planet((WIDTH/2)+100,(HEIGHT/2),2,RED,10)
Venus=Planet((WIDTH/2)+200,HEIGHT/2,5,WHITE,10)
Terra=Planet((WIDTH/2)+300,HEIGHT/2,10,BLUE,10)

Mercurio.distance_to_sun=math.sqrt((Mercurio.x-Sol.x)**2+(Mercurio.y-Sol.y)**2)		#Distancia dos planetas
Venus.distance_to_sun=math.sqrt((Venus.x-Sol.x)**2+(Venus.y-Sol.y)**2)
Terra.distance_to_sun=math.sqrt((Terra.x-Sol.x)**2+(Terra.y-Sol.y)**2)




running =True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    L=pygame.draw.rect(WIN,BLACK,(0,0,HEIGHT,WIDTH))
    
    pygame.draw.circle(WIN,Sol.color,(Sol.x,Sol.y),Sol.radius)
    
    pygame.draw.circle(WIN,Mercurio.color,(Mercurio.x,Mercurio.y),Mercurio.radius)
    pygame.draw.circle(WIN,Venus.color,(Venus.x,Venus.y),Venus.radius)
    pygame.draw.circle(WIN,Terra.color,(Terra.x,Terra.y),Terra.radius)
    
    Terra.x_vel=1
    Terra.y_vel=1
    
    Terra.x=Terra.x+Terra.x_vel
    Terra.y=Terra.y+Terra.y_vel

    pygame.display.update()

    clock.tick(60)  

#pygame.display.quit()