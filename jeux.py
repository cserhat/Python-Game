import os
from time import sleep
import pygame #importation de la bibliothèque
import pygame.freetype #importation de la bibliothèque
import pygame_menu #importation de la bibliothèque
import random #importation de la bibliothèque
from pygame_menu import sound #importation de la bibliothèque

pygame.init() #initialisation de pygame 
pygame.freetype.init() #initialisation de font 

#DEFINIR LES COULERS

BLACK = (0,0,0) #variable couleur en rgb
WHITE = (255,255,255) #variable couleur en rgb
RED = (255, 0, 0) #variable couleur en rgb

#partie font de score

player_score = 0 #variable pour le score
font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"assets","fonts","ex.ttf") #on indique le chemin de font
font_size = 16 #on definie la taille de font
scorefont = pygame.freetype.Font(font_path, font_size) #on creer une variable pour definier font

#partie l'ecran

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #definir la taille de l'écran
screen.fill(WHITE) #l'arrier plan blanc
pygame.display.update() #mettre a jour l'ecran


#random

#animation de player

class Player(pygame.sprite.Sprite): #on cree un objet qui on va appeler player
    def __init__(self, pos_x, pos_y): 
        super().__init__()
        self.sprite = [] #on creer un tableau qui s'appele sprite 
        self.right = []   #on creer un tableau qui s'appele right 
        self.sprite.append(pygame.image.load('assets/images/idle_0.png'))  #on insér dans le tableau
        self.sprite.append(pygame.image.load('assets/images/idle_1.png'))  #on insér dans le tableau
        self.sprite.append(pygame.image.load('assets/images/idle_2.png'))  #on insér dans le tableau
        self.sprite.append(pygame.image.load('assets/images/idle_3.png'))  #on insér dans le tableau
        self.sprite.append(pygame.image.load('assets/images/idle_4.png'))  #on insér dans le tableau
        self.right.append(pygame.image.load('assets/images/left_0.png'))   #on insér dans le tableau
        self.right.append(pygame.image.load('assets/images/left_1.png'))   #on insér dans le tableau
        self.right.append(pygame.image.load('assets/images/left_2.png'))   #on insér dans le tableau
        self.right.append(pygame.image.load('assets/images/left_3.png'))   #on insér dans le tableau
        self.right.append(pygame.image.load('assets/images/left_4.png'))   #on insér dans le tableau
        self.right.append(pygame.image.load('assets/images/left_5.png'))   #on insér dans le tableau
        self.current_sprite = 0 #initialisation de l'animation
        self.image = self.sprite[self.current_sprite] #image est premier image de l'animation

        self.current_right = 0 #initialisation de l'animation
        self.image = self.right[self.current_right] #image est premier image de l'animation
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.x = pos_x 
        self.y = pos_y

    def move(self): #fonction pour deplacement
        keys = pygame.key.get_pressed() #variable pour detecter le button appui
        if keys[pygame.K_LEFT]: #si on appui fleche gauche
            self.rect.x -= 1
            self.is_animating = False
        if keys[pygame.K_RIGHT]: #si on appui fleche droit
            self.rect.x += 1
            self.right = True
        if keys[pygame.K_UP]: #si on appui fleche haut
            self.rect.y -= 1
            self.is_animating = False
        if keys[pygame.K_DOWN]: #si on appui fleche bas
            self.rect.y += 1
            self.is_animating = False


    def animate(self):
        self.is_animating = True
        
    def update(self, speed): #mettre a jour

        self.current_sprite += speed
        self.current_right += speed
        if self.current_sprite >= len(self.sprite):
            self.current_sprite = 0
            self.is_animating = False
        self.image = self.sprite[int(self.current_sprite)]
        self.move()
        if self.move() == True:

            self.sprite = False
            self.is_animating = False

#afficage de ui (score, vie et temp)

def score(score, healt, time):

    scorefont.render_to(screen, (4,4), "Score: "+str(score), BLACK, None, size= 30)
    scorefont.render_to(screen, (4,35), "Healt: "+str(healt), BLACK, None, size= 30)
    scorefont.render_to(screen, (4,68), "Time: "+str(time), BLACK, None, size= 30)

