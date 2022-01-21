#Spatial Genetic Algorithm

import matplotlib.pyplot as plt
import random as random
import numpy as np
from hillclimber import hillclimber

Matrix = np.array([['a', 5, 3, 0], ['b', 6, 2, 0], ['c', 1, 4, 0], ['d', 9, 5, 0], ['e', 2, 8, 0], ['f', 8, 9, 0], ['g', 4, 10, 0], ['h', 3, 1, 0], ['i', 7, 6, 0], ['j', 10, 7, 0]], dtype = object)
Genotype = Matrix



class spatialGA:
    def __init__(self, Genotype, populationSize, numberOfGen):
        self.pop = []
        randomSize = random.randint(50, populationSize)
        for i in range(randomSize):
            hillClimber0 = hillclimber()
            hillClimber = hillClimber0.CreateGenotype(Genotype)
            self.pop.append(hillClimber)

        self.noOfGen = numberOfGen
        self.Geno = Genotype


    def mutate(self, k):
        meanFitnessAtEachEvaluation = []
        lenPop = ((len(self.pop)) - 1)
        # pick random individual
        num = random.randint(0, lenPop)
        posOrNeg = random.randint(0, 1)
        if(posOrNeg == 0):
            k = -k
        if(posOrNeg == 1):
            k = k
            

        aIndividual = self.pop[num]
        bIndividual = self.pop[num + k]
        if ((num + k) > lenPop):
            bIndividual = self.pop[(num - k)]
        if ((num + k) < 0):
            bIndividual = self.pop[(num + k)]


        print(aIndividual)
        print(bIndividual)

        aFit = hillClimber0.fitness(aIndividual)
        bFit = hillClimber0.fitness(bIndividual)

        loser = aFit
        winner = bFit
        if (aFit == bFit):
            winner = aIndividual
            loser = bIndividual
        if (aFit > bFit):
            winner = aIndividual
            loser = bIndividual
        if (bFit > aFit):
            winner = bIndividual
            loser = aIndividual
        # copy W over L
        aIndividual = winner
        bIndividual = winner

        self.pop[num] = winner
        self.pop[num + k] = winner
        # add a mutation to the loser
        # loserFit = fitnessBefore(loser, 0)
        winnerFit = hillClimber0.fitness(winner)
        # print(type(loser))
        j = 0
        while (j < 20):
            winnerFit = hillClimber0.fitness(winner)
            mutatedLoser = hillClimber0.mutate(loser)
            mutatedLoserFit = hillClimber0.fitness(mutatedLoser)
            if (mutatedLoserFit > winnerFit):
                winner = mutatedLoser
            j += 1

        meanFitnessAtEachEvaluation.append(winnerFit)

        return meanFitnessAtEachEvaluation


hillClimber0 = hillclimber()
ga0 = spatialGA(Genotype, 100, 300)
fitnessPlot = ga0.mutate(3)

plt.plot(fitnessPlot)



