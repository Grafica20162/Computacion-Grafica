import pygame
import random


ANCHO = 1000
ALTO = 600

BLANCO=[255,255,255]
NEGRO=[0,0,0]
ROJO=[255,0,0]
azul=[0,255,255]
GRIN=[0,200,0]

#Clase donde carga los tiburones
class shark11(pygame.sprite.Sprite):
    def __init__(self,archivo,xi,yi,nombre):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.nombre = nombre
        self.rect.x = xi
        self.rect.y = yi

        self.vida=20 #Definimos la longitud de vida
        #self.sonido2=pygame.mixer.Sound("comidabuena.wav")
        self.sonido1=pygame.mixer.Sound("mordida.wav")
        self.golpe=True


    #con esto le vamos restando cada vez que golpe y se le resta de a 5
    def choque(self):
        #self.vida-=20
        print "Perdiste un elemento "
        
        if  self.golpe:
            self.sonido1.play()



#Clase Jugador principal
class Jugador(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("sprite.png") 
        self.rect=self.image.get_rect() #rect devuelve x,y,width,height
        self.rect.x=x
        self.rect.y=y
        self.var_x=0
        self.var_y=0
        self.vida=800 #Definimos la longitud de vida
        #self.sonido2=pygame.mixer.Sound("comidabuena.wav")
        self.sonido1=pygame.mixer.Sound("mordida.wav")
        self.golpe=True


    #con esto le vamos restando cada vez que golpe y se le resta de a 5
    def choque(self):
        self.vida-=5
        print "Tu vida es: "
        print self.vida
        if  self.golpe:
            self.sonido1.play()

    '''def premioo(self):
        self.vida+=5
        print "Tu vida es: "
        print self.vida
        if  self.golpe:
            self.sonido2.play()'''

    #Me cambia la posicion del Jugador
    def update(self,pantalla):
        self.rect.x += self.var_x
        self.rect.y += self.var_y

#Margen de donde se puede mover el sprite de jugador
def margen():
    if jp.rect.x > 850:
        jp.var_x=0
        jp.rect.x=850

    if jp.rect.y > 580:
        jp.var_y=0
        jp.rect.y=580

    if jp.rect.x < 0:
        jp.var_x=0
        jp.rect.x=0

    if jp.rect.y < 0:
        jp.var_y=0
        jp.rect.y=0

#Clase donde carga la madera cada vez
class Madera (pygame.sprite.Sprite):
    def __init__(self,archivo,xi,yi,nombre):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.nombre = nombre
        self.rect.x = xi
        self.rect.y = yi
        self.var_x=100
        self.var_y=100

#Clase donde carga el boton flotador la madera cada vez
class botonflotador (pygame.sprite.Sprite):
    def __init__(self,archivo,xi,yi,nombre):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.nombre = nombre
        self.rect.x = xi
        self.rect.y = yi


##Clase donde carga el flontador y la madera muchas veces
class pintaflotador(pygame.sprite.Sprite):
    def __init__(self,archivo,xi,yi):
        pygame.sprite.Sprite.__init__(self)
        self.image  = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.click = False
        self.rect.x = xi
        self.rect.y = yi
        self.id = 0

    def update(self,surfac):
        if self.click :
            self.rect.center = pygame.mouse.get_pos()
        surfac.blit(self.image,self.rect)


class algas(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("alga.png") 
        self.rect=self.image.get_rect() 
        self.rect.x=x
        self.rect.y=y
        self.var_x=0
        self.var_y=0

if __name__ == "__main__":

    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    fondo=pygame.image.load("Fondo.png") #cargo imagen fondo

    pygame.mixer.music.load("pista.mp3")
    pygame.mixer.music.play(-1)
    #pygame.mixer.music.set_volume(0.25)

    shark1= shark11("shark11.gif",100,100,"Tiburon1") #Cargo sprite de tiburon1
    shark2= shark11("sharkd.gif",800,400,"Tiburon2") #Cargo sprite de tiburon2
    Canoa=pygame.image.load("ship.png") #Cargo la canoa
    botonflo = botonflotador("float.png",920,80,"flotador") #Cargo boton flotador
    botonmad = Madera("trunk.png",930,280,"madera") #Cargo boton madera
    jp=Jugador(450,50) #creo el jugador



    #listas de sprites
    listatodos=pygame.sprite.Group() #lista de todos los sprites
    listaalgas=pygame.sprite.Group() #lista donde esta todas las algas
    listabotonflo=pygame.sprite.Group() #lista donde esta todos los flotadores
    listabotonmade=pygame.sprite.Group() #lista donde esta todos las maderas
    listabloques=pygame.sprite.Group() #lista donde esta todos los botones
    listatiburones=pygame.sprite.Group() #lista donde esta tdos los tiburones
    
    #Banderas de partida de los tiburones
    flag=False
    flag2=False

    #Creo algas aleatoriamente dentro del mar
    for i in range(30):
        x=random.randrange(ANCHO-20)
        y=random.randrange(ALTO-20)
        if x < 700:
            if y < 400 and y > 50:
                e=algas(x,y)
                listatodos.add(e)
                listaalgas.add(e)

    #Agrego los sprites a las listas
    listatodos.add(botonflo,botonmad,jp,shark1,shark2)
    listabotonflo.add(botonflo)
    listabotonmade.add(botonmad)
    listatiburones.add(shark1,shark2)

        

    contador = 0
    contador2 = 0
    #pantalla.blit(fondo,(0,0)) #con esto coloco el fondo en la pantalla
    #pantalla.blit(shark1,[shark_X,shark_Y]) #Coloco el tiburon1 son las coordenadas en pantalla
    #pantalla.blit(shark2,[shark2_X,shark2_Y]) #Coloco el tiburon2 son las coordenadas en pantalla
    
    pygame.display.flip()

    reloj=pygame.time.Clock()

i = 0
fin = False
while not fin:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_DOWN: #solo se mueve con la tecla de abajo
                    jp.var_y=4
                    jp.var_x=0
                if event.key==pygame.K_UP: #solo se mueve con la tecla de ARRIBA
                    jp.var_y=-4
                    jp.var_x=0
                if event.key == pygame.K_s: # con la tecla s hace stop
                    jp.var_x=0
                    jp.var_y=0

        if event.type == pygame.KEYUP:
            jp.var_x=0
            jp.var_y=0


        if event.type == pygame.MOUSEBUTTONDOWN:
                for b in listabotonflo:
                    if (contador<=2):
                        if b.rect.collidepoint(event.pos):
                            flotador = pintaflotador("float.png",600,0)
                            sonido=pygame.mixer.Sound("seleccion.wav")
                            sonido.play()
                            #listabotonflo.add(flotador)
                            #print "pase"
                            flotador.id = contador
                            contador += 1
                            print "Flotador",contador
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
        #Madera
        col=True
        if event.type == pygame.MOUSEBUTTONDOWN:
                for m in listabotonmade:
                    if (contador2<=2):
                        if m.rect.collidepoint(event.pos):
                            maderaa = pintaflotador("trunk.png",200,0)
                            sonido2=pygame.mixer.Sound("seleccion.wav")
                            sonido2.play()
                            #listabotonmade.add(maderaa)
                            #print "pase"
                            maderaa.id = contador2
                            contador2 += 1
                            print "Madera",contador2
                            col = True

                            while col:
                                col = False
                                colision = pygame.sprite.spritecollide(maderaa,listabloques,False)
                                for bl in colision:
                                    if maderaa.id != bl.id:
                                        maderaa.rect.left = bl.rect.right
                                        col = True

                            listabloques.add(maderaa)
                            listatodos.add(maderaa)
                for bloquem in listabloques:
                    if bloquem.rect.collidepoint(event.pos):
                        bloquem.update(pantalla)
                        bloquem.click = True
        elif event.type == pygame.MOUSEBUTTONUP:
            for bloquem in listabloques:
                    bloquem.update(pantalla)
                    bloquem.click = False
                    col = True
                    while col:
                        col = False
                        colision =pygame.sprite.spritecollide(bloquem,listabloques,False)
                        for ee in colision:
                            if bloquem.id != ee.id:
                                bloquem.rect.left = ee.rect.right
                                col = True           
        if event.type == pygame.QUIT:
            fin = True

    #LLamado a funcion que me mantiene el jugador en su margen 
    margen()




    #MOVIMIENTO DE IZQUIERDA A DERECHA EN LA VENTANA DE TIBURON1
    if (shark1.rect.x==0):
     flag = False
    if(shark1.rect.x==800):
     flag=True
    if flag:
      shark1.rect.x-=2
    else:
      shark1.rect.x+=2

     #MOVIMIENTO DE DERECHA A IZQUIERDA EN LA VENTANA DE TIBURON2
    if (shark2.rect.x==0):
     flag2 = False
    if(shark2.rect.x==800):
     flag2=True
    if flag2:
      shark2.rect.x-=2
    else:
      shark2.rect.x+=2

    l_col=pygame.sprite.spritecollide(shark1,listabloques,True) #lista de colociones de tiburon 1 con flotadores y maderas
    l_col2=pygame.sprite.spritecollide(shark2,listabloques,True) #lista de colociones de tiburon 2 con flotadores y maderas
    l_coljugador=pygame.sprite.spritecollide(jp,listatiburones,False) #lista de colociones de tiburones con jugador
    #l_colmad=pygame.sprite.spritecollide(jp,listatiburones,False) #lista de colociones de tiburones con madera

    #cada que se golpe le voy quitando vida y suena
    for en in l_col:
        shark1.choque()
        if(listabloques==[]): #PARA SABER QUE SE ACABARON LOS FLOTADORES Y MADERAS Y ASI ACABAR JUEGO
           print "perdio"
         #   fin=True
    for ennn in l_col2:
        shark2.choque()

    for enn in l_coljugador:
        jp.choque()
        if(jp.vida==0):
            print "Perdio por bobo"
            letra=pygame.font.Font("Atlantis Heart Free.ttf",80)
            imprime=letra.render("GAME OVER...",True,NEGRO)
            pantalla.blit(imprime,(200,200))
            pygame.display.flip()
            pygame.time.delay(6000)
            fin=True

    pantalla.blit(fondo,(0,0))
    pantalla.blit(Canoa,[400,0]) #Pinto canoa en esa posicion
    
    listatodos.draw(pantalla)
    pygame.display.update()
    listatodos.update(pantalla)
    #pantalla.blit(shark1,[shark_X,shark_Y])
    #pantalla.blit(shark2,[shark2_X,shark2_Y])
    pygame.display.flip()
    reloj.tick(40)