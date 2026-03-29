# Maze Solver for Robotics Navigation using DFS

## Project Overview
In real-world robotics, autonomous navigation in unknown or complex environments is a significant challenge. This project focuses on designing a maze-solving system that enables a robot to explore and navigate through an unknown environment using the **Depth First Search (DFS)** algorithm.

This implementation demonstrates how an autonomous agent can make decisions, avoid obstacles, and backtrack when hitting a dead end to eventually reach a target destination.

---
## Student Details

| Field | Details |
|---|---|
| Name | `Shashank Kumar` |
| Registration Number | `25BME10012` |
| Branch | MECHANICAL core |
| Subject | Fundamentals of AI/ML (CSA2001) |
| Academic Year | 2026 |

---

## Features
* **Pure Python Implementation**: No external libraries are required, making it lightweight and compatible with any standard Python environment.
* **Autonomous Pathfinding**: Uses DFS to explore available paths.
* **Obstacle Avoidance**: Logic to detect and bypass "walls" or restricted zones.
* **Visual Output**: Generates a text-based occupancy grid showing the final path taken by the robot.

---

## Technical Approach: Depth First Search (DFS)
The project utilizes a stack-based DFS approach. The "robot" explores as far as possible along each branch before backtracking. 

---

## Project Structure
To show the development progress, the project was committed in four distinct stages:

* **1]**: Initialization of the `MazeSolver` class and coordinate detection for Start (S) and End (E).
* **2]**: Implementation of movement constraints and boundary-checking logic.
* **3]**: Integration of the core DFS algorithm logic.
* **4]**: Final visualization and execution script for the terminal.

---

## How to Run
1.  Ensure you have **Python 3.x** installed.
2.  Clone this repository:
    ```bash
    git clone [https://github.com/your-username/maze-solver-robotics.git](https://github.com/your-username/maze-solver-robotics.git)
    ```
3.  Navigate to the project directory:
    ```bash
    cd maze-solver-robotics
    ```
4.  Run the script:
    ```bash
    python maze_solver.py
    ```

---

## Output Representation
The output displays the maze grid where:
* `S`: Starting Point
* `E`: Exit/Goal
* `1`: Obstacle/Wall
* `0`: Open Path
* `*`: Path taken by the Robot

**Example Output:**
```text
S * 1 0 0
1 * 1 0 1
0 * * * *
0 1 1 1 *
0 0 0 1 E

