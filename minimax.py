def minimax(node, depth, maximizing):
    # Leaf node
    if isinstance(node, int):
        return node

    if maximizing:
        best = float('-inf')

        for child in node:
            value = minimax(child, depth + 1, False)
            best = max(best, value)

        return best

    else:
        best = float('inf')

        for child in node:
            value = minimax(child, depth + 1, True)
            best = min(best, value)

        return best


# Game tree
tree = [
    [
        [3, 2],
        [5, 6]
    ],
    [
        [9, 1],
        [7, 5]
    ]
]

# Root A is MAX
result = minimax(tree, 0, True)

print("Minimax Value:", result)