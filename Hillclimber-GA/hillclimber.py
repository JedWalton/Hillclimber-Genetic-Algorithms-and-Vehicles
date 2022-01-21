#Hillclimber Algorithm

import matplotlib.pyplot as plt
import random as random
import numpy as np

Matrix = np.array([['a', 5, 3, 0], ['b', 6, 2, 0], ['c', 1, 4, 0], ['d', 9, 5, 0], ['e', 2, 8, 0], ['f', 8, 9, 0], ['g', 4, 10, 0], ['h', 3, 1, 0], ['i', 7, 6, 0], ['j', 10, 7, 0]], dtype = object)
Genotype = Matrix



class hillclimber:#
    optimalCount = 0
    def _init_(self, Genotype, object):
        hillclimber.Genotype = Matrix
        hillclimber.Genotype = self.CreateGenotype(Genotype)
        hillclimber.hillClimberCount += 1
        Genotype = Matrix
        self.optimalCount = 0

    def RandomiseGenotype(self, Genotype):
        for i in Genotype:
            vol = self.getTotalVolumeOfGenotype(Genotype)
            count = 0
            while (vol + i[1] <= 20):
                randomChoice = random.choice(list(Genotype))
                comparison = i == randomChoice
                equal_arrays = comparison.all()
                if (equal_arrays == True):
                    i[3] = 1
                count += 1
                if (count == 30):
                    break

        return (Genotype)

    def displayGenotype(self, Genotype):
        print(Genotype)

    def getTotalVolumeOfGenotype(self, Genotype):
        volume = 0
        for i in Genotype:
            if (i[3] == 1):
                volume = volume + i[1]
        return volume

    def getTotalBenefitOfGenotype(self, Genotype):
        benefit = 0
        for i in Genotype:
            if (i[3] == 1):
                benefit = benefit + i[2]
        return benefit

    def fitness(self, Genotype):
        if (self.getTotalVolumeOfGenotype(Genotype) < 20):
            return self.getTotalBenefitOfGenotype(Genotype)
        else:
            return 20 - self.getTotalBenefitOfGenotype(Genotype)
        if(getTotalBenefitOfGenotype(Genotype) == 31):
            self.optimalCount += 1

    def CreateGenotype(self, Genotype):  # function to create a genotype with VOLUME <= 20
        Genotype = np.array([])
        Genotype = Matrix
        Genotype = self.RandomiseGenotype(Genotype)
        #print(Genotype)
        return Genotype
#
    def mutate(self, Genotype):
        num = random.randint(0, 9)
        if (Genotype[num][3] == 0):
            Genotype[num][3] = 1
            if (self.getTotalVolumeOfGenotype(Genotype) > 20):
                Genotype[num][3] = 0
        if (Genotype[num][3] == 1):
            Genotype[num][3] = 0
            self.RandomiseGenotype(Genotype)

        return Genotype

    def climber(self, Genotype, G):
        fitness = []
        fitnessGeno = self.fitness(Genotype)
        for i in range(0, G):
            mutatedGeno = self.mutate(Genotype)
            fitnessMutatedGeno = self.fitness(mutatedGeno)
            #if(fitnessMutatedGeno < fitnessGeno):
            #    fitnessGeno = fitnessGeno
            if(fitnessGeno < fitnessMutatedGeno):
                fitnessGeno = fitnessMutatedGeno
            fitness.append(fitnessGeno)
            #print(len(fitness))
        return fitness


hillClimber0 = hillclimber()
geno = hillClimber0.CreateGenotype(Genotype)
fitness0Climber = hillClimber0.climber(geno, 100)
#print(fitness0Climber)

P = []
listOfFitness = []
for i in range(0, 100): # create 100 genotypes
    geno = hillClimber0.CreateGenotype(Genotype)
    fitness0Climber = hillClimber0.climber(geno, 100)
    P.append(geno)
    listOfFitness.append(fitness0Climber[-1])
    plt.plot(fitness0Climber)
    plt.xlabel("Generations")
    plt.ylabel("fitness")

plt.show()
print(listOfFitness)
optimalCount = 0
for i in listOfFitness:
    if(i == 32):
        optimalCount += 1

print(optimalCount)