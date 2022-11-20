import numpy as np
import imageio
import os
from MemeticAlgo import Memetic
import MazeGrid as maze
import time
import GeneratePath as Tracing
from pathlib import Path
import Stamp as stamp

startTime = time.time()
# Save Path
imageFolder = Path().resolve()
saveLocation = imageFolder / "Saved Images/All Mazes.gif"
copiesLocation = imageFolder / "Saved Mazes/"

'''
Value of the genes is intended to be imbalance to ensure that the algorithm runs
with more generation
'''
GENES = '1111111111111111111111111111110' 
POPULATION_SIZE = 100
MAZE_CELLS = 15
# It is essential to add one to result in a 15 x 15 cells
MAZE_EDGE = MAZE_CELLS + 1
MAZE_SIZE = MAZE_EDGE * MAZE_EDGE

# For printing the maze into images
def PrintMaze(fittest_list: list):
    # Array value from the sketch
    final_maze = Tracing.ImagePixelating(MAZE_CELLS)
    #print(final_maze)
    trace = np.array(final_maze)
    # List of Mazes Images
    imageList = []
    # Variable for the counting of mazes
    mazeNum = 1
    for file in os.scandir(copiesLocation):
        os.remove(file.path)
    for fitness, fittest in fittest_list:
        gridFittest = np.reshape(np.array(list(map(int, fittest.chromosome))), [MAZE_EDGE, MAZE_EDGE])
        processedGrid = maze.GridWalls(gridFittest, MAZE_EDGE)
        output = maze.CarveMaze(processedGrid, MAZE_EDGE)
        
        outputGrid = np.array(stamp.LayeringMaze(trace, output, MAZE_EDGE))
        maze.GridIntoImage(outputGrid, imageList, fitness, MAZE_EDGE, mazeNum)
        mazeNum = mazeNum + 1
        #print(mazeNum)
    """
    # This is to show the values of the grids
    for i in range(len(outputGrid)):   
        print(outputGrid[i])
    print(gridFittest)
    print(processedGrid)    
    """
    #Output the fittest from generation into an animated gif
    imageio.mimsave(saveLocation, imageList, fps=2)
    
def GetFitness(self):
    '''
    Calculate fitness score
    The Fitness calculation is the sum of the chromosomes that consists of 0s and 1s
    subtracted to the size // 2
    '''
    fitness = abs(sum(list(map(int, self.chromosome))) - MAZE_SIZE // 2)
    return fitness
    
def main():
    startProcess = Memetic(populationSize=POPULATION_SIZE, genes=GENES, gnomeLen=MAZE_SIZE, fitnessFunc=GetFitness)
    # Start the maze generation
    output = startProcess.run()
    numGen = 0
    for number, (generation, fittest) in enumerate(output):
        print("Generation: {} String: {} Fitness: {}".
            format(generation,
            "".join(fittest.chromosome),
            fittest.fitness))
        numGen = generation
        chromosomeArray = np.reshape(np.array(list(map(int, fittest.chromosome))), [MAZE_EDGE, MAZE_EDGE])
        #print(chromosomeArray)
    PrintMaze(fittest_list=output)
    return numGen
def start():
    startProgram = main()
    print("--- Execution Time: {} seconds ---".format(round(time.time() - startTime), 2))
    return startProgram 
# For testing purposes by running this program calling start     
#start()