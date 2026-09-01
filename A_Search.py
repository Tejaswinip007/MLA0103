import heapq

def a_star(graph, heuristic, start, goal):
    # Priority queue: (f, g, node, path)
    pq = [(heuristic[start], 0, start, [start])]

    # Minimum cost to reach each node
    g_cost = {}

    while pq:
        f, g, node, path = heapq.heappop(pq)

        # Skip if a cheaper path already exists
        if node in g_cost and g_cost[node] <= g:
            continue

        g_cost[node] = g

        # Goal reached
        if node == goal:
            return path, g

        # Explore neighbours
        for neighbour, edge_cost in graph[node]:
            new_g = g + edge_cost
            new_f = new_g + heuristic[neighbour]

            heapq.heappush(
                pq,
                (new_f, new_g, neighbour, path + [neighbour])
            )

    return None, float("inf")


# Graph
graph = {
    'S': [('A', 3), ('D', 4)],
    'A': [('S', 3), ('D', 5), ('B', 4)],
    'B': [('A', 4), ('E', 5), ('C', 4)],
    'C': [('B', 4)],
    'D': [('S', 4), ('A', 5), ('E', 2)],
    'E': [('D', 2), ('B', 5), ('F', 4)],
    'F': [('E', 4), ('G', 3.5)],
    'G': [('F', 3.5)]
}

# Heuristic values
heuristic = {
    'S': 11,
    'A': 10.1,
    'B': 5.8,
    'C': 2.4,
    'D': 9.2,
    'E': 7.1,
    'F': 3.5,
    'G': 0
}

# Start and goal
start = 'S'
goal = 'G'

# Perform A* Search
path, cost = a_star(graph, heuristic, start, goal)

print("Optimal Path:", " -> ".join(path))
print("Minimum Cost:", cost)