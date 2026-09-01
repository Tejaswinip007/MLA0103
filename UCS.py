import heapq

def uniform_cost_search(graph, start, goal):
    # Priority queue: (cost, current_node, path)
    pq = [(0, start, [start])]

    # Store the minimum cost found for each node
    visited = {}

    while pq:
        cost, node, path = heapq.heappop(pq)

        # If this node was already reached with a lower cost
        if node in visited and visited[node] <= cost:
            continue

        visited[node] = cost

        # Goal reached
        if node == goal:
            return path, cost

        # Explore neighbouring nodes
        for neighbor, edge_cost in graph[node]:
            new_cost = cost + edge_cost
            heapq.heappush(
                pq,
                (new_cost, neighbor, path + [neighbor])
            )

    return None, float("inf")


# Graph
graph = {
    'S': [('A', 1), ('G', 12)],
    'A': [('B', 3), ('C', 1)],
    'B': [('D', 3)],
    'C': [('D', 1), ('G', 2)],
    'D': [('G', 3)],
    'G': []
}

# Start and goal
start = 'S'
goal = 'G'

# Perform UCS
path, cost = uniform_cost_search(graph, start, goal)

# Display result
print("Optimal Path:", " -> ".join(path))
print("Minimum Cost:", cost)