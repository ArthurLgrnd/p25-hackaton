import numpy as np
import random as rd



class sheep :
    
    def __init__(self, x,y,energy,age,is_grass): # is_grass: pos des herbes adjacentes
        self.x=x
        self.y=y
        self.energy=energy
        self.age=age
        self.mort=False
        self.repro=False
    
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


    def Deplacement(self,grid_size): # ATTENTION potentielle redondance avec Simulation, format liste (xmax,ymax)          
        
        
        cases_possibles=cases_dispo(self,grid_size)
        (dx,dy)=rd.choice(cases_possibles)
        self.x+=dx
        self.y+=dy
    
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
              


        
class wolf :
    
    def __init__(self,position,energy,age,):
        self.x=x
        self.y=y
        self.energy=energy
        self.age=age
        self.mort=False
        self.repro=False





class grass :
    
    def __init__(self,
                 state,
                 regrowth_rate,      
    ):
        