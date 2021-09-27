#VehiclesTask2

from simple_agent_lesion import run
import numpy as np

def navigateToLightSource():
    geno = np.array([1, 1, 0, 0])
    initial_pos = [50, 50]
    t = 4000
    bearing = 50
    output = run(t, initial_pos, bearing, geno, 1)

navigateToLightSource()

#rotate 360 degrees, move towards light.
#If brightess goes up continue rotating and moving forward,
#if brightness goes down, rotate the other direction slowly and keep moving
#keep alternating between the two rotations until light sensor value is peaked.
#This will hone in on the light source

#rotate clockwise
#if current intensity is greater than before, keep rotating clockwise
#if current intensity is less than before, rotate anticlockwise
