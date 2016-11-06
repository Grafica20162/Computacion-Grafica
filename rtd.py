
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
    shark1=pygame.image.load("shark1.gif") #Cargo sprite de tiburon
    shark_X=100
    shark_Y=100
    pantalla.blit(fondo,(0,0)) #con esto coloco el fondo en la pantalla
    pantalla.blit(shark1,[shark_X,shark_Y]) #Coloco el tiburon son las coordenadas en pantalla
    
    pygame.display.flip()

    reloj=pygame.time.Clock()
    
i = 0
fin = False
while not fin:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT: #solo se mueve con la tecla de la derecha
                shark_X+=10
            if event.key==pygame.K_LEFT: #solo se mueve con la tecla de la Izquierda
                shark_X+=-10
            if event.key==pygame.K_DOWN: #solo se mueve con la tecla de abajo
                shark_Y+=10
            if event.key==pygame.K_UP: #solo se mueve con la tecla de ARRIBA
                shark_Y+=-10
    pantalla.blit(fondo,(0,0))
    pantalla.blit(shark1,[shark_X,shark_Y])
    pygame.display.flip()
