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

Create an empty queue.
Create an empty visited list.

Insert node 0 into the queue.

WHILE queue is not empty DO
    Remove front node.
    IF node is not visited THEN
        Display node.
        Mark node as visited.
        Insert adjacent nodes into the queue.
    END IF
END WHILE

STOP
