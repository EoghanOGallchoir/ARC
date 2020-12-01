#!/usr/bin/python

import os, sys
import json
import numpy as np
import re

### Name: Eoghan Ó Gallchóir
### ID:   16339936

### github link:
### https://github.com/EoghanOGallchoir/ARC

def solve_4258a5f9(x):
    '''
    Task description:
    Light blue squares must be surrounded by purple squares. (Unsure of exact colours, bit colour blind)
    so a grid of: 0 0 0 0 0 must become:  0 1 1 1 0
                  0 0 5 0 0               0 1 5 1 0
                  0 0 0 0 0               0 1 1 1 0
                  
    Function:
    Solve will work by identifying blue squares, which is 5 in the grid.
    Then, the function will put purple squares, 1, around the blue (5) square.
    '''
    blue = 5
    purple = 1
    
    #iterating through each row+column to find blues
    for row in range(0, x.shape[0]):
        for col in range(0, x.shape[1]):
            # changing the surrounding black squares to blue
            if x[row][col] == blue:
                for change in range(-1,2):
                    x[row-1][col+change] = purple
                    x[row+1][col+change] = purple
                    # easiest way i could think of keeping the blue square blue while changing left and right of it
                    if x[row][col+change] != blue:
                        x[row][col+change] = purple           
    
    return x

def solve_46442a0e(x):
    '''
    Task Description:
    This takes the entire grid as an input and rotates it around 3 times, if that makes sense.
    So a 2x2 grid of: 0 1 becomes a 4x4 grid of: 0 1 1 0
                      1 0                        1 0 0 1
                                                 1 0 0 1
                                                 0 1 1 0
    As you can see the original matrix in the top left gets rotated around.
    
    Function:
    Get the grid, x, and rotate its orientation 90 deg to get x1.
    get x1 and rotate that 90 deg to get x2, then x2 rotate to get x3.
    Finally put all 4 grids together in the form: x  x1
                                                  x3 x2
    
                                                            
    '''
    # using list comprehension to revere grids x, x1, x2 using reversed() python function
    x1 = [list(reversed(colour)) for colour in zip(*x)]
    x2 = [list(reversed(colour)) for colour in zip(*x1)]
    x3 = [list(reversed(colour)) for colour in zip(*x2)]
    # combining the the lists along the horizontal axis, two halves
    arr1 = np.concatenate((x, x1), axis=1)
    arr2 = np.concatenate((x3,x2),axis=1)
    # combining both into one grid
    x = np.concatenate((arr1,arr2))
              
    return x



def solve_508bd3b6(x):
    '''
    Task Description:
    One must get the direction of the blue squares and trace its trajectory towards a red wall.
    Green squares must then kind of trace that trajectory towards and away from that red wall.
    
    Function:
    Function finds the direction of the blue squares and the location of the red wall.
    The function must then put green squares towards the red wall, using the blue squares to direct itself.
    Then the direction is reversed to give the bounce trajectory of the blue squares.
    '''
    blue = 8

    row_len = len(x)
    col_len = x.shape[1]
    
    # get top and bottom blues
    for row in range(row_len): 
        if row == 0 or row == row_len-1:
            for col in range(col_len):
                if x[row][col] == blue:
                    # on first and last row, get blue square and their neighbour to get direction.
                    if row == 0:
                        if x[1][col+1] == blue:
                            # direction is then passed to the paint_to function so it can paint green squares
                            x = paint_to("SE", x,row,col)
                        elif x[1][col-1] == blue:
                            
                            x = paint_to("SW", x,row,col)
                    else:
                        if x[row_len-2][col+1] == blue:
                            
                            x = paint_to("NE", x,row,col)
                        elif x[row_len-2][col-1] == blue:
                            
                            x = paint_to("NW", x,row,col)
    
    # look for blues on left and right side                          
    for col in range(col_len):
        if col == 0 or col == col_len-1:
            for row in range(row_len):
                if x[row][col] == blue:
                    if col == 0:
                        if x[row+1][1] == blue:
                            # same as before, painting green squares
                            x = paint_to("SE", x, row, col)
                        elif x[row-1][1] == blue:
                            x = paint_to("NE",x,row,col)
                    else:
                        if x[row+1][col_len-1] == blue:
                            x = paint_to("SW", x, row, col)
                        elif x[row-1][col_len-1] == blue:
                            x = paint_to("NW",x,row,col)
                    
                    
    return x

