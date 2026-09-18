# 8-Puzzle Solver using A* Search

import heapq


# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Manhattan Distance
def heuristic(state):

    distance = 0

    for i in range(9):

        if state[i] == 0:
            continue

        current_row = i // 3
        current_col = i % 3

        goal_index = goal.index(state[i])

        goal_row = goal_index // 3
        goal_col = goal_index % 3

        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)

    return distance


# Generate possible moves
def get_neighbors(state):

    neighbors = []

    zero_index = state.index(0)

    row = zero_index // 3
    col = zero_index % 3

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_index = new_row * 3 + new_col

            new_state = list(state)

            # Swap blank with new position
            new_state[zero_index], new_state[new_index] = \
                new_state[new_index], new_state[zero_index]

            neighbors.append(tuple(new_state))

    return neighbors


# A* Algorithm
def solve(start):

    priority_queue = []

    # f(n) = g(n) + h(n)
    heapq.heappush(
        priority_queue,
        (heuristic(start), 0, start, [])
    )

    visited = set()

    while priority_queue:

        f, g, state, path = heapq.heappop(priority_queue)

        if state in visited:
            continue

        visited.add(state)

        new_path = path + [state]

        # Goal reached
        if state == goal:
            return new_path

        for neighbor in get_neighbors(state):

            if neighbor not in visited:

                new_g = g + 1
                new_h = heuristic(neighbor)
                new_f = new_g + new_h

                heapq.heappush(
                    priority_queue,
                    (new_f, new_g, neighbor, new_path)
                )

    return None


# Initial state
start = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)


solution = solve(start)


# Print solution
if solution:

    print("Solution found!")
    print("Number of moves:", len(solution) - 1)

    print("\nSteps:")

    for step, state in enumerate(solution):

        print("\nStep", step)

        for i in range(0, 9, 3):
            print(state[i], state[i + 1], state[i + 2])

else:

    print("No solution found.")