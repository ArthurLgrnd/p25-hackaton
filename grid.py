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

        def remove_grass(self, pos):
            for elt in self.is_grass:
                if (elt.x,elt.y)==pos:
                    self.is_grass.remove(elt)        

    def draw(self):
        pyxel.cls(15)
        for x, y in self.damier:
            pyxel.rect(x, y, 1, 1, 4)
        for tile in self.is_grass:
            pyxel.rect(tile.x,tile.y,1,1,3)
        

    def update(self):
        pass

    def start(self):
        pyxel.run(self.update, self.draw)



grid().start()

        

