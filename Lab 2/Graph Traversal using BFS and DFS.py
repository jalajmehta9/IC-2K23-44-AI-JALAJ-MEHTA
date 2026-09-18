# Graph Traversal using BFS and DFS

from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


# BFS
def bfs(start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            result.append(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

    return result


# DFS
def dfs(node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    result = [node]

    for neighbour in graph[node]:
        if neighbour not in visited:
            result.extend(dfs(neighbour, visited))

    return result


print("BFS Traversal:")
print(bfs('A'))

print("\nDFS Traversal:")
print(dfs('A'))