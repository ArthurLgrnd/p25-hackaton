import numpy as np
import pyxel
import random as rd


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

from entities import wolf, sheep, grass


class grid:
    def __init__(self):

        self.is_wolf=[]
        self.is_sheep=[]
        self.is_grass=[]

        def libre(x, y):
            return all(obj.x != x or obj.y != y
                       for obj in (self.is_sheep + self.is_wolf))
        def sol(x, y):
            return all(obj.x != x or obj.y !=y
                       for obj in self.is_grass)

        while len(self.is_grass) < np.floor(INITIAL_GRASS_COVERAGE*GRID_SIZE**2/100):
            x1, y1 =rd.randint(0,GRID_SIZE-1), rd.randint(0,GRID_SIZE-1)
            if sol(x1,y1):
                self.is_grass += [grass(x1, y1, True)]

        while len(self.is_sheep) < INITIAL_SHEEP:
            x1, y1=rd.randint(0,GRID_SIZE-1), rd.randint(0,GRID_SIZE-1)
            if libre(x1, y1):
                self.is_sheep += [sheep(x1, y1,SHEEP_INITIAL_ENERGY,0)]

        while len(self.is_wolf) < INITIAL_WOLF:
            x1, y1=rd.randint(0,GRID_SIZE-1), rd.randint(0,GRID_SIZE-1)
            if libre(x1, y1):
                self.is_wolf += [wolf(x1, y1,WOLF_INITIAL_ENERGY,0)]

        pyxel.init(GRID_SIZE*TILE, GRID_SIZE*TILE, title="Simulation")
        pyxel.load("sim.pyxres")
        
        
        def remove_wolf(self, pos): # pos est un couple (x,y)
            for w in self.is_wolf:
                if (w.x,w.y)==pos:
                    self.is_wolf.remove(w)

        def remove_sheep(self, pos):
            for s in self.is_sheep:
                if (s.x,s.y)==pos:
                    self.is_sheep.remove(s)

        def remove_grass(self, pos):
            for g in self.is_grass:
                if (g.x,g.y)==pos:
                    self.is_grass.remove(g)        

    def draw(self):
        pyxel.cls(4)
        for g in self.is_grass:
            g.draw()
        for s in self.is_sheep:
            s.draw()
        for w in self.is_wolf:
            w.draw()

    def update(self):
        pass

    def start(self):
        pyxel.run(self.update, self.draw)

grid().start()

        

