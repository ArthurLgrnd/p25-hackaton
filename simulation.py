from entities import wolf, sheep, grass
import numpy as np
import pyxel

class Simulation :

    def __init__(self,
                 grid,
                 time,
                 max_time = 500,          
                 ) : 
        
        self.grid = grid
        self.time = time
        self.max_time = max_time



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
    
        self.update()

        # populations et recouvrement d'herbe
        pop_sheep = len(self.grid.is_sheep)
        pop_wolf = len(self.grid.is_wolf)
        grass = len(self.grid.is_grass)

        # parametre de controle de similation
        total_animal = pop_sheep + pop_wolf
        t = self.time


        return self.grid, t, pop_sheep, pop_wolf, grass, total_animal 
        
    
    def start(self):
        pyxel.run(self.update(), self.draw)