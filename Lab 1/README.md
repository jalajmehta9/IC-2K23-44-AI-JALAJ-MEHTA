# AI Problem-Solving Programs

This repository contains four Python programs demonstrating classic problems and concepts used in Artificial Intelligence (AI):

1. Water Jug Problem
2. Missionaries and Cannibals Problem
3. Vacuum Cleaner Problem
4. State Space Representation using the 8-Puzzle

Each program demonstrates a different problem-solving approach, including state representation, action selection, constraint checking, and search.

## Repository Contents

| File | Description |
|---|---|
| `water_jug.py` | Uses 4-litre and 3-litre jugs to measure exactly 2 litres of water. |
| `Missionaries_and_Cannibals_Problem.py` | Uses Breadth-First Search (BFS) to find a valid solution to the Missionaries and Cannibals problem. |
| `Vacuum Cleaner Problem.py` | Simulates a vacuum agent that cleans two rooms based on their initial conditions. |
| `State Space Representation.py` | Represents the 8-puzzle and generates the valid next states from a given board configuration. |

## Requirements

- Python 3.x
- No third-party Python packages are required. The Missionaries and Cannibals program uses `deque` from Python's standard-library `collections` module.

## How to Run

Open a terminal in the project directory and run the programs individually.

```bash
python water_jug.py
python Missionaries_and_Cannibals_Problem.py
python "Vacuum Cleaner Problem.py"
python "State Space Representation.py"
```

Depending on your installation, you may need to use `python3` instead of `python`.

---

## 1. Water Jug Problem

### Objective

Measure exactly **2 litres of water** using two unmarked jugs:

- Jug 1 has a capacity of 4 litres.
- Jug 2 has a capacity of 3 litres.

Both jugs initially contain 0 litres of water.

### Approach

The program uses a `while` loop and conditional statements to perform three operations:

- **Fill:** If the 4-litre jug is empty, fill it completely.
- **Empty:** If the 3-litre jug is full, empty it.
- **Transfer:** Pour water from the 4-litre jug into the 3-litre jug until the source jug is empty or the destination jug is full.

The transfer amount is calculated using:

```python
transfer = min(a, jug2 - b)
```

Here, `a` is the amount of water in the first jug, and `jug2 - b` is the remaining capacity in the second jug.

### Expected State Sequence

The program prints the following jug quantities:

| Step | 4-litre jug | 3-litre jug | Operation |
|---|---:|---:|---|
| Initial | 0 | 0 | Both jugs are empty |
| 1 | 4 | 0 | Fill the 4-litre jug |
| 2 | 1 | 3 | Transfer water into the 3-litre jug |
| 3 | 1 | 0 | Empty the 3-litre jug |
| 4 | 0 | 1 | Transfer the remaining water |
| 5 | 4 | 1 | Fill the 4-litre jug |
| 6 | 2 | 3 | Transfer water until the 3-litre jug is full |

**Result:** The 4-litre jug contains exactly 2 litres, and the program prints `Target achieved!`.

---

## 2. Missionaries and Cannibals Problem

### Objective

Transport three missionaries and three cannibals from the left bank of a river to the right bank using a boat.

The boat can carry one or two people at a time. Missionaries must never be outnumbered by cannibals on either bank when missionaries are present.

### State Representation

Each state is represented as a tuple:

```python
(m_left, c_left, boat)
```

Where:

- `m_left` is the number of missionaries on the left bank.
- `c_left` is the number of cannibals on the left bank.
- `boat` indicates the boat's position: `0` for the left bank and `1` for the right bank.

The initial state is:

```python
(3, 3, 0)
```

The goal state is:

```python
(0, 0, 1)
```

### Approach

The program uses **Breadth-First Search (BFS)** to explore possible states and find a path from the initial state to the goal state.

The main functions are:

