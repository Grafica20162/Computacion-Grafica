import pygame
import random


ANCHO = 1000
ALTO = 600

BLANCO=[255,255,255]
NEGRO=[0,0,0]
ROJO=[255,0,0]
azul=[0,255,255]
GRIN=[0,200,0]

class Madera (pygame.sprite.Sprite):
    def __init__(self,archivo,xi,yi,nombre):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.nombre = nombre
        self.rect.x = xi
        self.rect.y = yi

class botonflotador (pygame.sprite.Sprite):
    def __init__(self,archivo,xi,yi,nombre):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.nombre = nombre
        self.rect.x = xi
        self.rect.y = yi

class pintaflotador(pygame.sprite.Sprite):
    def __init__(self,archivo,xi,yi):
        pygame.sprite.Sprite.__init__(self)
        self.image  = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.click = False
        self.rect.x = xi
        self.rect.y = yi
        self.id = 0


class algas(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("alga.png") #pygame Surface dibuja un cuadrado de 20,20
        self.rect=self.image.get_rect() #rect devuelve x,y,width,height
        self.rect.x=x
        self.rect.y=y
        self.var_x=0
        self.var_y=0

if __name__ == "__main__":

    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    fondo=pygame.image.load("Fondo.png") #cargo imagen fondo
    shark1=pygame.image.load("shark11.gif") #Cargo sprite de tiburon1
    shark2=pygame.image.load("sharkd.gif") #Cargo sprite de tiburon2
    Canoa=pygame.image.load("ship.png") #Cargo la canoa
    botonflo = botonflotador("float.png",880,80,"flotador") #Cargo boton flotador
    botonmad = Madera("trunk.png",880,250,"madera") #Cargo boton madera



    #listas de sprites
    listatodos=pygame.sprite.Group() #lista de todos los sprites
    listaalgas=pygame.sprite.Group() #lista donde esta todas las algas
    listabotonflo=pygame.sprite.Group() #lista donde esta todos los flotadores
    listabotonmade=pygame.sprite.Group() #lista donde esta todos las maderas
    listabloques=pygame.sprite.Group() #lista donde esta todos los botones
    
    #Cargo coordenas del tiburon1
    shark_X=100 
    shark_Y=100

    #Cargo coordenadas del tiburon2
    shark2_X=800 
    shark2_Y=400

    #Banderas de partida de los tiburones
    flag=False
    flag2=False

    #Creo las algas y tiburones con sus posiciones
    a=algas(200,445)
    b=algas(300,145)
    c=algas(500,245)
    d=algas(80,145)
    f=algas(700,300)


    #Agrego los sprites a las listas
    listatodos.add(a,b,c,d,f,botonflo,botonmad)
    listaalgas.add(a,b,c,d,f)
    listabotonflo.add(botonflo)
    listabotonmade.add(botonmad)



    contador = 0
    #pantalla.blit(fondo,(0,0)) #con esto coloco el fondo en la pantalla
    #pantalla.blit(shark1,[shark_X,shark_Y]) #Coloco el tiburon1 son las coordenadas en pantalla
    #pantalla.blit(shark2,[shark2_X,shark2_Y]) #Coloco el tiburon2 son las coordenadas en pantalla
    
    pygame.display.flip()

    reloj=pygame.time.Clock()

i = 0
fin = False
while not fin:

    for event in pygame.event.get():
    	if event.type == pygame.MOUSEBUTTONDOWN:
                for b in listabotonflo:
                	if b.rect.collidepoint(event.pos):
                		flotador = pintaflotador("float.png",750,0)
                		#print "pase"
                        flotador.id = contador
                        contador += 1
                        print contador
                        col = True

                        while col:
                            col = False
                            colision = pygame.sprite.spritecollide(flotador,listabloques,False)
                            for bl in colision:
                                if flotador.id != bl.id:
                                    flotador.rect.left = bl.rect.right
                                    col = True

                        listabloques.add(flotador)
                        listatodos.add(flotador)

                for bloque in listabloques:
                    if bloque.rect.collidepoint(event.pos):
                        bloque.update(pantalla)
                        bloque.click = True
                    elif event.type == pygame.MOUSEBUTTONUP:
                    	for bloque in listabloques:
	                        bloque.update(pantalla)
	                        bloque.click = False
	                        col = True

	                        while col:
	                            col = False
	                            colision =pygame.sprite.spritecollide(bloque,listabloques,False)
	                            for e in colision:
	                                if bloque.id != e.id:
	                                    bloque.rect.left = e.rect.right
	                                    col = True










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
    pantalla.blit(Canoa,[400,0])
    listatodos.update()
    listatodos.draw(pantalla)
    pygame.display.flip()
reloj.tick(60)