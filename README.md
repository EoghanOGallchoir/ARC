## Tasks Chosen:
**1.** solve_4258a5f9

**2.** solve_46442a0e

**3.** solve_608bd3b6 

### 1.

#### Description

The first task consists of a grid containing a few blue (5) squares.
The function must surround those squares with purple (1) squares.
![pic1]
So a grid of 0 0 0 0 0 must become:  0 1 1 1 0
             0 0 5 0 0               0 1 5 1 0
             0 0 0 0 0               0 1 1 1 0

[pic1] https://github.com/EoghanOGallchoir/ARC/Images/blue-purple.PNG

#### How my function works

We start by identifying the location of each blue square, aka 5, is in the grid. 
This is done by iterating through row by row, column by column.
Once a blue square is found, the function puts a purple, aka 1, in the surrounding 8 squares, while keeping the blue square blue.

#### Testing

Training grids: 2/2

Test grids: 1/1
                  
### 2.

#### Description

This task takes the entire grid as an input and rotates it around 3 times, completing a box shape. 
This is a bit hard to describe but imaginee a 2x2 grid:0 1 becomes a 4x4 grid of: 0 1 2 0
                        			       2 0                        2 0 0 1
                                                        			  1 0 0 2
                                                 				  0 2 1 0
#### How my function works

We take the grid **x**, and rotate it 90 degrees left to get **x1**.
We then take **x1** and rotate it 90 degrees to get **x2**, and the same with **x2** to get **x3**.
Finally we combine all 4 grids together in the form: x  x1
						     x3 x2
						     
#### Testing

Training grids: 3/3

Test grids: 1/1

### 3.

#### Description

This task takes the direction started by the blue squares (always diagonal) and continues it with green squares until it hits a red wall.
Upon meeting the wall, the green line must then *"bounce"* off that wall and continue its trajectory until it hits the edge of the grid.

#### How my function works

My function starts by finding blue squares along the edge squares of the grid.
Once it finds one it looks for its blue neighbour, and from that it gets one of 4 directions it can go in (NW, SW, SE, NE).
A helper funcion is then called to paint green squares from the blue squares to the red wall, stopping once it gets there.
When we hit the wall, we inverse its direction and begin to paint again, until it hits any of the edges of the grid.

#### Testing

Training grids: 2/3

Test grids: 1/1


### Short Comments

For the most part, I used only basic python features to create my functions. Of course some numpy stuff was done as the grid was read in as a numpy array.
I used the `len()` function to get the row number, but the `x.shape[1]` to get the columns of numpy array x. These were used acrosss all 3 functions, as all needed
me to iterate through them row**x**column.
The second function utilised more basic python function, `reversed()` and `zip()` to rotate the grid(s). The second function also used numpy concatenate to join the lists
the way I wanted them to join. It was a very useful function for doing what I needed it to. The third function is similar to the first where there is basic python used to complete
the task at hand. Loops are heavily featured here, a commonality with the other two functions to go through the every square in the grid.

One difference that the third function has in comparison with the first two is that it uses other functions to solve its problem. These functions `paint_to()` and `paint_fro` were
implemented to try and make the code look a little more elegant, on top of it making sense at the time. They take multiple arguments and again use nested (upon nested) loops to 
execute what I want them to do.







# The Abstraction and Reasoning Corpus (ARC)

This repository contains the ARC task data, as well as a browser-based interface for humans to try their hand at solving the tasks manually.

*"ARC can be seen as a general artificial intelligence benchmark, as a program synthesis benchmark, or as a psychometric intelligence test. It is targeted at both humans and artificially intelligent systems that aim at emulating a human-like form of general fluid intelligence."*

A complete description of the dataset, its goals, and its underlying logic, can be found in: [The Measure of Intelligence](https://arxiv.org/abs/1911.01547).

As a reminder, a test-taker is said to solve a task when, upon seeing the task for the first time, they are able to produce the correct output grid for *all* test inputs in the task (this includes picking the dimensions of the output grid). For each test input, the test-taker is allowed 3 trials (this holds for all test-takers, either humans or AI).


## Task file format

The `data` directory contains two subdirectories:

- `data/training`: contains the task files for training (400 tasks). Use these to prototype your algorithm or to train your algorithm to acquire ARC-relevant cognitive priors.
- `data/evaluation`: contains the task files for evaluation (400 tasks). Use these to evaluate your final algorithm. To ensure fair evaluation results, do not leak information from the evaluation set into your algorithm (e.g. by looking at the evaluation tasks yourself during development, or by repeatedly modifying an algorithm while using its evaluation score as feedback).

The tasks are stored in JSON format. Each task JSON file contains a dictionary with two fields:

- `"train"`: demonstration input/output pairs. It is a list of "pairs" (typically 3 pairs).
- `"test"`: test input/output pairs. It is a list of "pairs" (typically 1 pair).

A "pair" is a dictionary with two fields:

- `"input"`: the input "grid" for the pair.
- `"output"`: the output "grid" for the pair.

A "grid" is a rectangular matrix (list of lists) of integers between 0 and 9 (inclusive). The smallest possible grid size is 1x1 and the largest is 30x30.

When looking at a task, a test-taker has access to inputs & outputs of the demonstration pairs, plus the input(s) of the test pair(s). The goal is to construct the output grid(s) corresponding to the test input grid(s), using 3 trials for each test input. "Constructing the output grid" involves picking the height and width of the output grid, then filling each cell in the grid with a symbol (integer between 0 and 9, which are visualized as colors). Only *exact* solutions (all cells match the expected answer) can be said to be correct.


## Usage of the testing interface

The testing interface is located at `apps/testing_interface.html`. Open it in a web browser (Chrome recommended). It will prompt you to select a task JSON file.

After loading a task, you will enter the test space, which looks like this:

![test space](https://arc-benchmark.s3.amazonaws.com/figs/arc_test_space.png)

On the left, you will see the input/output pairs demonstrating the nature of the task. In the middle, you will see the current test input grid. On the right, you will see the controls you can use to construct the corresponding output grid.

You have access to the following tools:

### Grid controls

- Resize: input a grid size (e.g. "10x20" or "4x4") and click "Resize". This preserves existing grid content (in the top left corner).
- Copy from input: copy the input grid to the output grid. This is useful for tasks where the output consists of some modification of the input.
- Reset grid: fill the grid with 0s.

### Symbol controls

- Edit: select a color (symbol) from the color picking bar, then click on a cell to set its color.
- Select: click and drag on either the output grid or the input grid to select cells.
    - After selecting cells on the output grid, you can select a color from the color picking to set the color of the selected cells. This is useful to draw solid rectangles or lines.
    - After selecting cells on either the input grid or the output grid, you can press C to copy their content. After copying, you can select a cell on the output grid and press "V" to paste the copied content. You should select the cell in the top left corner of the zone you want to paste into.
- Floodfill: click on a cell from the output grid to color all connected cells to the selected color. "Connected cells" are contiguous cells with the same color.

### Answer validation

When your output grid is ready, click the green "Submit!" button to check your answer. We do not enforce the 3-trials rule.

After you've obtained the correct answer for the current test input grid, you can switch to the next test input grid for the task using the "Next test input" button (if there is any available; most tasks only have one test input).

When you're done with a task, use the "load task" button to open a new task.
