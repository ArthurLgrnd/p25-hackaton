import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from simulation import Simulation
from grid import grid

grille = grid()
sim = Simulation(grille)

pop_wolf = []
pop_sheep = []
grass = []
time = []
total_animals = []

fig, axis = plt.subplots(1,3)

axis[0].set_xlim([0,500])
axis[0].set_ylim([0,20])
axis[1].set_xlim([0,500])
axis[1].set_ylim([0,20])
axis[2].set_xlim([0,500])
axis[2].set_ylim([0,20])

animated_wolf, =axis[0].plot([], [], label='loups')
animated_sheep, =axis[1].plot([], [], label='moutons')
animated_grass, =axis[2].plot([], [], label='herbe')


def update_data(frame):
    
    grid,t,w,s,g,tot_animal = sim.run_sim()
    
    time.append(t)
    pop_wolf.append(w)
    pop_sheep.append(s)
    grass.append(g)
    
    total_animals.append(tot_animal)

    animated_wolf.set_data(time[:frame], pop_wolf[:frame])
    animated_sheep.set_data(time[:frame], pop_sheep[:frame])
    animated_grass.set_data(time[:frame], grass[:frame])

    sim.start()

    return animated_wolf, animated_sheep, animated_grass

animation = FuncAnimation(fig = fig, func = update_data, frames = 500, interval=200, repeat = False)

axis[0].set_xlabel('temps')
axis[1].set_xlabel('temps')
axis[2].set_xlabel('temps')

axis[0].set_ylabel('effectifs')
axis[0].set_ylabel('effectifs')
axis[0].set_ylabel('effectifs')

axis[0].legend()
axis[1].legend()
axis[2].legend()

plt.show()



