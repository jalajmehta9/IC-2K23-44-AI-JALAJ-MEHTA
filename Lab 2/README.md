# AI Search and Problem-Solving Algorithms

This repository contains five Python programs demonstrating fundamental Artificial Intelligence (AI) search techniques through classic puzzles, graph traversal, maze solving, robot navigation, and route planning.

## Programs Included

| File | Problem | Algorithm |
|---|---|---|
| `8-Puzzle Solver.py` | Find a sequence of board states leading to the 8-puzzle goal | A* Search with Manhattan Distance |
| `Graph Traversal using BFS and DFS.py` | Traverse a directed graph from a starting node | Breadth-First Search (BFS) and Depth-First Search (DFS) |
| `Maze Solver using DFS.py` | Find a path from the start cell to the goal in a maze | Depth-First Search (DFS) with backtracking |
| `Robot Navigation using BFS.py` | Find a path for a robot through a grid containing obstacles | Breadth-First Search (BFS) |
| `Route Planning using BFS.py` | Find a route between two cities in a graph | Breadth-First Search (BFS) |

## Requirements

- Python 3.x
- No third-party packages are required.
- The programs use Python standard-library modules:
  - `collections.deque` for BFS queues.
  - `heapq` for the A* priority queue.

## How to Run

Open a terminal in the folder containing the files and run each program separately:

```bash
python "8-Puzzle Solver.py"
python "Graph Traversal using BFS and DFS.py"
python "Maze Solver using DFS.py"
python "Robot Navigation using BFS.py"
python "Route Planning using BFS.py"
```

On systems where Python 3 is invoked using `python3`, replace `python` with `python3`.

---

## 1. 8-Puzzle Solver using A* Search

**File:** `8-Puzzle Solver.py`

### Objective

Solve the 8-puzzle, a 3 × 3 sliding-tile puzzle containing the numbers 1 to 8 and one blank space represented by `0`. The aim is to transform the initial board into the goal board by moving the blank space.

### Initial and Goal States

Initial state:

```text
1 2 3
4 0 6
7 5 8
```

Goal state:

```text
1 2 3
4 5 6
7 8 0
```

### Algorithm: A* Search

The program uses A* search to explore board configurations. A* evaluates states using:

```text
f(n) = g(n) + h(n)
```

- `g(n)` is the number of moves made from the initial state.
- `h(n)` is the estimated remaining cost to reach the goal.
- `f(n)` is the combined score used to prioritize states.

The heuristic is **Manhattan Distance**. For every numbered tile, it calculates the horizontal and vertical distance between the tile's current position and its goal position. The blank tile (`0`) is excluded from the calculation.

### Main Functions

- `heuristic(state)`: Calculates the Manhattan Distance for a board state.
- `get_neighbors(state)`: Generates valid neighboring states by moving the blank space up, down, left, or right.
- `solve(start)`: Runs A* using a priority queue, tracks visited states, and returns the solution path when the goal is reached.

### Output

If a solution is found, the program prints the success message, the number of moves, and every board state in the solution, beginning with the initial state and ending with the goal state. Otherwise, it prints `No solution found.`

---

## 2. Graph Traversal using BFS and DFS

**File:** `Graph Traversal using BFS and DFS.py`

### Objective

Traverse a graph from a starting node and display the order in which nodes are visited using two different search techniques.

### Graph Representation

The graph is represented using an adjacency list stored in a Python dictionary:

```python
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
```

Each key represents a node, and its list contains the neighboring nodes.

### Algorithms

**Breadth-First Search (BFS)**

BFS explores the graph level by level. It uses a queue (`deque`) to process nodes in first-in, first-out order. A `visited` set prevents nodes from being processed more than once.

**Depth-First Search (DFS)**

DFS explores one branch as deeply as possible before returning to explore another branch. This implementation uses recursion and a `visited` set.

### Main Functions

- `bfs(start)`: Traverses the graph using a queue and returns the traversal order.
- `dfs(node, visited=None)`: Traverses the graph recursively and returns the traversal order.

Both traversals start from node `A`.

### Expected Output

```text
BFS Traversal:
['A', 'B', 'C', 'D', 'E', 'F']

DFS Traversal:
['A', 'B', 'D', 'E', 'F', 'C']
```

The traversal order follows the neighbor order in the graph's adjacency lists.

---

## 3. Maze Solver using DFS

**File:** `Maze Solver using DFS.py`

### Objective

Find a path from the starting cell (`S`) to the goal cell (`G`) in a 2D maze. Walls are represented by `1`, while open cells are represented by `0`.

### Maze Representation

The maze is stored as a 5 × 5 list:

```text
S 0 1 0 0
1 0 1 0 1
0 0 0 0 1
0 1 1 0 0
0 0 0 1 G
```

### Algorithm: Depth-First Search (DFS)

The program uses recursive DFS to explore the maze. From each cell, it attempts to move up, down, left, and right.

