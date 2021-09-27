#Steady State Genetic Algorithm

import matplotlib.pyplot as plt
import random as random
import numpy as np
from hillclimber import hillclimber

Matrix = np.array([['a', 5, 3, 0], ['b', 6, 2, 0], ['c', 1, 4, 0], ['d', 9, 5, 0], ['e', 2, 8, 0], ['f', 8, 9, 0], ['g', 4, 10, 0], ['h', 3, 1, 0], ['i', 7, 6, 0], ['j', 10, 7, 0]], dtype = object)
Genotype = Matrix

class GA:
    def __init__(self, Genotype, populationSize, numberOfGen):
        self.pop = []
        randomSize = random.randint(50, populationSize)
        for i in range(randomSize):
            hillClimber0 = hillclimber()
            hillClimber = hillClimber0.CreateGenotype(Genotype)
            self.pop.append(hillClimber)

        self.noOfGen = numberOfGen
        self.Geno = Genotype
        print(self.Geno)
        print(self.noOfGen)

    def mutate(self):
        meanFitnessAtEachEvaluation = []
        for i in range(self.noOfGen):
            lenPop = ((len(self.pop)) - 1)
            num1 = random.randint(0, lenPop)
            num2 = random.randint(0, lenPop)
            a = self.pop[num1]
            b = self.pop[num2]
            aclimb = hillclimber0.climber(self.Geno, self.noOfGen)
            bclimb = hillclimber0.climber(self.Geno, self.noOfGen)
            #last item of fitness arrays
            #compare last item
            aFit = aclimb[-1]
            bFit = bclimb[-1]

            if (aFit == bFit):
                winner = a
                loser = b
            if (aFit > bFit):
                winner = a
                loser = b
            if (bFit > aFit):
                winner = b
                loser = a
            # copy W over L
            a = winner
            b = winner
            self.pop[num1] = a
            self.pop[num2] = b
            #print(a)
            # add a mutation to the loser
            for i in range(20):
                winnerFit = hillclimber0.fitness(winner)
                mutatedLoser = hillclimber0.mutate(loser)
                mutatedLoserFit = hillclimber0.fitness(mutatedLoser)
                if(mutatedLoserFit > winnerFit):
                    winner = mutatedLoser

            meanFitnessAtEachEvaluation.append(winner)
        return meanFitnessAtEachEvaluation


hillclimber0 = hillclimber()
ga0 = GA(Genotype, 100, 100)
fitnessPlot = ga0.mutate()

#print(fitnessPlot)

plt.plot(fitnessPlot)
plt.show()


