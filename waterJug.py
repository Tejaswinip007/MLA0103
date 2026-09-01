from collections import deque

def water_jug():
    capacity_a = 4
    capacity_b = 3
    goal = 2

    start = (0, 0)

    queue = deque()
    queue.append((start, []))

    visited = set()
    visited.add(start)

    while queue:
        (a, b), path = queue.popleft()

        # Goal check
        if a == goal or b == goal:
            print("Solution Found!")
            for step in path + [(a, b)]:
                print(step)
            return

        states = []

        # Fill Jug A
        states.append(((capacity_a, b), "Fill Jug A"))

        # Fill Jug B
        states.append(((a, capacity_b), "Fill Jug B"))

        # Empty Jug A
        states.append(((0, b), "Empty Jug A"))

        # Empty Jug B
        states.append(((a, 0), "Empty Jug B"))

        # Pour A -> B
        amount = min(a, capacity_b - b)
        states.append(((a - amount, b + amount), "Pour A -> B"))

        # Pour B -> A
        amount = min(b, capacity_a - a)
        states.append(((a + amount, b - amount), "Pour B -> A"))

        for new_state, action in states:
            if new_state not in visited:
                visited.add(new_state)
                queue.append(
                    (new_state, path + [new_state])
                )

                print(action, ":", new_state)


water_jug()