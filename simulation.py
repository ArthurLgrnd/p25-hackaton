from entities import wolf, sheep, grass
import numpy as np


class Simulation :

    def __init__(self,
                 grid,
                 time,
                 max_time = 500,          
                 ) : 
        
        self.grid = grid
        self.time = time
        self.max_time = max_time

    # fonction qui renvoie les déplacement intéressants en fonction de la position de l'herbe
    # renvoie les déplacements dans les 4 directions si pas d'herbe autour
    def where_grass(self,x,y):
        list_grass = []
        for i in [-1,1] :
            if self.grid[x+i][y].isinstance(grass):   
                list_grass.append([i,0])
        for j in [-1,1] :
            if self.grid[x][y+j].isinstance(grass):   
                list_grass.append([0,j])

        if list_grass == []:
            return [(-1,0),(1,0),(0,-1),(0,1)]
        return list_grass

    # idem pour les moutons
    def where_sheep(self,x,y):
        list_sheep = []
        for i in [-1,1] :
            if self.grid[x+i][y].isinstance(sheep):   
                list_sheep.append([i,0])
        for j in [-1,1] :
            if self.grid[x][y+j].isinstance(sheep):   
                list_sheep.append([0,j])

        if list_sheep == []:
            return [(-1,0),(1,0),(0,-1),(0,1)]
        return list_sheep





    def run_sim(self):
    
        # on effectue toutes les actions de la simulation :
        new_grid_sheep = self.grid.aging()
        new_grid_wolf = self.grid.aging()
        new_grid_grass = self.grid.update_grass()

        new_grid_sheep = self.grid.phase_moutons()
        new_grid_wolf = self.grid.phase_loups()
        
        new_grid_sheep = self.grid.update_dead()
        new_grid_wolf = self.grid.update_dead()

        new_grid_sheep = self.grid.reproduction()
        new_grid_wolf = self.grid.reproduction()

        
        #mise à jour de la grille
        self.grid.is_sheep = new_grid_sheep
        self.grid.is_wolf = new_grid_wolf
        self.grid.is_grass = new_grid_grass

        # populations et recouvrement d'herbe
        pop_sheep = len(self.grid.is_sheep)
        pop_wolf = len(self.grid.is_wolf)
        grass = len(self.grid.is_grass)

        # parametre de controle de similation
        total_animal = pop_sheep + pop_wolf
        t = self.time
        return self.grid, t, 
        
   