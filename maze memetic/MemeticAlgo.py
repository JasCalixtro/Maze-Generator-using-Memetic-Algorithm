from Crossover import Individual
from random import choice
from pathlib import Path
import customtkinter
from tkinter import *
from tkinter.ttk import *
from Mutate import Mutation
from tkinter import messagebox

class Memetic(Mutation):

    def __init__(self, populationSize, genes, gnomeLen, fitnessFunc):
        super().__init__(genes)
        self.populationSize = populationSize
        self.fitnessFunc = fitnessFunc
        self.gnomeLen = gnomeLen
        print("Length of Genes per Generation: {}".format(self.gnomeLen))

        # Window
        self.window = customtkinter.CTk()
        self.window.configure(bg="#edede9")
        self.window.title("Maze Generator")
        imageFolder = Path().resolve()
        imageLocation = imageFolder /"icon.ico"
        self.window.iconbitmap(imageLocation)
        x = (self.window.winfo_screenwidth()//2)-(380//2)
        y = (self.window.winfo_screenheight()//2)-(200//2)
        self.window.geometry('{}x{}+{}+{}'.format(380, 200, x, y))    
        # LoadScreen
        self.bar = Progressbar(self.window,orient=HORIZONTAL,length=350)
        self.bar.pack(pady=80)

    def loadScreen(self, currentPercent):
        textLabel = Label(self.window, text= 'Please wait while the program is generating mazes', font=("System", 12))
        textLabel.place(relx = 0.035, rely = 0.05)
        percentLabel = Label(self.window, text= "Current Progress: " + str(currentPercent) + "% Complete", font=("System", 12))
        percentLabel.place(relx = 0.035, rely = 0.3)
        self.bar['value'] = currentPercent
        self.window.update()

    def CreateGnome(self) -> list:
        # Mutating genes to generate chromosomes
        return [self.mutate_genes() for _ in range(self.gnomeLen)]

    def run(self) -> list:
        output = []
        # Current generation
        generationNumber = 1
        found = False
        population = []
        # Create initial population
        for _ in range(self.populationSize):
            gnome = self.CreateGnome()
            population.append(Individual(gnome, self.genes, self.gnomeLen, self.fitnessFunc))
        # Used for the loading percentage
        xpop= sorted(population, key=lambda x: x.fitness)
        popMax = xpop[-1].fitness
        while not found:
            # Sort the population in increasing order of fitness score
            population = sorted(population, key=lambda x: x.fitness)
            # Loading Screen
            percent =  int(100-(round(population[0].fitness / popMax, 2)*100))
            self.loadScreen(percent)
            fill = '█'
            bar = fill * percent + '-' * (100 - percent)
            print('\rProgress: |{}| {}% Complete'.format(bar,percent), end = '\r')

            '''
            Condition to determine if the population is currently best
            if the lowest individual which is the first index has 0 fitness
            it will then break the loop as the program decides that the best population is found
            '''
            if population[0].fitness <= 0:
                found = True
                break
            # Otherwise generate new offsprings for new generation
            newGeneration = []
            # Perform Elitism, that means 10% of fittest population goes to the next generation
            elite = int((10*self.populationSize)/100)
            newGeneration.extend(population[:elite])
            # 50% of the fittest population individuals will mate to produce offspring
            half = int((90*self.populationSize)/100)
            for _ in range(half):                
                parent1 = choice(population[:self.populationSize//2])
                parent2 = choice(population[:self.populationSize//2])                
                pair = False
                # Making sure that parents arent identical
                while not pair:
                    if parent1 == parent2:
                        parent2 = choice(population[:self.populationSize//2])
                    elif parent1 != parent2:
                        pair = True
                # Call the MateCrossover function to mate two individuals
                child = parent1.MateCrossover(parent2, self.populationSize)
                newGeneration.append(child) 
            # Makes the new generation as the current population      
            population = newGeneration
            output.append((generationNumber, population[0]))
            generationNumber += 1
        output.append((generationNumber, population[0]))
        # Close the loading window
        self.window.destroy()
        messagebox.showinfo("Maze Generator", "Mazes are generated Successfully! \nPlease wait for the next window to open \n\nPlease click 'OK' to continue...")

        return output
