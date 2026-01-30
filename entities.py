import numpy as np
import random as rd
import pyxel


TILE=16


class sheep() :

    def __init__(self, x,y,energy,age): 
        self.x=x
        self.y=y
        self.energy=energy
        self.age=age
        self.mort=False
        self.repro=False

    def draw(self):
        pyxel.blt(self.x*TILE, self.y*TILE, 0, 0, 0, 16, 16, 0)


    """  # Pour savoir si on est sur le bord
    def cases_dispo(self, grid_size):
        if self.x==0:
            if self.y==0:
                return([(0,1),(1,0)])

            if self.y==GRID_SIZE:
                return([(0,-1),(1,0)])

            else:
                return([(0,1),(0,-1),(1,0)])

        elif self.x==GRID_SIZE:
            if self.y==0:
                return([(0,1),(-1,0)])

            if self.y==GRID_SIZE:
                return([(0,-1),(-1,0)])

            else:
                return([(0,1),(0,-1),(-1,0)])

        elif self.y==0:
                return([(0,1),(1,0),(-1,0)])

        elif self.y==GRID_SIZE:
                return([(0,-1),(1,0),(-1,0)])

        else:
                return([(0,1),(0,-1),(1,0),(-1,0)])                        

"""
    #def deplacement(self,cases): # cases : liste des cases possibles (tri si grass déjà fait)     
            #(self.x,self.y) += rd.choice(cases)
 
    def alimentation(self): # Lancé par sim 
        self.energy+=10
    
    def reproduction(self,seuil):  #Seuil à définir dans main
         if self.energy > seuil:
              self.energy-=20
              self.repro=True 
# ATTENTION: il faut que Simulation créée un nv mouton avec 20 d'energie et mette repro à False
    
    def meurt(self,age_limite):  # Âge limite à définir dans simulation
         if self.energy<=0 or self.age > age_limite:
              self.mort=True
    
    def aging(self):
         self.age+=1
              

class wolf() :
    
    def __init__(self,x,y,energy,age): 
        self.x=x
        self.y=y
        self.energy=energy
        self.age=age
        self.mort=False
        self.repro=False  

    def draw(self):
        pyxel.blt(self.x*TILE, self.y*TILE, 1, 0, 0, 16, 16, 0)           

    #def Deplacement(self,cases): # cases : liste des cases possibles (tri si sheep déjà fait)     
        #(self.x,self.y) += rd.choice(cases)

    def alimentation(self): # Lancé par sim 
        self.energy+=30 

    def reproduction(self,seuil):  #Seuil à définir dans main
         if self.energy > seuil:
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

        