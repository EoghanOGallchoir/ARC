#!/usr/bin/python

import os, sys
import json
import numpy as np
import re

### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.

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
    print("solving provlem 1")
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
    This function takes the entire grid as an input and rotates it around 3 times, if that makes sense.
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
    print("solving provlem 2")
    # using list comprehension to revere grids x, x1, x2 using reveresed() python function
    x1 = [list(reversed(colour)) for colour in zip(*x)]
    x2 = [list(reversed(colour)) for colour in zip(*x1)]
    x3 = [list(reversed(colour)) for colour in zip(*x2)]
    arr1 = np.concatenate((x, x1), axis=1)
    arr2 = np.concatenate((x3,x2),axis=1)
    x = np.concatenate((arr1,arr2))
              
    return x



'''

def solve_05269061(x):
    return x
'''

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

