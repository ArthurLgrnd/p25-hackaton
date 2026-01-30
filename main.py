import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

#pop_wolf, pop_sheep, grass = simulation()

pop_wolf = np.random.randint(0,20,size=(20))
pop_sheep = np.random.randint(0,20,size=(20))
grass = np.random.randint(0,20,size=(20))

t=np.linspace(1,20,20)

fig, axis = plt.subplots(1,3)

axis[0].set_xlim([0,max(t)])
axis[0].set_ylim([0,20])
axis[1].set_xlim([0,max(t)])
axis[1].set_ylim([0,20])
axis[2].set_xlim([0,max(t)])
axis[2].set_ylim([0,20])

animated_wolf, =axis[0].plot([], [], label='loups')
animated_sheep, =axis[1].plot([], [], label='moutons')
animated_grass, =axis[2].plot([], [], label='herbe')


def update_data(frame):
    animated_wolf.set_data(t[:frame], pop_wolf[:frame])
    animated_sheep.set_data(t[:frame], pop_sheep[:frame])
    animated_grass.set_data(t[:frame], grass[:frame])

    return animated_wolf, animated_sheep, animated_grass

animation = FuncAnimation(fig = fig, func = update_data, frames = len(t), interval=200, repeat = False)

axis[0].set_xlabel('temps')
axis[1].set_xlabel('temps')
axis[2].set_xlabel('temps')

axis[0].set_ylabel('effectifs')
axis[0].set_ylabel('effectifs')
axis[0].set_ylabel('effectifs')

animated_wolf
axis[0].legend()
axis[1].legend()
axis[2].legend()

plt.show()



