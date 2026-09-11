from collections import deque


def is_valid(state):
    m_left, c_left, boat = state

    m_right = 3 - m_left
    c_right = 3 - c_left

    # Check valid number of people
    if m_left < 0 or m_left > 3:
        return False

    if c_left < 0 or c_left > 3:
        return False

    # Check left side
    if m_left > 0 and c_left > m_left:
        return False

    # Check right side
    if m_right > 0 and c_right > m_right:
        return False

    return True


def get_next_states(state):
    m_left, c_left, boat = state

    moves = [
        (1, 0, "1 Missionary"),
        (2, 0, "2 Missionaries"),
        (0, 1, "1 Cannibal"),
        (0, 2, "2 Cannibals"),
        (1, 1, "1 Missionary and 1 Cannibal")
    ]

    next_states = []

    for m, c, description in moves:

        if boat == 0:
            # Boat moves from left to right
            new_state = (m_left - m, c_left - c, 1)
            direction = "Left -> Right"

        else:
            # Boat moves from right to left
            new_state = (m_left + m, c_left + c, 0)
            direction = "Right -> Left"

        if is_valid(new_state):
            next_states.append(
                (new_state, description + " : " + direction)
            )

    return next_states


def missionaries_and_cannibals():

    initial_state = (3, 3, 0)
    goal_state = (0, 0, 1)

    queue = deque([initial_state])

    visited = {initial_state}

    parent = {}
    action = {}

    while queue:

        current = queue.popleft()

        if current == goal_state:

            path = []

            while current != initial_state:
                path.append((current, action[current]))
                current = parent[current]

            path.reverse()

            print("\nSolution:")
            print("Initial State:", initial_state)

            for state, act in path:
                print(act)
                print("State:", state)

            return

        for next_state, act in get_next_states(current):

            if next_state not in visited:

                visited.add(next_state)
                queue.append(next_state)

                parent[next_state] = current
                action[next_state] = act

    print("No solution found.")


missionaries_and_cannibals()