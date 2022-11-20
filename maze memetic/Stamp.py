import numpy as np

'''
This part is the Layering of the Maze and also
Stamping the pattern of the sketch
'''
def LayeringMaze(trace, output, size):
    outputList = []
    # Convertion of # and ' ' into 0s and 1s
    for element in output:
        element[element == '#'] = 0
        element[element == ' '] = 1
        outputList.append(list(element.astype(int)))
    # Solidifying the first column and the last row
    # To have a border for the maze
    for i in range(1, len(outputList)-2):
        outputList[i][1] = 1
        outputList[-3][i] = 1

    i = 0
    j = 0
    while i < size - 1:
        p = i*4 + 3
        while j < size - 1:
            q = j*4 + 3
            temp = trace[i,j]
            if temp == 0:
                if i != size-2:
                    # Below walls
                    # Removes walls below if an index value 0 has another index value 0 below it
                    if trace[i+1,j] == 0:
                            outputList[p+2][q] = 0
                            outputList[p+2][q-1] = 0
                            outputList[p+2][q+1] = 0

                if j != size-2:
                    # Sides wall
                    # Adds or removes a wall if the next index value is either 1 or 0
                    if trace[i,j+1] == 1:
                        outputList[p][q+2] = 1
                        outputList[p-1][q+2] = 1
                        outputList[p+1][q+2] = 1
                        outputList[p+2][q+2] = 1
                    
                    if trace[i,j+1] == 0:
                        outputList[p][q+2] = 0
                        outputList[p-1][q+2] = 0
                        outputList[p+1][q+2] = 0
                    
                    # Below side wall
                    '''
                    Adds a wall on the right side of the cell depending on the random chance
                    if the current index value is surrounded by other index value 0
                    sample => 0 0  result may be => 0|0
                              0 0                   0 0
                    '''
                    if i != size-2 and trace[i+1, j+1] == 0:
                        if trace[i+1, j] == 0 :
                            if trace[i, j+1] == 0:
                                outputList[p][q+2] = 1
                                outputList[p-1][q+2] = 1
                                outputList[p+1][q+2] = 1 
                                                
            # Fixing deadblocks
            '''
            We like to call an impassable path as a deadblock
            This path does not have an entry or exit point
            We decided to only fix single and double blocks to
            have a acceptable maze path
            ''' 
            # Single cell deadblock
            if outputList[p-2][q] == 1 and outputList[p+2][q] == 1 and outputList[p][q-2] == 1 and outputList[p][q+2] == 1:
                u = np.random.randint(0, 2)
                if u == 0:#updown
                    outputList[p-2][q-1] = 0
                    outputList[p-2][q] = 0
                    outputList[p-2][q+1] = 0
                    #outputList[p-2][q+2] = 0
                    outputList[p+2][q-1] = 0
                    outputList[p+2][q] = 0
                    outputList[p+2][q+1] = 0
                if u == 1: #leftright
                    outputList[p-1][q+2] = 0
                    outputList[p][q+2] = 0
                    outputList[p+1][q+2] = 0
                    
                    outputList[p-1][q-2] = 0
                    outputList[p][q-2] = 0
                    outputList[p+1][q-2] = 0 

            # Double cell deadblock
            # Vertical
            if i != size-2 and outputList[p-2][q] == 1 and outputList[p+2][q] == 0 and outputList[p+6][q] == 1:
                if outputList[p][q-2] == 1 and outputList[p][q+2] == 1:
                    if outputList[p+4][q-2] == 1 and outputList[p+4][q+2] == 1:
                        # upper right
                        outputList[p][q+2] = 0
                        outputList[p-1][q+2] = 0
                        outputList[p+1][q+2] = 0

                        # lower left
                        outputList[p+3][q-2] = 0
                        outputList[p+4][q-2] = 0
                        outputList[p+5][q-2] = 0
            # Horizontal
            if j != size-2 and outputList[p][q-2] == 1 and outputList[p][q+2] == 0 and outputList[p][q+6]== 1:
                if outputList[p-2][q] == 1 and outputList[p+2][q] == 1:
                    if outputList[p-2][q+4] == 1 and outputList[p+2][q+4] == 1:
                        # lower left
                        outputList[p+2][q] == 0
                        outputList[p+2][q-1] == 0
                        outputList[p+2][q+1] == 0

                        # upper right
                        outputList[p-2][q+3] == 0
                        outputList[p-2][q+4] == 0
                        outputList[p-2][q+5] == 0

            j = j + 1
        i = i + 1
        j = 0
    # Refixing the walls for the border
    for i in range(1, len(outputList)-2):
        outputList[i][1] = 1
        outputList[-3][i] = 1
        outputList[i][-2] = 1
        outputList[1][i] = 1
    return outputList