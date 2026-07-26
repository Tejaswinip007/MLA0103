START

Create graph:
0 → 1
1 → 3
3 → 4, 2
2 → 1
4 → 5
5 → 7
7 → 6
6 → 4

Mark all nodes as unvisited.

Call DFS(0)

DFS(Node)
    Mark node as visited.
    Display node.
    Recursively visit every adjacent node.

STOP
