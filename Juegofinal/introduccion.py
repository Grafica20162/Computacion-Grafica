import pygame
from pygame.locals import *

screen = pygame.display.set_mode((710,500))

def Inicio():
    inicio= False
    fondo = pygame.image.load("game_files/introd.png").convert()
    while not inicio:
        for event in pygame.event.get():
            if event.type == QUIT:
                inicio = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    inicio = True

        screen.blit(fondo,(0,0))
        pygame.display.flip()
        pygame.time.delay(10)

    pass
def Intro():
    salir = False
    fondo = pygame.image.load("game_files/introd1.png").convert()
    while not salir:
        for event in pygame.event.get():
            if event.type == QUIT:
                salir = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    salir = True

        screen.blit(fondo,(0,0))
        pygame.display.flip()
        pygame.time.delay(10)
def pausa():
        pausado=True
        fondo = pygame.image.load("game_files/pausa.png").convert()
        while pausado: #mientras este ausado
            for event in pygame.event.get():
                if event.type==pygame.QUIT:#como si presionaramo la tecla x
                    pygame.quit()
                    quit();
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_c:#esto es para continuar
                        pausado=False
                    elif event.key==pygame.K_q:#para terminar
                        pygame.quit()
                        quit()
            screen.blit(fondo,(0,0))
            pygame.display.flip()
            pygame.time.delay(10)