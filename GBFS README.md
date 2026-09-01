BEGIN

    Define graph

    Define heuristic value h(n) for each node

    Create a priority queue

    Insert START node into priority queue
    using its heuristic value

    Create an empty VISITED set

    WHILE priority queue is not empty

        Remove the node having the
        smallest heuristic value

        IF node is already visited
            CONTINUE
        END IF

        Add node to VISITED

        IF node = GOAL
            Return the path
        END IF

        FOR each neighbour of current node

            IF neighbour is not visited
                Insert neighbour into priority queue
                using h(neighbour)
            END IF

        END FOR

    END WHILE

END