- `is_valid(state)`: Checks that the number of people is within the allowed range and that missionaries are not outnumbered by cannibals on either bank when missionaries are present.
- `get_next_states(state)`: Generates possible next states using the permitted boat movements and keeps only valid states.
- `missionaries_and_cannibals()`: Performs BFS using a queue, tracks visited states, and stores parent states and actions to reconstruct the solution.

### Possible Boat Movements

- 1 Missionary
- 2 Missionaries
- 1 Cannibal
- 2 Cannibals
- 1 Missionary and 1 Cannibal

### Search Details

The implementation uses:

- `deque` as the BFS queue.
- A `visited` set to avoid exploring the same state more than once.
- A `parent` dictionary to remember the state from which each state was reached.
- An `action` dictionary to record the move used to reach each state.

When the goal state is found, the program reconstructs and prints the sequence of actions and states. If no solution is found, it prints `No solution found.`

---

## 3. Vacuum Cleaner Problem

### Objective

Simulate a vacuum-cleaning agent operating in two rooms: Room A and Room B. The rooms can each be either `Clean` or `Dirty`, and the vacuum starts in either room.

The goal is to make both rooms clean.

### User Input

The program asks for:

1. The initial status of Room A (`Clean` or `Dirty`).
2. The initial status of Room B (`Clean` or `Dirty`).
3. The vacuum's initial location (`A` or `B`).

### Approach

The program uses conditional statements to decide what the vacuum should do.

- If the vacuum starts in Room A and Room A is dirty, it cleans Room A.
- If Room B is dirty, it moves from A to B and cleans Room B.
- If the vacuum starts in Room B and Room B is dirty, it cleans Room B.
- If Room A is dirty, it moves from B to A and cleans Room A.
- If the starting location is neither A nor B, it displays `Invalid location!`.

The program displays the initial state, the actions performed, and the final state. It prints `Goal Achieved: Both rooms are clean.` when both rooms are clean.

### AI Concept

This program illustrates a simple **goal-based agent**: it observes the room conditions and its location, then performs actions intended to reach the goal state.

---

## 4. State Space Representation using the 8-Puzzle

### Objective

Represent the 8-puzzle as a state space and generate the possible next states from a given board configuration.

The 8-puzzle consists of a 3 × 3 board containing tiles numbered 1 to 8 and one empty position, represented by `0`.

### Initial and Goal States

The initial state is:

```text
1 2 3
4 0 6
7 5 8
```

The goal state is:

```text
1 2 3
4 5 6
7 8 0
```

### State Representation

Each board is stored as a tuple containing nine values. The value `0` represents the blank space.

### Approach

The program uses the following functions:

- `print_state(state)`: Displays the tuple as a 3 × 3 board.
- `get_next_states(state)`: Finds the blank tile's position and generates the board configurations that can be reached by moving it one position.

The blank tile can move:

- Up, if it is not in the top row.
- Down, if it is not in the bottom row.
- Left, if it is not in the leftmost column.
- Right, if it is not in the rightmost column.

For each permitted move, the program swaps the blank tile (`0`) with the adjacent tile and stores the resulting board as a tuple.

### Output

The program displays:

1. The initial state.
2. The goal state.
3. Every possible next state from the initial state, along with the corresponding move.

**Note:** This program generates the immediate successor states of the initial board. It does not implement a complete search algorithm to find a path from the initial state to the goal state.

---

## Concepts Demonstrated

| Concept | Program |
|---|---|
| Conditional statements and loops | Water Jug Problem |
| State representation and constraints | Missionaries and Cannibals Problem |
| Breadth-First Search (BFS) | Missionaries and Cannibals Problem |
| Queue, set, and dictionaries | Missionaries and Cannibals Problem |
| Goal-based agent and action selection | Vacuum Cleaner Problem |
| State-space representation | 8-Puzzle |
| Successor-state generation | 8-Puzzle |

## Conclusion

These four programs demonstrate foundational AI problem-solving concepts through classic examples. They cover representing a problem as states, defining valid actions, checking constraints, generating successor states, and using BFS to search for a solution.

The programs are independent and can be executed separately using Python 3.
