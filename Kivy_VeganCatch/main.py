from kivy.app import App
from kivy.core.window import Window
from kivy.core.window import WindowBase
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
#Nombres aleatoires:
import random

#On declare deux ecrans 'Menu' et 'Game'
class MenuScreen(Screen):
    def build(self):
        self.name='Menu'#On donne un nom a l'ecran
        #Une image de fond:
        self.add_widget(Image(source='land.png',allow_stretch=True,keep_ratio=False))
        #On definie un layout pour cet ecran:
        Menu_Layout = BoxLayout(padding=100,spacing=10,orientation='vertical')
        #On cree un bouton pour lancer le jeu:
        self.Bouton_Jeu=Button(text='Jouer!')
        self.Bouton_Jeu.font_size=Window.size[0]*0.05
        self.Bouton_Jeu.background_color=[0,0,0,0.2]
        self.Bouton_Jeu.bind(on_press=self.Vers_Game)
        #On ajoute le bouton dans l'affichage:
        Menu_Layout.add_widget(self.Bouton_Jeu)
        #On cree un bouton qui ne fait rien pour l'instant:
        self.Bouton_Rien=Button(text='Je ne fais rien !')
        self.Bouton_Rien.font_size=Window.size[0]*0.05
        self.Bouton_Rien.background_color=[0,0,0,0.2]
        self.Bouton_Rien.bind(on_press=self.Vers_Rien)
        #On ajoute le bouton dans l'affichage:
        Menu_Layout.add_widget(self.Bouton_Rien)
        #On ajoute ce layout dans l'ecran:
        self.add_widget(Menu_Layout)

    def Vers_Game(self,instance):#Fonction de transition vers 'Game'
        Game=GameScreen()
        Game.build()#On construit l'ecran 'Game'
        sm.add_widget(Game)#On ajoute l'ecran dans le screen manager
        sm.current='Game'#On definit 'Menu' comme ecran courant

    def Vers_Rien(self, instance):
        pass

class GameScreen(Screen):
    def build(self):
        self.name='Game'#On donne un nom a l'ecran
        Game_Layout=Jeu()#Creation du jeu
        Game_Layout.debut()#Initialisation du jeu
        self.add_widget(Game_Layout)#On l'ajoute dans l'ecran

class Carotte(Widget):
    def __init__(self,canvas):
        self.dy=-10
        self.canvas=canvas
        #Taille et position aleatoire:
        self.size=(Window.size[0]*0.05,Window.size[1]*0.1)
        self.x = random.randint(0,int(Window.size[0]-self.size[0]))
        self.y=Window.size[1]-100
        #Ajout de l'image du Carotte:
        with self.canvas:
            self.dessin = Rectangle(source='Carotte.png',size=self.size, pos=self.pos)
        #Detection des mouvements:
        self.bind(pos=self.update_canvas)

    def update_canvas(self, *args):#Mise a jour des positions de l'image:
        self.dessin.pos = self.pos

    def move(self):
        #On recalcule les positions:
        self.y=self.y+self.dy
        #On teste la fin de la chute:
        if self.y<=0-self.size[1]:
            #Repositionnement aleatoire en haut:
            self.y=Window.size[1]
            self.x=random.randint(0,int(Window.size[0]-self.size[0]))

    def prise(self):#Changement d'image pour le succes:
        self.dy=0#On stoppe la chute
        #Position au dessus du hippie pour stopper la collision:
        self.y=Window.size[1]*0.2
        #On lance le nouveau Carotte dans 0.5 seconde:
        Clock.schedule_once(self.prise_fin, 0.5)

    def prise_fin(self,dt):#Retour a l'image de Carotte et en haut:
        self.y=0-self.size[1]#On le place en dessous pour qu'il remonte
        self.dessin.source='Carotte.png'   #On change l'image
        self.dy=-10    #On relance la chute

class hippie(Widget):
    def __init__(self,canvas):
        self.canvas=canvas
        #Taille et position:
        self.size=(Window.size[0]*0.20,Window.size[1]*0.20)
        self.pos=(0,Window.size[1]*0.02)
        #Ajout de l'image (add_wiget fonctionne aussi):
        with self.canvas:
            self.dessin = Rectangle(source='hippie.png',size=self.size, pos=self.pos)
        #On associe le mouvement du hippie et son image:
        self.bind(pos=self.update_canvas)

    def update_canvas(self, *args):#Mise a jour des positions de l'image:
        self.dessin.pos = self.pos

class Jeu(FloatLayout):
    def debut(self):
        #On recupere la taille de l'ecran:
        self.size=Window.size
        #Une image de fond:
        self.add_widget(Image(source='fond1.jpg',allow_stretch=True,keep_ratio=False))

        #Un label pour le score:
        self.score=0#Creation de la variable score
        self.label=Label(text='Score : '+str(self.score),markup=True)
        #Taille de la police en fonction de l'ecran:
        self.label.font_size=self.size[0]*0.05
        #Le label ne doit pas ecraser tout l'ecran:
        self.label.size_hint=(None,None)
        #Position du label vers le centre de l'ecran:
        self.label.pos=(Window.size[0]*0.47,Window.size[1]*0.45)
        self.label.color=[0,0,0,1]
        #On ajoute le label dans l'ecran du jeu:
        self.add_widget(self.label)

        #Creation du hippie:
        self.hippie=hippie(self.canvas)
        #Creation des Carotte:
        self.Carotte=[]
        for i in range(0,5):#On ajoute les Carotte
            self.Carotte.append(Carotte(self.canvas))

        #Creation des chiffres pour de depart:
        self.compteur_anim=3
        self.chiffre=Image(source='3.png',allow_stretch=True,keep_ratio=False)
        self.chiffre.size_hint=(0,0)
        self.chiffre.pos=self.center
        self.add_widget(self.chiffre)
        #Lancement de l'animation start:
        self.animation_start()

        #Depart de l'horloge du jeu:
        Clock.schedule_interval(self.update_chute, 4.0/100.0)

    def update_chute(self,dt):#Chute des Carotte et tests de collisions
        for Carotte in self.Carotte:
            Carotte.move()
            if Carotte.collide_widget(self.hippie):
                    Carotte.prise()#Animation de la capture
                    self.score+=1
                    self.label.text='Score : '+str(self.score)


    def on_touch_move(self,touch):#Deplacement du hippie
        if touch.y<self.size[1]/3:
            self.hippie.center_x=touch.x

    def animation_start(self):#Depart de l'animation start
        #On compose l'animation avec deux anim successives:
        anim = Animation(pos=(0,0),size=self.size,t='in_quad',duration=0.8)
        anim += Animation(pos=self.center,size=(0,0),duration=0.8)
        #On prevoie de lancer le prochain chiffre a la fin de l'animation:
        anim.bind(on_complete=self.animation_next)
        #Depart de l'animation:
        anim.start(self.chiffre)

    def animation_next(self,animation,widget):#Animation suivante:
        self.compteur_anim-=1
        if self.compteur_anim==0:
            self.remove_widget(self.chiffre)
        else:
            self.chiffre.source=str(self.compteur_anim)+'.png'
            self.animation_start()

# Creation du screen manager
sm = ScreenManager()

class CarotteApp(App):
    def build(self):
        Menu=MenuScreen()#Creation de l'ecran 'Menu'
        Menu.build()#Construction de l'ecran 'Menu'
        #On ajoute l'ecran dans le screen manager
        sm.add_widget(Menu)
        sm.current='Menu'#On definit 'Menu' comme ecran courant
        return sm #On envoie le screen manager pour affichage

if __name__ == '__main__':
    CarotteApp().run()
