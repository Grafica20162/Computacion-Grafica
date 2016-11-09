import pygame
import random


ANCHO = 1000
ALTO = 600

BLANCO=[255,255,255]
NEGRO=[0,0,0]
ROJO=[255,0,0]
azul=[0,255,255]
GRIN=[0,200,0]

#Clase donde cargo las rayas
class rayas(pygame.sprite.Sprite):
    def __init__(self,archivo,xi,yi,nombre):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.nombre = nombre
        self.rect.x = xi
        self.rect.y = yi

        self.vida=20 #Definimos la longitud de vida



    #con esto le vamos restando cada vez que golpe y se le resta de a 5
    def choque(self):
        self.vida-=20
      



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
        self.vida=100 #Definimos la longitud de vida
        #self.sonido2=pygame.mixer.Sound("comidabuena.wav")
        self.sonido1=pygame.mixer.Sound("mordida.wav")
        self.sonidooo=pygame.mixer.Sound("elec.wav")
        self.golpe=True


    #con esto le vamos restando cada vez que golpe y se le resta de a 5
    def choque(self):
        self.vida-=1
        print "Tu vida es: "
        print self.vida

        if  self.golpe:
            self.sonido1.play()

    def choque2(self):
        self.vida-=1
        print "Tu vida es: "
        print self.vida

        if  self.golpe:
            self.sonidooo.play()

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

def muerte():
    #print "Perdio por bobo"
    letra=pygame.font.Font("Atlantis Heart Free.ttf",80)
    imprime=letra.render("GAME OVER...",True,NEGRO)
    pantalla.blit(imprime,(200,200))
    pygame.display.flip()
    pygame.time.delay(6000)
    fin=True

if __name__ == "__main__":

    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    fondo=pygame.image.load("Fondo.png") #cargo imagen fondo

    #Musica de fondo
    pygame.mixer.music.load("pista.mp3")
    pygame.mixer.music.play(-1)
    #pygame.mixer.music.set_volume(0.25)

    #Cargo sprites
    shark1= shark11("shark11.gif",100,100,"Tiburon1") #Cargo sprite de tiburon1
    shark2= shark11("sharkd.gif",800,400,"Tiburon2") #Cargo sprite de tiburon2
    Canoa=pygame.image.load("ship.png") #Cargo la canoa
    raya=rayas("raya.png",200,200,"Raya1")
    raya2=rayas("raya.png",400,300,"Raya2")
    botonflo = botonflotador("float.png",920,80,"flotador") #Cargo boton flotador
    botonmad = Madera("trunk.png",930,280,"madera") #Cargo boton madera
    titleF= pygame.image.load("titleF.png") #caga titulo
    titleM= pygame.image.load("titleM.png") #carga titulo
    muelle= pygame.image.load("muelle.png") #carga titulo
    jp=Jugador(450,50) #creo el jugador



    #listas de sprites
    listatodos=pygame.sprite.Group() #lista de todos los sprites
    listaalgas=pygame.sprite.Group() #lista donde esta todas las algas
    listabotonflo=pygame.sprite.Group() #lista donde esta todos los flotadores
    listabotonmade=pygame.sprite.Group() #lista donde esta todos las maderas
    listabloques=pygame.sprite.Group() #lista donde esta todos los botones
    listatiburones=pygame.sprite.Group() #lista donde esta tdos los tiburones
    listaflotadores=pygame.sprite.Group() #Lista donde guardo los 3 flotadores
    listamaderas=pygame.sprite.Group() #Lista donde guardo las 3 maderas
    listainteraccion=pygame.sprite.Group() #Lista donde esta el jugador, flotadores y maderas
    listarayas=pygame.sprite.Group() #Lista donde estan las rayas

    #Banderas de partida de los tiburones y rayas
    flag=False
    flag2=False
    flag3=False
    flag4=False

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
    listatodos.add(jp,shark1,shark2,botonflo,botonmad,raya,raya2)
    listabotonflo.add(botonflo)
    listabotonmade.add(botonmad)
    listatiburones.add(shark1,shark2)
    listarayas.add(raya,raya2)
    #listamaderas.add(botonmad)
    #listaflotadores.add(botonflo)
    #listainteraccion.add(jp)

    

    contador = 0
    contador2 = 0
    contador3=0 #Contador para saber si las listas de flota y made ya estan vacias
    #pantalla.blit(fondo,(0,0)) #con esto coloco el fondo en la pantalla
    #pantalla.blit(shark1,[shark_X,shark_Y]) #Coloco el tiburon1 son las coordenadas en pantalla
    #pantalla.blit(shark2,[shark2_X,shark2_Y]) #Coloco el tiburon2 son las coordenadas en pantalla
    
    pygame.display.flip()

    reloj=pygame.time.Clock()

