
import pygame
import random


ANCHO = 1000
ALTO = 600

BLANCO=[255,255,255]
NEGRO=[0,0,0]
ROJO=[255,0,0]
azul=[0,255,255]
GRIN=[0,200,0]


if __name__ == "__main__":

    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    fondo=pygame.image.load("Fondo.png") #cargo imagen fondo
    shark1=pygame.image.load("shark11.gif") #Cargo sprite de tiburon1
    shark2=pygame.image.load("sharkd.gif") #Cargo sprite de tiburon2
    
    #Cargo coordenas del tiburon1
    shark_X=100 
    shark_Y=100

    #Cargo coordenadas del tiburon2
    shark2_X=800 
    shark2_Y=400

    #Banderas de partida de los tiburones
    flag=False
    flag2=False

    pantalla.blit(fondo,(0,0)) #con esto coloco el fondo en la pantalla
    pantalla.blit(shark1,[shark_X,shark_Y]) #Coloco el tiburon1 son las coordenadas en pantalla
    pantalla.blit(shark2,[shark2_X,shark2_Y]) #Coloco el tiburon2 son las coordenadas en pantalla
    
    pygame.display.flip()

    reloj=pygame.time.Clock()

i = 0
fin = False
while not fin:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True

    #MOVIMIENTO DE IZQUIERDA A DERECHA EN LA VENTANA DE TIBURON1
    if (shark_X==0):
     flag = False
    if(shark_X==800):
     flag=True
    if flag:
      shark_X-=2
    else:
      shark_X+=2

     #MOVIMIENTO DE DERECHA A IZQUIERDA EN LA VENTANA DE TIBURON2
    if (shark2_X==0):
     flag2 = False
    if(shark2_X==800):
     flag2=True
    if flag2:
      shark2_X-=2
    else:
      shark2_X+=2

    pantalla.blit(fondo,(0,0))
    pantalla.blit(shark1,[shark_X,shark_Y])
    pantalla.blit(shark2,[shark2_X,shark2_Y])
    pygame.display.flip()
    reloj.tick(60)
