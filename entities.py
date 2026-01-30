import numpy as np
import random as rd
import pyxel

GRID_SIZE = 30
TILE = 16

INITIAL_SHEEP = 50
INITIAL_WOLF = 10
INITIAL_GRASS_COVERAGE = 30
SHEEP_INITIAL_ENERGY = 20
WOLF_INITIAL_ENERGY = 40
SHEEP_ENERGY_FROM_GRASS = 15
WOLF_ENERGY_FROM_GRASS = 35
SHEEP_ENERGY_LOSS_PER_TURN = 1
WOLF_ENERGY_LOSS_PER_TURN = 2

SHEEP_REPRODUCTION_THRESHOLD = 50
WOLF_REPRODUCTION_THRESHOLD = 80
REPRODUCTION_ENERGY_COST = 20

SHEEP_MAX_AGE = 40
WOLF_MAX_AGE = 50

GRASS_GROWTH_PROBABILITY = 0.08
GRASS_REGROWTH_TIME = 7

class sheep() :

    def __init__(self, x,y,energy,age,energy_seuil=SHEEP_REPRODUCTION_THRESHOLD): 
        self.x=x
        self.y=y
        self.energy=energy
        self.age=age
        self.energy_seuil = energy_seuil
        self.mort=False
        self.repro=False

    def draw(self):
        pyxel.blt(self.x*TILE, self.y*TILE, 0, 0, 0, 16, 16, 0)


    def deplacement(self,cases): # cases : liste des cases intéressantes à voir (priorité aux ressources)  
        new_x,new_y = (self.x,self.y) + rd.choice(cases)
        if 0<= new_x < 50 and 0<= new_y < 50 :
            (self.x,self.y) = (new_x,new_y)
        # on suppose ici que si l'animal veut se déplacer aléatoirement en dehors de la grille , il s'arrete...  
    
    def alimentation(self): # Lancé par sim 
        self.energy += 10
    
    def reproduction(self):  #Seuil à définir dans main
        if self.energy > self.energy_seuil:
            self.energy -= REPRODUCTION_ENERGY_COST
            self.repro=True 
# ATTENTION: il faut que Simulation créée un nv mouton avec 20 d'energie et mette repro à False
    
    def meurt(self,age_limite):  # Âge limite à définir dans simulation
        if self.energy<=0 or self.age > age_limite:
            self.mort=True
    
    def aging(self):
        self.age+=1
              

class wolf() :
    
    def __init__(self,x,y,energy,age,energy_seuil = WOLF_REPRODUCTION_THRESHOLD): 
        self.x=x
        self.y=y
        self.energy=energy
        self.age=age
        self.mort=False
        self.repro=False              
        self.energy_seuil = energy_seuil

    def draw(self):
        pyxel.blt(self.x*TILE, self.y*TILE, 1, 0, 0, 16, 16, 0)           

    def deplacement(self,cases): # cases : liste des cases intéressantes à voir (priorité aux ressources)  
        while pas == False:
            new_x, new_y = (self.x,self.y) + rd.choice(cases)
            if 0<= new_x < 50 and 0<= new_y < 50 :
                (self.x,self.y) = (new_x,new_y)
                pas = True
        # on suppose ici que si l'animal veut se déplacer aléatoirement en dehors de la grille , il s'arrete...  

    def alimentation(self): # Lancé par sim 
        self.energy+=30 

    def reproduction(self):  #Seuil à définir dans main
        if self.energy > self.energy_seuil:
            self.energy-=20
            self.repro=True 
# ATTENTION: il faut que Simulation créée un nv loup avec 40 d'energie et mette repro à False

    def meurt(self,age_limite):  # Âge limite à définir dans simulation
        if self.energy<=0 or self.age > age_limite:
            self.mort=True  

    def aging(self):
        self.age+=1 

class grass() :
    
    def __init__(self,x,y,state): # eventuellement retirer x et y
        self.x=x
        self.y=y
        self.state=state # Bool
        self.compt=0

    def draw(self):
         pyxel.rect(self.x*TILE, self.y*TILE, TILE, TILE, 3 if self.state == True else 15)

    def growing(self):
        self.compt+=1
        if self.compt==7: # Eventuellement l'appeler regrowth_rate et le mettre en cte sur main
            self.state=True
            self.compt=0

        