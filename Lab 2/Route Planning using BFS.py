# Route Planning using BFS

from collections import deque

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


def find_route(start, destination):

    queue = deque([[start]])
    visited = set()

    while queue:

        route = queue.popleft()
        city = route[-1]

        if city == destination:
            return route

        if city in visited:
            continue

        visited.add(city)

        for neighbour in graph[city]:

            if neighbour not in visited:
                new_route = route + [neighbour]
                queue.append(new_route)

    return None


start = "Indore"
destination = "Jabalpur"

route = find_route(start, destination)

if route:
    print("Route found:")
    print(" -> ".join(route))
else:
    print("No route found.")