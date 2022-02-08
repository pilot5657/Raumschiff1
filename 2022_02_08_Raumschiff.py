from cmath import cos, sin
from tkinter import CENTER
from turtle import up
import pygame
import time 
from pygame import constants 
from pygame.constants import(QUIT,KEYDOWN,KEYUP,K_ESCAPE,K_TAB,K_KP_PLUS,K_KP_MINUS,K_F10,K_LEFT,K_RIGHT,K_UP,K_DOWN,K_SPACE,MOUSEBUTTONDOWN) # importierung der Knoepfe /import of buttons
import os
import random

class Settings:
    screen_width = 800
    screen_height = 500 
    inner_rect = pygame.Rect(
    100, 100, screen_width - 200, screen_height - 200)
    fps = 60 
    pygame.display.set_caption("Raumschiff-Game") 
    file_path = os.path.dirname(os.path.abspath(__file__)) 
    image_path = os.path.join(file_path,"images") 
    def get_dim():
        return (Settings.screen_width, Settings.screen_height)

        
        
class Background(pygame.sprite.Sprite): 
    def __init__(self, filename):
        super().__init__() 
        self.image = pygame.image.load(os.path.join(Settings.image_path, filename)).convert() 
        self.rect = pygame.transform.scale(self.image,Settings.get_dim()) 
        self.rect = self.image.get_rect() 

    def draw(self,screen): 
        screen.blit(self.image,self.rect)  



class Raumschiff(pygame.sprite.Sprite): #  Hauptklasse Jet / Main Class Jet
    def __init__(self, filename):  # Definiert die Funktion  (self,filename) / Define the function (self,filename)
        self.image = pygame.image.load(os.path.join(Settings.image_path, filename)).convert_alpha() # Ladet das PNG.Image in die Klasse Hintergrund rein /# Load the PNG. Image in the Background class  
        self.rect = self.image.get_rect() # Gibt Informationen ueber die Position und Größe des Rechtecks zurueck / returns information about the position and size of the rectangle
        self.rect.top  = 400  # Die Position der Hoehe / The position of the height
        self.rect.left = 400 # Die Position Links / The position Links
        self.time_jump = 3000 # Wann wieder gesprungen werden kann / When  do you can jump 
        self.time_optional_jump = pygame.time.get_ticks()  # Wohin wird gesprungen / Where do you jump
        self.speed_x =  0 # Geschwindigkeit Vertikal / Speed Vertical
        self.speed_y =  0 # Geschwindigkeit Horisontal / Speed Horizontal
        self.speed = 5 # Geschwindigkeit / Speed 
        self.radius = 0 # Legt den Radius fest / Sets the radius
        interval = [-10,10]
        self.angle(angle=0)
        self.direction_h = 0 # Richtung Horisontal /  Direction Horisontal
        self.direction_v =  0  # Richtung Vertikal /  Direction Vertical
    



      
    def draw(self,screen): # Zeichnet das Foto im Bildschirm ein / Enter the photo on the screen
         screen.blit(self.image,self.rect)


    
    

    #pygame.transform.rotate()
    def move_stop(self): # Nach dem Bewegen komme zum stehen / After moving, come to a standstill
        self.speed_h = self.speed_v = 0 # Berechnungs Koordina    ten/  Calculation coordinates
    
    def move_left(self):  # Bewege dich nach links /  Move to the left
        self.image =   pygame.transform.rotate(self.image,22.5)


    def angle(self,angle):
        self.speed_x = self.speed_x - sin(angle)
        self.speed_y = self.speed_y - cos(angle)
      
        
 
     
        
    
    def move_right(self): # Bewege dich nach rechts /  Move to the right
       self.image =   pygame.transform.rotate(self.image,22.5)
      

    
    def move_up(self,angle):  # Bewege dich  zurück /  Move to the back
        self.speed_x = self.speed_x - sin(angle)
        self.speed_y = self.speed_y - cos(angle)



    def update(self): #  aktualisiere / Update 
      self.rect = self.rect.move(self.speed_h,self.speed_v)
       

       




class Game(object): 
    def __init__(self):
        pygame.init() # 
        self.screen = pygame.display.set_mode(Settings.get_dim()) #Dimme den Bildschirm /  Dim the  Display
        self.clock = pygame.time.Clock() # Es wird  die Zeit im spiel eingefuegt = The time is inserted into the game
        self.background = Background("2021_11_17_Sternen_Himmel.png") # Ladet das Foto in der Klasse Hintergrund rein /Loads the photo in the Background class
        self.raumschiff = Raumschiff("2022_02_08_Raumschiff.png")

    
          
    def watch_for_events(self):
        for event in pygame.event.get():                               
            if event.type == QUIT:                                  
                 self.running = False                                 # Fenster wird zum schließen aufgefordert
            elif event.type == KEYDOWN:                              #                         gedrükt
                if event.key == K_ESCAPE:                            # Wenn die Escape Taste            wurde
                    self.running = False                             # setzt self.running auf False. Damit wird es weiter unten zum schließen aufgefordert
                elif event.key == K_LEFT:                            # Bei Tastendruck von Pfeiltaste links
                    self.raumschiff.move_left()                          # Käfer läuft nach links
                elif event.key == K_RIGHT:                           # Bei Tastendruck von Pfeiltaste rechts
                    self.raumschiff.move_right()                         # Käfer läuft nach rechts                                      # Käfer springt zu einem zufälligen Ort -> Zugriff auf def jump
            elif event.type == KEYUP:                                # Beim loslassen der Pfeiltasten
                if event.key == K_LEFT or event.key == K_RIGHT or event.key == K_UP or event.key == K_DOWN: 
                    self.raumschiff.move_stop()   

         

                    self.raumschiff.update()
                    pygame.display.flip()
  

                      
           
    def draw(self): # Die Funktion Zeichne / The Draw function
        self.background.draw(self.screen) # Zeichne den Hintergrund Fenster / Draw the background on the windows
        self.raumschiff.draw(self.screen)
        pygame.display.flip() # Aktualisiert nur einen bestimmten Bereich / Updates only a specific area

        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(Settings.get_dim())
      #  self.raumschiff = pygame.sprite.GroupSingle(Raumschiff())


    def run(self): 
        self.running = True
        while self.running:
            self.clock.tick(Settings.fps) 
            self.watch_for_events() 

            self.draw() 
  
if __name__ == '__main__': 
    os.environ['SDL_VIDEO_WINDOW_POS'] = "10, 30"

    game = Game()
    game.run() 