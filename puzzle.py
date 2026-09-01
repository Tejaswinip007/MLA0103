import heapq

def manhattan(state, goal):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            current_row, current_col = divmod(i, 3)
            goal_index = goal.index(state[i])
            goal_row, goal_col = divmod(goal_index, 3)

            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

    return distance


def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def a_star(start, goal):
    pq = []
    h = manhattan(start, goal)

    heapq.heappush(pq, (h, 0, start, [start]))

    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            return path

        for next_state in get_neighbors(state):
            if next_state not in visited:
                new_g = g + 1
                new_h = manhattan(next_state, goal)
                new_f = new_g + new_h

                heapq.heappush(
                    pq,
                    (new_f, new_g, next_state, path + [next_state])
                )

    return None


def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


# Initial state
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Solve
solution = a_star(start, goal)

if solution:
    print("Solution found!")
    print("Number of moves:", len(solution) - 1)
    print()

    for step, state in enumerate(solution):
        print("Step", step)
        print_puzzle(state)
else:
    print("No solution exists.")