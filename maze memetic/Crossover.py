import random
from Mutate import Mutation

# Function for getting the fitness value 
def XO_GetFitness(childfit, size):
        '''
        The Fitness calculation is the sum of the chromosomes that consists of 0s and 1s
        subtracted to the size // 2
        '''
        fitness = abs(sum(list(map(int, childfit))) - size // 2)
        return fitness
        
class Individual(Mutation):
    def __init__(self, chromosome: str, genes: str, gnomeLen: int, fitnessFunc):
        super().__init__(genes)
        self.chromosome = chromosome
        self.gnomeLen = gnomeLen
        self.fitnessFunc = fitnessFunc
        self.fitness = fitnessFunc(self)

    # Crosssover with First Choice Hill Climbing Algorithm 
    def MateCrossover(self, par2, size) -> list: 
        # Breeding the first offspring
        childChromosome = []
        # Uniform Crossover
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):
                prob = random.random()
                if prob < 0.45:
                    childChromosome.append(gp1)
                elif prob < 0.90:
                    childChromosome.append(gp2)
                else:
                    childChromosome.append(self.mutate_genes())
        '''  
        Evaluation and comparing of offspring to siblings using
        First-Choice Hill Climbing Algorithm
        '''
        isBetter = False
        while isBetter != True:
            # Generating new offsprings as siblings
            # Siblings is considered as the neighbor of the offspring
            sibling = []
            for gp1, gp2 in zip(self.chromosome, par2.chromosome):
                prob = random.random()
                if prob < 0.45:
                    sibling.append(gp1)
                elif prob < 0.90:
                    sibling.append(gp2)
                else:
                    sibling.append(self.mutate_genes())
            # Getting the fitness value of the current offspring and sibling
            childFit = XO_GetFitness(childChromosome, size)
            siblingFit = XO_GetFitness(sibling, size)
            """
            # For diplaying the fitness of the offspring and sibling
            print("Offspring: {} Sibling: {}".
                format(childFit, siblingFit))
            """
            # Comparison of the offspring and the sibling
            if siblingFit < childFit:
                childChromosome = sibling
                childFit = siblingFit
                isBetter = True
        return Individual(childChromosome,self.genes,self.gnomeLen,self.fitnessFunc)


