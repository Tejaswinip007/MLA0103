import heapq

def greedy_best_first_search(graph, heuristic, start, goal):
    # Priority queue: (heuristic value, node, path)
    pq = [(heuristic[start], start, [start])]

    visited = set()

    while pq:
        h, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        # Goal reached
        if node == goal:
            return path

        # Add unvisited neighbours
        for neighbour in graph[node]:
            if neighbour not in visited:
                heapq.heappush(
                    pq,
                    (heuristic[neighbour],
                     neighbour,
                     path + [neighbour])
                )

    return None


# Graph
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'E', 'F'],
    'D': ['A', 'F'],
    'E': ['B', 'C', 'H'],
    'F': ['C', 'D', 'G'],
    'H': ['E'],
    'G': ['F']
}

# Heuristic values
heuristic = {
    'A': 40,
    'B': 32,
    'C': 25,
    'D': 35,
    'E': 19,
    'F': 17,
    'G': 0,
    'H': 10
}

# Start and goal
start = 'A'
goal = 'G'

# Perform GBFS
path = greedy_best_first_search(graph, heuristic, start, goal)

print("GBFS Path:", " -> ".join(path))