i = 0
fin = False
while not fin:

    #Muestro vida
    letra=pygame.font.Font("Atlantis Heart Free.ttf",40)
    Fvida= letra.render("Vida: "+str(jp.vida), True, NEGRO)
    

    if(jp.vida==0 ):
        letraaaa=pygame.font.Font("Atlantis Heart Free.ttf",80)
        imprimir=letraaaa.render("GAME OVER...",True,NEGRO)
        pantalla.blit(imprimir,(200,200))
        letraaa=pygame.font.Font("Atlantis Heart Free.ttf",40)
        imprimeee=letraaa.render("Te mato una raya",True,NEGRO)
        pantalla.blit(imprimeee,(300,300))
        pygame.display.flip()
        pygame.time.delay(6000)
        fin=True
    
    for event in pygame.event.get():
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
                                colision = pygame.sprite.spritecollide(flotador,listaflotadores,False)
                                for bl in colision:
                                    if flotador.id != bl.id:
                                        flotador.rect.left = bl.rect.right
                                        col = True

                            #listabloques.add(flotador)
                            listaflotadores.add(flotador)
                            listainteraccion.add(flotador)
                            listatodos.add(flotador)

                for bloque in listaflotadores:
                    if bloque.rect.collidepoint(event.pos):
                        bloque.update(pantalla)
                        bloque.click = True
        elif event.type == pygame.MOUSEBUTTONUP:
            for bloque in listaflotadores:
                    bloque.update(pantalla)
                    bloque.click = False
                    col = True
                    while col:
                        col = False
                        colision =pygame.sprite.spritecollide(bloque,listaflotadores,False)
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
                            sonido2=pygame.mixer.Sound("madera.wav")
                            sonido2.play()
                            #listabotonmade.add(maderaa)
                            #print "pase"
                            maderaa.id = contador2
                            contador2 += 1
                            print "Madera",contador2
                            col = True

                            while col:
                                col = False
                                colision = pygame.sprite.spritecollide(maderaa,listamaderas,False)
                                for bl in colision:
                                    if maderaa.id != bl.id:
                                        maderaa.rect.left = bl.rect.right
                                        col = True

                            #listabloques.add(maderaa)
                            listamaderas.add(maderaa)
                            listainteraccion.add(maderaa)
                            listatodos.add(maderaa)
                for bloquem in listamaderas:
                    if bloquem.rect.collidepoint(event.pos):
                        bloquem.update(pantalla)
                        bloquem.click = True
        elif event.type == pygame.MOUSEBUTTONUP:
            for bloquem in listamaderas:
                    bloquem.update(pantalla)
                    bloquem.click = False
                    col = True
                    while col:
                        col = False
                        colision =pygame.sprite.spritecollide(bloquem,listamaderas,False)
                        for ee in colision:
                            if bloquem.id != ee.id:
                                bloquem.rect.left = ee.rect.right
                                col = True           
        if event.type == pygame.QUIT:
            fin = True

        #CAMINO

        l_colinteraccion=pygame.sprite.spritecollide(jp,listainteraccion,False) #lista de coliciones de jp con mad y flota
        
        aux=False

        if(l_colinteraccion):
            print "True"
            aux=True

        if event.type == pygame.KEYDOWN and aux:

            if event.key==pygame.K_DOWN: #solo se mueve con la tecla de abajo
                jp.var_y=4
                jp.var_x=0
            if event.key==pygame.K_UP: #solo se mueve con la tecla de ARRIBA
                jp.var_y=-4
                jp.var_x=0
            if event.key == pygame.K_s: # con la tecla s hace stop
                jp.var_x=0
                jp.var_y=0
            aux=False

        if event.type == pygame.KEYUP:
            jp.var_x=0
            jp.var_y=0

        '''if (pene==False):
            jp.vida=0'''


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

    #MOVIMIENTO DE LA RAYA
    if (raya.rect.x==100):
     flag3 = False
    if(raya.rect.x==400):
     flag3=True
    if flag3:
      raya.rect.x-=2
    else:
      raya.rect.x+=2

    #MOVIMIENTO DE LA RAYA2
    if (raya2.rect.x==100):
     flag4 = False
    if(raya2.rect.x==400):
     flag4=True
    if flag4:
      raya2.rect.x-=2
    else:
      raya2.rect.x+=2

    l_col=pygame.sprite.spritecollide(shark1,listaflotadores,True) #lista de colociones de tiburon 1 con flotadores
    l_col2=pygame.sprite.spritecollide(shark2,listamaderas,True) #lista de colociones de tiburon 2  maderas
    l_col3=pygame.sprite.spritecollide(shark1,listamaderas,True) #lista de colociones de tiburon 1 con maderas
    l_col4=pygame.sprite.spritecollide(shark2,listaflotadores,True) #lista de colociones de tiburon 2 con flotadores 
    l_coljugador=pygame.sprite.spritecollide(jp,listatiburones,False) #lista de colociones de tiburones con jugador
    l_coljugadorflota=pygame.sprite.spritecollide(jp,listaflotadores,False) #lista de colociones de tiburones con jugador
    l_coljugadoraya=pygame.sprite.spritecollide(jp,listarayas,False) #lista de colociones de tiburones con jugador
    
   



    #colision del tibu 1 con flotadores
    for en in l_col:
        shark1.choque()
        listaflotadores.remove(flotador)
        contador3+=1
        #if(listabloques==[]): #PARA SABER QUE SE ACABARON LOS FLOTADORES Y MADERAS Y ASI ACABAR JUEGO
         #  print "perdio"
         #   fin=True

    #Colision del tibu 1 con maderas
    for en in l_col3:
        shark1.choque()
        listamaderas.remove(maderaa)
        contador3+=1

    #colision del tibu 2 con maderas
    for ennn in l_col2:
        shark2.choque()
        listamaderas.remove(maderaa)
        contador3+=1


    #Colision del tibu 2 con flota
    for ennn in l_col4:
        shark2.choque()
        listaflotadores.remove(flotador)
        contador3+=1

    #Colision del juador con raya
    for ennnn in l_coljugadoraya:
        jp.choque2()
        

      
    for enn in l_coljugador:
        jp.choque()
        if(jp.vida=="0"):
            #print "Perdio por bobo"
            
            '''letra=pygame.font.Font("Atlantis Heart Free.ttf",80)
            imprime=letra.render("GAME OVER...",True,NEGRO)
            pantalla.blit(imprime,(200,200))
            etraaa=pygame.font.Font("Atlantis Heart Free.ttf",40)
            imprimeee=letraaa.render("Te mato un Tiburon",True,NEGRO)
            pantalla.blit(imprimeee,(300,300))
            pygame.display.flip()
            pygame.time.delay(6000)
            fin=True'''

    #Avisa cuando llega al muelle GANA
    if(jp.rect.y>507 and jp.rect.y<1000):
        letr=pygame.font.Font("Atlantis Heart Free.ttf",80)
        Aviso=letr.render("Felicidades Ganaste",True,NEGRO)
        pantalla.blit(Aviso,(200,200))
        pygame.display.flip()
        pygame.time.delay(10000)
        fin=True

    #Valido si el jugador cae al agua cuando pasa un tiburon encima de el
    if(jp.rect.y>85 and jp.rect.y<507 and l_coljugador):

        letraa=pygame.font.Font("Atlantis Heart Free.ttf",80)
        imprimee=letraa.render("GAME OVER...",True,NEGRO)
        pantalla.blit(imprimee,(200,200))
        letraaa=pygame.font.Font("Atlantis Heart Free.ttf",40)
        imprimeee=letraaa.render("Caiste al agua y te comio un tiburon",True,NEGRO)
        pantalla.blit(imprimeee,(200,300))
        pygame.display.flip()
        pygame.time.delay(6000)
        fin=True

    '''if(l_coljugadorflota):
        print "hola"'''
 
        
    #Pierde si se queda sin elementos
    if(contador3==6):
        letraa=pygame.font.Font("Atlantis Heart Free.ttf",80)
        imprimee=letraa.render("GAME OVER...",True,NEGRO)
        pantalla.blit(imprimee,(200,200))
        letraaa=pygame.font.Font("Atlantis Heart Free.ttf",40)
        imprimeee=letraaa.render("Perdiste todos los elementos",True,NEGRO)
        pantalla.blit(imprimeee,(300,300))
        pygame.display.flip()
        pygame.time.delay(6000)
        fin=True

    pantalla.blit(fondo,(0,0))
    pantalla.blit(Canoa,[400,0]) #Pinto canoa en esa posicion    
    pantalla.blit(titleF,[925,40]) #pinto titulo de flotadores
    pantalla.blit(titleM,[927,240]) #Pinto titulo de Maderas
    pantalla.blit(muelle,[740,550])
    pantalla.blit(Fvida,(60,550))
    listatodos.draw(pantalla)
    pygame.display.update()
    listatodos.update(pantalla)
    pygame.display.flip()
    reloj.tick(40)