# paints diagonal squares green when given a direction
def paint_to(dir, arr,r,c):
    blue = 8
    red = 2
    black = 0
    green = 3
    i = 0
    j = 0
    # using the direction, gives i and j a value in which the squares are painted
    if dir == "SE":
        i = 1
        j = 1
    if dir == "SW":
        i = 1
        j = -1
    if dir == "NE":
        i = -1
        j = 1
    if dir == "NW":
        i = -1
        j = -1

    # paints green if allowed
    if 0 <= r < len(arr):
        if 0 <= c < arr.shape[1]:
            while arr[r+i][c+j] != red or arr[r+i][c+j] == black:
                if arr[r+i][c+j] != blue:
                    arr[r+i][c+j] = green
                
                r = r+i
                c = c+j
        # similar function to paint_to, paints from the red wall until the edge of the grid
        # i.e the bounce back
        paint_fro(dir,arr,r,c)

    return arr
    
def paint_fro(dir, x_inp, row, col):
    i = 0
    j = 0
    green = 3
    if dir == "SE":
        dir = "SW"
        i = 1
        j = -1
        
    elif dir == "SW":
        dir = "SE"
        i = 1
        j = 1

    elif dir == "NE":
        dir = "NW"
        i = -1
        j = -1

    elif dir == "NW":
        dir = "NE"
        i = -1
        j = 1

    # paints green until the border
    while 0 <= row+i < len(x_inp) and 0 <= col+j < x_inp.shape[1]:
        x_inp[row+i][col+j] = green
        row = row + i
        col = col + j
    
    

def main():
    # Find all the functions defined in this file whose names are
    # like solve_abcd1234(), and run them.

    # regex to match solve_* functions and extract task IDs
    p = r"solve_([a-f0-9]{8})" 
    tasks_solvers = []
    # globals() gives a dict containing all global names (variables
    # and functions), as name: value pairs.
    for name in globals(): 
        m = re.match(p, name)
        if m:
            # if the name fits the pattern eg solve_abcd1234
            ID = m.group(1) # just the task ID
            solve_fn = globals()[name] # the fn itself
            tasks_solvers.append((ID, solve_fn))

    for ID, solve_fn in tasks_solvers:
        # for each task, read the data and call test()
        directory = os.path.join("..", "data", "training")
        json_filename = os.path.join(directory, ID + ".json")
        data = read_ARC_JSON(json_filename)
        test(ID, solve_fn, data)
    
def read_ARC_JSON(filepath):
    """Given a filepath, read in the ARC task data which is in JSON
    format. Extract the train/test input/output pairs of
    grids. Convert each grid to np.array and return train_input,
    train_output, test_input, test_output."""
    
    # Open the JSON file and load it 
    data = json.load(open(filepath))

    # Extract the train/test input/output grids. Each grid will be a
    # list of lists of ints. We convert to Numpy.
    train_input = [np.array(data['train'][i]['input']) for i in range(len(data['train']))]
    train_output = [np.array(data['train'][i]['output']) for i in range(len(data['train']))]
    test_input = [np.array(data['test'][i]['input']) for i in range(len(data['test']))]
    test_output = [np.array(data['test'][i]['output']) for i in range(len(data['test']))]

    return (train_input, train_output, test_input, test_output)


def test(taskID, solve, data):
    """Given a task ID, call the given solve() function on every
    example in the task data."""
    print(taskID)
    train_input, train_output, test_input, test_output = data
    print("Training grids")
    for x, y in zip(train_input, train_output):
        yhat = solve(x)
        show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)

        
def show_result(x, y, yhat):
    print("Input")
    print(x)
    print("Correct output")
    print(y)
    print("Our output")
    print(yhat)
    print("Correct?")
    # if yhat has the right shape, then (y == yhat) is a bool array
    # and we test whether it is True everywhere. if yhat has the wrong
    # shape, then y == yhat is just a single bool.
    print(np.all(y == yhat))

if __name__ == "__main__": main()

