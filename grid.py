import numpy as np
import pyxel
import random as rd


GRID_SIZE=30
INITIAL_SHEEP=50
INITIAL_WOLF=10
INITIAL_GRASS_COVERAGE=30

class grid:
    def __init__(self):
        
        self.is_wolf=[]
        self.is_sheep=[]
        self.is_grass=[]

        while len(self.is_grass) < np.floor(INITIAL_GRASS_COVERAGE*GRID_SIZE**2/100):
            Tile=(rd.randint(0,GRID_SIZE),rd.randint(0,GRID_SIZE))
            if grass(Tile) not in self.is_grass:
                self.is_grass += grass(Tile)

        while len(self.is_sheep) < INITIAL_SHEEP:
            Tile=(rd.randint(0,GRID_SIZE),rd.randint(0,GRID_SIZE))
            if sheep(Tile) not in self.is_sheep:
                self.is_grass += sheep(Tile)

        while len(self.is_wolf) < INITIAL_WOLF:
            Tile=(rd.randint(0,GRID_SIZE),rd.randint(0,GRID_SIZE))
            if wolf(Tile) not in self.is_wolf:
                self.is_wolf += wolf(Tile)
        
        def remove_wolf(self, pos): # pos est un couple (x,y)
            for elt in self.is_wolf:
                if (elt.x,elt.y)==pos:
                    self.is_wolf.remove(elt)

        def remove_sheep(self, pos):
            for elt in self.is_sheep:
                if (elt.x,elt.y)==pos:
                    self.is_sheep.remove(elt)
        

    def draw(self):
        pyxel.init(GRID_SIZE, GRID_SIZE, title="Simulation")
        pyxel.cls(15)

    def start(self):
        pyxel.run(self.draw)


grid().start()

        

