from entities import wolf, sheep, grass
import numpy as np
import pyxel
from grid import grid

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

class Simulation :

    def __init__(self): 

        pyxel.init(GRID_SIZE*TILE, GRID_SIZE*TILE, title="Simulation", fps=1)
        pyxel.load("sim.pyxres")
        
        self.grid = grid()
        self.time = 0
        self.max_time = 1000



    def update(self):
            
        # on effectue toutes les actions de la simulation :
            self.grid.aging_sheep()
            self.grid.aging_wolf()
            self.grid.update_grass()


            self.grid.phase_moutons()
            self.grid.phase_loups()
        
            self.grid.update_dead()
            self.grid.update_dead()

            self.grid.reproduction()
            self.grid.reproduction()

        

    def run_sim(self):
        # populations et recouvrement d'herbe
        pop_sheep = len(self.grid.is_sheep)
        pop_wolf = len(self.grid.is_wolf)
        grass = len(self.grid.is_grass)

        # parametre de controle de similation
        total_animal = pop_sheep + pop_wolf
        t = self.time


        return self.grid, t, pop_sheep, pop_wolf, grass, total_animal 
    
    
    def draw(self):
        self.grid.draw()
    
    def start(self):
        pyxel.run(self.update, self.draw)

Simulation().start()