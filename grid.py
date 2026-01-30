import numpy as np
import pyxel
import random as rd


GRID_SIZE=30
INITIAL_SHEEP=50
INITIAL_WOLF=10
INITIAL_GRASS_COVERAGE=30

class wolf:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class sheep:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class grass:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class grid:
    def __init__(self):
        self.damier = []
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if (i + j) % 2 == 0:
                    self.damier.append((i, j))

        self.is_wolf=[]
        self.is_sheep=[]
        self.is_grass=[]

        while len(self.is_grass) < np.floor(INITIAL_GRASS_COVERAGE*GRID_SIZE**2/100):
            x1, y1 =rd.randint(0,GRID_SIZE), rd.randint(0,GRID_SIZE)
            if grass(x1,y1) not in self.is_grass:
                self.is_grass += [grass(x1, y1)]

        while len(self.is_sheep) < INITIAL_SHEEP:
            x1, y1=rd.randint(0,GRID_SIZE), rd.randint(0,GRID_SIZE)
            if sheep(x1, y1) not in self.is_sheep:
                self.is_sheep += [sheep(x1, y1)]

        while len(self.is_wolf) < INITIAL_WOLF:
            x1, y1=rd.randint(0,GRID_SIZE), rd.randint(0,GRID_SIZE)
            if wolf(x1, y1) not in self.is_wolf and sheep(x1,y1) not in self.is_sheep:
                self.is_wolf += [wolf(x1, y1)]

        pyxel.init(GRID_SIZE, GRID_SIZE, title="Simulation")
        
        
    def remove_wolf(self, pos): # pos est un couple (x,y)
        for elt in self.is_wolf:
            if (elt.x,elt.y)==pos:
                self.is_wolf.remove(elt)

    def remove_sheep(self, pos):
        for elt in self.is_sheep:
            if (elt.x,elt.y)==pos:
                self.is_sheep.remove(elt)
    




    # fonction qui renvoie les déplacement intéressants en fonction de la position de l'herbe
    # renvoie les déplacements dans les 4 directions si pas d'herbe autour
    def where_grass(self,x,y):
        list_grass = []
        for i in [-1,1] :
            if self[x+i][y].isinstance(grass):   
                list_grass.append([i,0])
        for j in [-1,1] :
            if self[x][y+j].isinstance(grass):   
                list_grass.append([0,j])

        if list_grass == []:
            return [(-1,0),(1,0),(0,-1),(0,1)]
        return list_grass

    # idem pour les moutons
    def where_sheep(self,x,y):
        list_sheep = []
        for i in [-1,1] :
            if self[x+i][y].isinstance(sheep):   
                list_sheep.append([i,0])
        for j in [-1,1] :
            if self[x][y+j].isinstance(sheep):   
                list_sheep.append([0,j])

        if list_sheep == []:
            return [(-1,0),(1,0),(0,-1),(0,1)]
        return list_sheep



    # fonction d'action pour update la grille
    
    def aging_sheep(self):
        L = self.is_sheep
        return [animal.aging() for animal in L]
    
    def aging_wolf(self):
        L = self.is_wolf
        return [animal.aging() for animal in L]
                

    def phase_moutons(self):
        # on supprime l'herbe là où se trouvent des moutons
        for s in self.is_sheep : 
            self.remove_grass(s.x,s.y)
            cases = self.where_grass(s.x,s.y)
            s.deplacement(cases)

    def phase_loups(self):
        # on supprime les moutons là où se trouvent des loups
        for w in self.is_wolf : 
            self.remove_sheep(w.x,w.y)
            cases = self.where_grass(w.x,w.y)
            w.deplacement(cases)

    def update_grass(self):
        for g in self.is_grass :
            g.growing()

    def update_dead(self):
        # on parcourt les loups existants et regarde si ils meurent
        for w in self.is_wolf : 
            w.meurt()
            if w.mort :
                self.is_wolf.remove(v)
        # idem pour les moutons
        for s in self.is_sheep : 
            s.meurt()
            if s.mort :
                self.is_sheep.remove(v)


    def reproduction(self):
        # on parcourt les mouons et regartde si le booléen de reproduction est vrai
        for s in self.is_sheep :
            s.Reproduction()
            if s.repro :
                self.is_sheep.append(sheep(x=s.x,y=s.y,energy = 40,age=0))
                s.repro = False
        # idem pour les loups
        for w in self.is_wolf :
            w.Reproduction()
            if w.repro :
                self.is_sheep.append(wolf(x=w.x,y=w.y,energy = 40,age=0))
                w.repro = False




    def draw(self):
        pyxel.cls(15)
        for x, y in self.damier:
            pyxel.rect(x, y, 1, 1, 4)
        for tile in self.is_grass:
            pyxel.rect(tile.x,tile.y,1,1,3)
        

    def start(self):
        pyxel.run(self.update, self.draw)



grid().start()

        

