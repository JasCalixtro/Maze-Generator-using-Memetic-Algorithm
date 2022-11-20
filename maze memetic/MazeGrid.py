import numpy as np
import imageio
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# Save Paths
imageFolder = Path().resolve()
saveLocation = imageFolder / "Saved Images/Best Maze.png"
mazeWithNumber = imageFolder / "Saved Images/Latest Maze.png"

def CarveMaze(grid: np.ndarray, size: int) -> np.ndarray:
    # Creation of Grid
    gridOutput = np.empty([size*4, (size*4)-1], dtype=str)
    gridOutput[:] = '#'

    i = 0
    j = 0
    # Variable i for the row
    # Variable j for the column
    '''
    In this grid # => space and ' ' is wall
    Making a one index into a 3 x 3 index cell
    An extension of one serving as the walls
    That is why i and j is multipled by 4 => (3 for cell space and 1 for wall space)
    Sample cell =>   ___
                    |   |
                    |   |
                    |___|
                    
    '''
    while i < size:
        w = i*4 + 1
        while j < size:
            k = j*4 + 1
            toss = grid[i, j]
            # This is a corner wall
            gridOutput[w, k] = ' '
            # If an index in fittest population is == 0, then create a horizontal wall
            if toss == 0 and k+3 < size*4: 
                gridOutput[w, k+1] = ' '
                gridOutput[w, k+2] = ' '
                gridOutput[w, k+3] = ' '
            # If an index in fittest population is == 1, then create a vertical wall    
            if toss == 1 and w-3 >= 0: 
                gridOutput[w-1, k] = ' '
                gridOutput[w-2, k] = ' '
                gridOutput[w-3, k] = ' '
            j = j + 1
        i = i + 1
        j = 0
    
    return gridOutput


def GridWalls(grid: np.ndarray, size: int) -> np.ndarray:
    
    '''
    We fixed the first row and last column 
    to avoid the program in carving this parts
    '''
    # first row
    firstRow = grid[0]
    firstRow[firstRow == 1] = 0
    grid[0] = firstRow
    #last column
    for i in range(1, size):
        grid[i, size-1] = 1

    return grid

def GridIntoImage(grid:np.ndarray, imgList:list, fit:int, size, mazeNum) -> list :
    '''
    Creates a copy of the current grid to be converted into an image
    by replacing its values with actual pixel colors.

    Outputs the current grid status to an image, to be added to
    imgList to produce an animated gif
    '''

    copiesLocation = imageFolder / "Saved Mazes/maze{}.png".format(mazeNum)
    imgGrid = grid.copy()
    imgGrid[imgGrid==0] = 1000 # White
    imgGrid[imgGrid==1] = 0    # Black
    # Converting image from array
    im = Image.fromarray(imgGrid)
    
    if im.mode != 'RGB':
        im = im.convert('RGB')
    # Size of the image
    size = 800, 800
    img = im.resize(size, Image.NEAREST)
    # Saving the current best
    imageio.imwrite(saveLocation, img)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 35)
    # Writes a number at the upper left that indicates the generation number
    draw.text((0, 0), text=str(fit), fill='red', stroke_fill='white', font=font)
    imgList.append(img)
    if fit == 0:
        imgList.append(img)
    imageio.imwrite(copiesLocation, img)
    imageio.imwrite(mazeWithNumber, img)


