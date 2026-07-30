START

Create graph:
1 → 2, 3
2 → 5, 6
3 → 4, 7
4 → 8
7 → 8

Create an empty queue.
Create an empty visited list.

Insert node 1 into the queue.

WHILE queue is not empty DO
    Remove front node.
    IF node is not visited THEN
        Display node.
        Mark node as visited.
        Insert adjacent nodes into the queue.
    END IF
END WHILE

STOP
