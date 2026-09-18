# Maze Solver using DFS

maze = [
    ['S', '0', '1', '0', '0'],
    ['1', '0', '1', '0', '1'],
    ['0', '0', '0', '0', '1'],
    ['0', '1', '1', '0', '0'],
    ['0', '0', '0', '1', 'G']
]

rows = len(maze)
cols = len(maze[0])

visited = set()
path = []

def dfs(r, c):
    # Check boundaries
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return False

    # Cannot move through walls or visited cells
    if maze[r][c] == '1' or (r, c) in visited:
        return False

    visited.add((r, c))
    path.append((r, c))

    # Goal reached
    if maze[r][c] == 'G':
        return True

    # Move Up, Down, Left, Right
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in directions:
        if dfs(r + dr, c + dc):
            return True

    # Backtrack
    path.pop()
    return False


# Find start position
for i in range(rows):
    for j in range(cols):
        if maze[i][j] == 'S':
            start = (i, j)

if dfs(start[0], start[1]):
    print("Path found:")
    print(path)

    # Mark path
    for r, c in path:
        if maze[r][c] not in ['S', 'G']:
            maze[r][c] = '*'

    print("\nSolved Maze:")
    for row in maze:
        print(" ".join(row))
else:
    print("No path found.")