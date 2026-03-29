# AI_-_ML-PROJECT
Maze Solver for Robotics Navigation using DFS
Project Overview:-
In real-world robotics, autonomous navigation in unknown or complex environments is a significant challenge. This project focuses on designing a maze-solving system that enables a robot to explore and navigate through an unknown environment using the Depth First Search (DFS) algorithm.

This implementation demonstrates how an autonomous agent can make decisions, avoid obstacles, and backtrack when hitting a dead end to eventually reach a target destination.

Features:-
Pure Python Implementation: No external libraries (like NumPy or OpenCV) are required, making it lightweight and compatible with any standard Python environment.

Autonomous Pathfinding: Uses DFS to explore available paths.

Obstacle Avoidance: Logic to detect and bypass "walls" or restricted zones.

Visual Output: Generates a text-based occupancy grid showing the final path taken by the robot.

Technical Approach: Depth First Search (DFS)
The project utilizes a stack-based DFS approach. The "robot" explores as far as possible along each branch before backtracking.

Project Structure-
To show the development progress, the project was committed in four distinct stages:

1] Initialization of the MazeSolver class and coordinate detection for Start (S) and End (E).

2] Implementation of movement constraints and boundary-checking logic.

3] Integration of the core DFS algorithm logic.

4] Final visualization and execution script for the terminal.

Output Representation:-
The output displays the maze grid where:

S: Starting Point

E: Exit/Goal

1: Obstacle/Wall

0: Open Path

*: Path taken by the Robot

Example Output:

Plaintext
S * 1 0 0
1 * 1 0 1
0 * * * *
0 1 1 1 *
0 0 0 1 E

Future Scope:-
Implementation of Breadth-First Search (BFS) for shortest-path guarantees.

Integration with A* Algorithm for weighted pathfinding.

Adapting the logic for physical hardware using sensors like LiDAR or Ultrasonics.

