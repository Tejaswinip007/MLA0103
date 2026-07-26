START

Create graph:
1 → 2, 3
2 → 4, 5
3 → NULL
4 → 5
5 → NULL

Create an empty queue.
Create an empty visited list.

Insert node 1 into the queue.

WHILE queue is not empty DO
    Remove the front node.
    IF node is not visited THEN
        Display the node.
        Mark it as visited.
        Insert all adjacent nodes into the queue.
    END IF
END WHILE

STOP
