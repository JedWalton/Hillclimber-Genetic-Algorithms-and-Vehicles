#Vehicles
# aggressor, lover, explorer, and cowardAttempt a one-eyed phototaxis solution implemented using Braitenberg
# machine to demonstrate how rich behavior emerges from a simple brain.

from simple_agent import run
import numpy as np

def aggressor():
    geno = np.array([0, 1, 1, 0, 0, 0])
    initial_pos = [12, 12]
    t = 1000
    bearing = 180
    output = run(t, initial_pos, bearing, geno, 1)


def coward():
    geno = np.array([1, 0, 0, 1, 0, 0])
    initial_pos = [5, 5]
    t = 100
    bearing = 90
    output = run(t, initial_pos, bearing, geno, 1)

def lover():
    geno = np.array([-1, 0, 0, -1, 1, 1])
    initial_pos = [-100, -5]
    t = 150
    bearing = 40
    output = run(t, initial_pos, bearing, geno, 1)


def explorer():
    geno = np.array([0, -1, -1, 0, 1, 1])
    initial_pos = [5, 10]
    t = 30
    bearing = 225
    output = run(t, initial_pos, bearing, geno, 1)



#Un-comment method to create graph
#aggressor()
#lover()
explorer()
#coward()