#parti coin
class Coin(pygame.sprite.Sprite): #on cree un objet qui on va appeler player
    def __init__(self, pos_x, pos_y): 
        super().__init__()
        self.coin = [] #on creer un tableau qui s'appele sprite 
        self.coin.append(pygame.image.load('assets/images/coin_0.png'))  #on insér dans le tableau
        self.coin.append(pygame.image.load('assets/images/coin_1.png'))  #on insér dans le tableau
        self.coin.append(pygame.image.load('assets/images/coin_2.png'))  #on insér dans le tableau
        self.coin.append(pygame.image.load('assets/images/coin_3.png'))  #on insér dans le tableau
        self.coin.append(pygame.image.load('assets/images/coin_4.png'))  #on insér dans le tableau
        self.coin.append(pygame.image.load('assets/images/coin_5.png'))  #on insér dans le tableau
        self.current_coin = 0 #initialisation de l'animation
        self.image = self.coin[self.current_coin] #image est premier image de l'animation

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self):
        self.is_animating = True
        
    def update(self, speed): #mettre a jour

        self.current_coin += speed
        if self.current_coin >= len(self.coin):
            self.current_coin = 0
            self.is_animating = False
        self.image = self.coin[int(self.current_coin)]


class Enemy(pygame.sprite.Sprite): #on cree un objet qui on va appeler player
    def __init__(self, pos_x, pos_y): 
        super().__init__()
        pos_x = 500 
        pos_y = 500
        self.sprite = [] #on creer un tableau qui s'appele sprite 
        self.right = []   #on creer un tableau qui s'appele right 
        self.sprite.append(pygame.image.load('assets/images/enemy.png'))  #on insér dans le tableau
        self.sprite.append(pygame.image.load('assets/images/enemy_1.png'))  #on insér dans le tableau
        self.sprite.append(pygame.image.load('assets/images/enemy_2.png'))  #on insér dans le tableau
        self.sprite.append(pygame.image.load('assets/images/enemy_3.png'))  #on insér dans le tableau
        self.sprite.append(pygame.image.load('assets/images/enemy_4.png'))  #on insér dans le tableau
        self.sprite.append(pygame.image.load('assets/images/enemy_5.png'))  #on insér dans le tableau
        self.current_sprite = 0 #initialisation de l'animation
        self.image = self.sprite[self.current_sprite] #image est premier image de l'animation

        self.current_right = 0 #initialisation de l'animation
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.x = pos_x 
        self.y = pos_y


    def animate(self):
        self.is_animating = True
        
    def update(self, speed): #mettre a jour

        self.current_sprite += speed
        if self.current_sprite >= len(self.sprite):
            self.current_sprite = 0
            self.is_animating = False
        self.image = self.sprite[int(self.current_sprite)]
#Gamehelp 

def gamehelp():
    HELP = "How to play? \n"\
       "I don't know how to play this game. \n"\
       "Just enjoy\n"\
       "^-^ \n"
    menu.add.label(HELP, max_char=-1, font_size=20)
    pass

#partie fin de jeux
def endgame():
    
    pass

#jeux

def start_the_game(): #on définie le jeux (fonction)
    running= True
    pygame.display.set_caption("Sprite Animation")
    moving_sprite = pygame.sprite.Group()
    moving_coin = pygame.sprite.Group()
    player = Player (100, 100)
    enemy = Enemy (100, 100)
    pos_x = random.randint(0,600)
    pos_y = random.randint(0,600)
    coin = Coin(int(pos_x), int(pos_y))
    moving_sprite.add(player)
    moving_sprite.add(enemy)
    moving_coin.add(coin)
    start_ticks=pygame.time.get_ticks()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        seconds=(pygame.time.get_ticks()-start_ticks)/1000 #on calcule le temps ecoulé
        timegame = 60 #la duree
        countdown = timegame - seconds
        if countdown == 0:
            break
        score(player_score,100,int(countdown)) #on affiche le score,la vie et le temps
        moving_sprite.draw(screen) 
        moving_coin.draw(screen)
        
        for x in range(100):
            pos_y += 100 
            pos_x += 100 
            moving_coin.update(0.030)

        moving_sprite.update(0.030)
        pygame.display.flip()
        screen.fill(WHITE)
    pass


#menu

engine = sound.Sound()
engine.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, './assets/sounds/click.ogg')
engine.set_sound(sound.SOUND_TYPE_OPEN_MENU, './assets/sounds/open.ogg')
engine.set_sound(sound.SOUND_TYPE_CLOSE_MENU, './assets/sounds/click.ogg')

menu = pygame_menu.Menu('SGameDev', 1280, 720,
                       theme=pygame_menu.themes.THEME_DARK) #on définie la taille et le thème du menu 
menu.add.button('Play', start_the_game) #on ajoute le button
menu.add.button('Help', gamehelp) #on ajoute le button
menu.add.button('Option') #on ajoute le button
menu.add.button('Quit', pygame_menu.events.EXIT)  #on ajoute le button
menu.set_sound(engine, recursive=True) 
menu.mainloop(screen) #on met le menu dans la boucle

