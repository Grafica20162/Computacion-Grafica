#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame,levels
from player import Player
from FilesLoader import *
from menu import *
from introduccion import pausa

#--Images and Sounds Files:
images = None
sounds = None
#--------------------------
# Screen dimensio=ns:
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
#=======================================================================
#.............................Main Class................................
class Game(object):
    running = False
    quitGame = False
    win_message = False
    #quitPause = False
    lives = 3
    
    help_menu = False
    game_over = False
    about_menu=False
    
    def __init__(self,screen):
        # Load images
        global images
        images = loadImages()
        #Load sounds Effects
        global sounds
        sounds = loadSounds()
        # Ojbects
        self.player = Player((93,324),images,sounds)
        self.playerSprite = pygame.sprite.Group()
        self.playerSprite.add(self.player)
        # -------------------
        self.levelList = []
        self.levelList.append(levels.Level_One(images,sounds,self.player,screen))
        self.levelList.append(levels.Level_Two(images,sounds,self.player,screen))
        self.currentLevel = 0
        self.level = self.levelList[self.currentLevel]
        self.level.load_music()
        self.player.level = self.level
        #--------------------------------------------------------------
        self.text_font = pygame.font.Font("game_files/FreeSansBold.ttf",25)
        #Create menu object:
        self.menu = Menu(screen,("Jugar","Instrucciones","Salir"),ttf_font="game_files/FreeSansBold.ttf",
                                font_color=(128,128,255),bg_image=images["introd"],font_size=38)
        self.screen = screen
    def run_logic(self):
        if self.running:
            if not self.player.game_over:
                self.level.update()
                # See if we have to shift the levels   
                limit_left =  self.level.limit_left()
                x = self.player.rect.x
                if  limit_left and x > SCREEN_WIDTH - 215:
                    if self.currentLevel < len(self.levelList) -1:
                        pygame.mixer.music.stop()
                        self.player.rect.center = (93,324)
                        self.currentLevel += 1
                        self.level = self.levelList[self.currentLevel]
                        self.level.load_music()
                        self.player.level = self.level
                        pygame.mixer.music.play(-1)
                    else:
                        pygame.mixer.music.stop()
                        self.player.image = images["playerFront"]
                        self.win_message = True
            else:
                if self.lives == 0:
                    self.running = False
                    self.game_over = True
                else:
                    self.lives -= 1
                    self.__init__(self.screen)
                    pygame.mixer.music.play(-1)
    #-------------------------------------------------------------------
    def displayFrame(self,screen):
        if self.running:
            self.level.draw(screen)
            self.playerSprite.draw(screen)
            
            screen.blit(images["hud_hear"],(3,8))
            screen.blit(images["hud_x"],(40,8))


            screen.blit(images["hud_p3Alt"],(5,40))
            screen.blit(images["hud_x"],(40,45))

            if self.lives == 3:
                screen.blit(images["hud_3"],(70,40))
            elif self.lives == 2:
                screen.blit(images["hud_2"],(70,40))
            elif self.lives == 1:
                screen.blit(images["hud_1"],(70,40))
            else:
                screen.blit(images["hud_0"],(70,40))
                
            screen.blit(images["hud_coin"],(165,5))
            screen.blit(images["hud_x"],(200,8))
            
            lives = str(self.player.lives)
            if len(lives) < 2:
                lives = "0" + lives 

            i = 50
            for m in lives:
                screen.blit(self.number_image1(int(m)),(20+i,5))
                i += 35
            
            # draw the number of coins collected: ----------------------
            coins = str(self.player.coins)
            if len(coins) < 2:
                coins = "0" + coins
            i = 50
            for n in coins:
                screen.blit(self.number_image(int(n)),(180+i,5))
                i += 35

            gem = str(self.player.coins)
            if len(gem) < 2:
                gem = "0" + gem
            i = 50
            for n in gem:
                screen.blit(self.number_image(int(n)),(180+i,5))
                i += 35
            # ----------------------------------------------------------
            text = self.text_font.render("Nivel:",True,(255,215,0))
            screen.blit(text,(334,5)) 
            screen.blit(self.number_image(self.currentLevel +1),(400,7))
            
            if self.win_message:
                text = self.text_font.render("¡Lo lograste!",True,(128,128,255))
                screen.blit(text,(100,200))
                pygame.display.flip() 
                pygame.time.wait(3000)
                self.running = False
                self.win_message = False
        elif self.about_menu:
            
            #fondo = pygame.image.load("game_files/instrucciones.png").convert()
            self.screen.blit(images["instrucciones"],(0,0))


        elif self.game_over:
            self.screen.blit(images["background"],(0,0))
            text = self.text_font.render("GAME OVER",True,(128,128,255))
            screen.blit(text,(250,125))
            text = self.text_font.render("Presiona SCP para regresar al menu",True,(128,128,255))
            screen.blit(text,(30,300)) 
        else:
            self.menu.display_frame()
    #-------------------------------------------------------------------
    def number_image(self,n):
        """ return a image with the number given in it. """
        if n == 1:
            return images["hud_1"]
        elif n == 2:
            return images["hud_2"]
        elif n == 3:
            return images["hud_3"]
        elif n == 4:
            return images["hud_4"]
        elif n == 5:
            return images["hud_5"]
        elif n == 6:
            return images["hud_6"]
        elif n == 7:
            return images["hud_7"]
        elif n == 8:
            return images["hud_8"]
        elif n == 9:
            return images["hud_9"]
        else:
            return images["hud_0"]

        #_____________________________
    def number_image1(self,m):
        if m== 1:
            return images["hud_1"]
        elif m == 2:
            return images["hud_2"]
        elif m == 3:
            return images["hud_3"]
        elif m == 4:
            return images["hud_4"]
        elif m == 5:
            return images["hud_5"]
        elif m == 6:
            return images["hud_6"]
        elif m == 7:
            return images["hud_7"]
        elif m == 8:
            return images["hud_8"]
        elif m == 9:
            return images["hud_9"]
        else:
            return images["hud_0"]
    #-------------------------------------------------------------------
    def eventHandler(self):
        flag = False
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                flag = True # Flag that we are done so we exit this loop
                pygame.mixer.music.stop()
            #---------KEY DOWN EVENTS-----------------------------------
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move_left()


                elif event.key == pygame.K_RIGHT:
                    self.player.move_right()
                    
                elif event.key == pygame.K_UP:
                    if self.running:
                        self.player.jump()

                elif event.key == pygame.K_DOWN:
                    if self.running:
                        self.player.down()
                elif event.key== pygame.K_p:
                    pausa()

                elif event.key == pygame.K_ESCAPE:
                    if self.running:
                        self.running = False
                        pygame.mixer.music.stop()
                    self.lives = 3
                    self.help_menu = False
                    self.game_over = False
                    self.about_menu=False
                elif event.key == pygame.K_RETURN and not self.running:
                    if not self.about_menu and not self.game_over:
                        if self.menu.state == 0:
                            self.__init__(self.screen)
                            self.lives = 3
                            self.running = True
                            pygame.mixer.music.play(-1)
                        
                        elif self.menu.state == 1:
                            self.about_menu = True
                            
                        else:
                            self.quitGame = True
                        
                if not self.running:
                    self.menu.event_handler(event)
            #---------KEY UP EVENTS-------------------------------------
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.stop()
                elif event.key == pygame.K_RIGHT:
                    self.player.stop()
            
            
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                print (self.player.rect.left + abs(self.level.world_shift[0]),
                        self.player.rect.top - (500 - abs(self.level.world_shift[1])))
            if self.quitGame:
                flag = True

        return flag
