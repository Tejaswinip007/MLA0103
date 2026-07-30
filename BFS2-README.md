START

Create graph:
1 → 2, 7
2 → 3, 6
3 → 4, 5
7 → 8, 10
8 → 9

Create an empty queue.
Create an empty visited list.

Insert node 1 into the queue.

WHILE queue is not empty DO
    Remove front node.
    IF node is not visited THEN
        Display node.
        Mark node as visited.
        Insert all adjacent nodes into the queue.
    END IF
END WHILE

STOP
