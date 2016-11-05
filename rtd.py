--PROBANDO
import pygame
import random


ANCHO = 800
ALTO = 600

BLANCO=[255,255,255]
NEGRO=[0,0,0]
ROJO=[255,0,0]
azul=[0,255,255]
GRIN=[0,200,0]


if __name__ == "__main__":

    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    fondo=pygame.image.load("holamundo.jpg") #cargo imagen
    sp=pygame.image.load("sprite.png")
    pantalla.blit(fondo,(0,0)) #con esto coloco el fondo en la pantalla
    pantalla.blit(sp,(100,100))
    pygame.display.flip()

i = 0
fin = False
while not fin:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True
