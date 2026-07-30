START

Create graph:
1 → 2, 3
2 → 4, 5
3 → NULL
4 → 5
5 → NULL

Mark all nodes as unvisited.

Call DFS(1)

DFS(Node)
    Mark node as visited.
    Display node.
    Visit every adjacent node recursively if not visited.

STOP