It checks that a move:
- Stays within the maze boundaries.
- Does not enter a wall (`1`).
- Does not revisit a cell already in the `visited` set.

The current route is stored in the `path` list. If a route does not lead to the goal, the program backtracks by removing the last cell from the path.

### Main Logic

- `dfs(r, c)`: Checks whether a path to the goal can be found from the current row and column.
- The program searches the maze for the starting cell marked `S`.
- If DFS reaches `G`, it prints the path and marks the path cells with `*` in the displayed maze.

### Output

If a route is found, the program displays the list of coordinates in the path and the solved maze. If no route is found, it prints `No path found.`

---

## 4. Robot Navigation using BFS

**File:** `Robot Navigation using BFS.py`

### Objective

Navigate a robot from its starting position (`R`) to a goal position (`G`) in a 2D grid while avoiding obstacles.

### Grid Representation

The environment is represented as a 5 × 5 grid:

```text
R 0 0 1 0
1 1 0 1 0
0 0 0 0 0
0 1 1 1 0
0 0 0 0 G
```

- `R`: Robot's starting position.
- `G`: Goal position.
- `0`: Free cell.
- `1`: Obstacle.

### Algorithm: Breadth-First Search (BFS)

The program uses BFS to explore reachable grid cells. Since BFS explores positions in increasing order of the number of moves, it finds a path with the fewest moves when every permitted move has equal cost.

The robot can move up, down, left, or right. It cannot move outside the grid, enter an obstacle, or revisit a position already in the `visited` set.

### Main Functions

- `find_position(symbol)`: Finds the coordinates of the specified grid symbol.
- `robot_navigation(start, goal)`: Uses a queue to explore possible positions and stores the path associated with each queued position.

### Output

If a path is found, the program prints the robot's path as a list of coordinates. It then marks the path cells with `*` and displays the updated grid. If no route is available, it prints `No path available.`

---

## 5. Route Planning using BFS

**File:** `Route Planning using BFS.py`

### Objective

Find a route between two cities using a graph in which cities are represented as nodes and direct connections are represented as edges.

### Graph Representation

The program stores the city connections in an adjacency list:

```python
graph = {
    "Indore": ["Bhopal", "Ujjain"],
    "Bhopal": ["Indore", "Jabalpur", "Sagar"],
    "Ujjain": ["Indore", "Ratlam"],
    "Jabalpur": ["Bhopal", "Katni"],
    "Sagar": ["Bhopal"],
    "Ratlam": ["Ujjain", "Neemuch"],
    "Katni": ["Jabalpur"],
    "Neemuch": ["Ratlam"]
}
```

The starting city is `Indore`, and the destination is `Jabalpur`.

### Algorithm: Breadth-First Search (BFS)

The program uses a queue containing routes. Each route is a list of cities, and the last city in the route is the current city being explored.

BFS checks whether the current city is the destination. If it is, the route is returned. Otherwise, the program adds routes through unvisited neighboring cities to the queue.

A `visited` set helps prevent repeated exploration of cities.

### Main Function

- `find_route(start, destination)`: Searches the graph using BFS and returns a route from the starting city to the destination. It returns `None` if no route is found.

### Expected Output

```text
Route found:
Indore -> Bhopal -> Jabalpur
```

This is the route produced by the current graph and neighbor ordering.

---

## Concepts Demonstrated

| AI / Programming Concept | Demonstrated In |
|---|---|
| State-space representation | 8-Puzzle Solver |
| Heuristic function | 8-Puzzle Solver |
| Manhattan Distance | 8-Puzzle Solver |
| A* Search and priority queue | 8-Puzzle Solver |
| Graph representation using adjacency lists | Graph Traversal and Route Planning |
| Breadth-First Search (BFS) | Graph Traversal, Robot Navigation, Route Planning |
| Depth-First Search (DFS) | Graph Traversal and Maze Solver |
| Recursion | Graph Traversal and Maze Solver |
| Backtracking | Maze Solver |
| Visited sets | All search-based programs |
| Path tracking | 8-Puzzle Solver, Maze Solver, Robot Navigation, Route Planning |
| Grid-based navigation | Maze Solver and Robot Navigation |

## BFS, DFS, and A* at a Glance

| Algorithm | Search Strategy | Data Structure / Technique | Used In |
|---|---|---|---|
| BFS | Explores level by level | Queue | Graph traversal, robot navigation, route planning |
| DFS | Explores deeply before backtracking | Recursion | Graph traversal, maze solving |
| A* | Prioritizes states using path cost and heuristic | Priority queue | 8-puzzle solving |

## Conclusion

These five programs demonstrate how search algorithms can solve different AI problem-solving tasks. BFS is used for level-by-level exploration and shortest paths in unweighted graphs, DFS explores paths deeply and uses backtracking in the maze, and A* combines the cost already incurred with a heuristic estimate to solve the 8-puzzle.

Together, the programs provide practical examples of graph search, state-space exploration, pathfinding, heuristic search, and navigation using Python.
