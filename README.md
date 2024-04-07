## About the Project
This repository contains the code for a program that can solve a text-based maze through either BFS or DFS. This is based on the CS50AI Week 0 problem involving mazes, but I wrote all of the code for this program myself in order to get a better handle on object-oriented programming and search algorithms.

## Usage
To use this program simply run the maze.py file. You will be prompted whether you would like to use Breadth-First Search or Depth-First Search, as well as whether you would like to highlight the explored portions of the maze in the result. The program will then run, and if a solution exists then the time taken to identify the solution and the solution itself will be printed, as well as the explored portion if requested. 

This repository has a large example maze, but if you would like to create your own maze simply edit the maze.txt file prior to running the program. You can draw your own using "#" characters for walls, "A" for the starting point, and "B" for the ending point, or you could visit this website (https://www.dcode.fr/maze-generator) and generate one with the same specifications for the walls of the maze of any size. Simply place the "A" character and "B" character anywhere you'd like in the maze, floating wall or not, and the program will find a solution.

## BFS vs. DFS
Breadth-First Search searches for the goal state by checking all of the nodes closest to the initial state and branching outwards, first checking all nodes one unit away, then all nodes that are two units away, etc. For the purposes of implementing this algorithm, a Queue data structure was used to keep track of unexplored states, following the principle of First-In-First-Out (FIFO). 

Depth-First Search, by contrast, uses a stack data structure to keep track of unexplored states, following the principle of Last-In-First-Out. In practice, this means that this search algorithm will pick a lead in the maze, so to speak, and follow it until it literally cannot make another move before pursuing a different lead.

Both of these algorithms are useful, and have different purposes. In the example of the maze, if the start and end point are a maximum distance from one another, DFS will almost certainly find the solution than BFS, which will be forced to explore the entire maze before identifying the solution. In contrast, DFS would fail to identify the solution as quickly as BFS in situations where the startpoint and endpoint are closer to one another most of the time, as it would likely explore many unnecessary portions of the maze, prioritizing depth, before identifying the endpoint.
