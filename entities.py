import numpy as np
import random as rd

class sheep() :

    def __init__(self, x,y,energy,age): 
        self.x=x
        self.y=y
        self.energy=energy
        self.age=age
        self.mort=False
        self.repro=False

    """  # Pour savoir si on est sur le bord
    def cases_dispo(self, grid_size):
        if self.x==0:
            if self.y==0:
                return([(0,1),(1,0)])

            if self.y==grid_size[1]:
                return([(0,-1),(1,0)])

            else:
                return([(0,1),(0,-1),(1,0)])

        elif self.x==grid_size[0]:
            if self.y==0:
                return([(0,1),(-1,0)])

            if self.y==grid_size[1]:
                return([(0,-1),(-1,0)])

            else:
                return([(0,1),(0,-1),(-1,0)])

        elif self.y==0:
                return([(0,1),(1,0),(-1,0)])

        elif self.y==grid_size[1]:
                return([(0,-1),(1,0),(-1,0)])

        else:
                return([(0,1),(0,-1),(1,0),(-1,0)])                        

"""
    def Deplacement(self,cases): # cases : liste des cases possibles (tri si grass déjà fait)     
        (self.x,self.y) += rd.choice(cases)
 
    def Alimentation(self): # Lancé par sim 
        self.energy+=10
    
    def Reproduction(self,seuil):  #Seuil à définir dans main
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

    def Deplacement(self,cases): # cases : liste des cases possibles (tri si sheep déjà fait)     
        (self.x,self.y) += rd.choice(cases)

    def Alimentation(self): # Lancé par sim 
        self.energy+=30 

    def Reproduction(self,seuil):  #Seuil à définir dans main
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

    def growing(self):
         self.compt+=1
         if self.compt==7: # Eventuellement l'appeler regrowth_rate et le mettre en cte sur main
              self.state=True
              self.compt=0

        