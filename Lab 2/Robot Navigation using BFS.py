# Robot Navigation using BFS

from collections import deque

grid = [
    ['R', '0', '0', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['0', '0', '0', '0', '0'],
    ['0', '1', '1', '1', '0'],
    ['0', '0', '0', '0', 'G']
]

rows = len(grid)
cols = len(grid[0])


def find_position(symbol):
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == symbol:
                return (i, j)


start = find_position('R')
goal = find_position('G')


def robot_navigation(start, goal):

    queue = deque([(start, [start])])
    visited = {start}

    directions = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    while queue:

        (r, c), path = queue.popleft()

        if (r, c) == goal:
            return path

        for dr, dc in directions:

            nr = r + dr
            nc = c + dc

            if (0 <= nr < rows and
                0 <= nc < cols and
                grid[nr][nc] != '1' and
                (nr, nc) not in visited):

                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))

    return None


path = robot_navigation(start, goal)

if path:
    print("Robot Path:")
    print(path)

    for r, c in path:
        if grid[r][c] not in ['R', 'G']:
            grid[r][c] = '*'

    print("\nGrid after navigation:")

    for row in grid:
        print(" ".join(row))
else:
    print("No path available.")