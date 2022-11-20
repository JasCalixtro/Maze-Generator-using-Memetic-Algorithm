import numpy as np
import matplotlib.pyplot as plt   
from pathlib import Path
from PIL import Image                                   
from skimage.color import rgb2gray

def ConvertSize(size, traced):
    '''
    Conversion from 30x30 array of traced into 30 x 15
    '''
    firstResize = []
    i = 0
    j = 0
    while i < size:
        j = 0
        while j < size:
            x = 0
            track = traced[i, j]
            if track == traced[i, j+1]:
                x = track
            elif track == 0 or traced[i, j+1] == 0:
                x = 0
            firstResize.append(x)
            j = j + 2
        i = i + 1
    '''
    Conversion from 30x15 array of traced into 15 x 15
    '''    
    updatedTrace = np.reshape(np.array(firstResize), [30,15])
    secondResize = []
    i = 0
    j = 0
    while i < size:
        j = 0
        while j < size/2:
            x = 0
            track = updatedTrace[i, j]
            if track == updatedTrace[i+1, j]:
                x = track
            elif track == 0 or updatedTrace[i+1, j] == 0:
                x = 0
            secondResize.append(x)
            j = j + 1
        i = i + 2

    sketchTraced= np.reshape(np.array(secondResize), [15,15])
    return sketchTraced

def ImagePixelating(sizeOfMaze):
    mazeSize = sizeOfMaze*2
    # Save Paths
    imageFolder = Path().resolve()
    imageLocation = imageFolder / "Saved Sketches/sketch.png"
    pixelLocation = imageFolder/ "Saved Images/pixelized.png"
    dimensionLocation = imageFolder/ "Saved Images/dimension.png"
    # Read image
    img=Image.open(imageLocation)
    # Transforming image to pixel version
    def pixelating(image, i_size):
        # Read file
        img=Image.open(image)
        # Convert to small image
        small_img=img.resize(i_size,Image.BILINEAR)
        # resize to output size
        res=small_img.resize(img.size, Image.NEAREST)
        # Save output image
        res.save(pixelLocation)

    # Using method to resize
    pixelating(image=imageLocation,i_size=(mazeSize,mazeSize))
    # Resizing image to pixel
    img = Image.open(pixelLocation)
    # Resizing dimension of image
    dim = img.resize((mazeSize,mazeSize))     
    dim.save(dimensionLocation)

    # Finding Path Structure
    image = Image.open(dimensionLocation)
    grey = rgb2gray(image)

    '''
    # For displaying the pixelated maze with pixel values
    plt.show()
    print(min(grey))
    '''

    path=[]
    # Read x,y cells of the image
    for x in range(mazeSize):
        for y in range(mazeSize):
            if grey[x,y] >= 0.7:
                grey[x,y]=1
            path.append(int(grey[x,y]))
    sample = np.reshape(np.array(path), [mazeSize,mazeSize])
    
    tracedSketch = ConvertSize(mazeSize, sample)
    
    return tracedSketch















