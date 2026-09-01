BEGIN

    Define graph with nodes and edge costs

    S → A = 1
    S → G = 12
    A → B = 3
    A → C = 1
    B → D = 3
    C → D = 1
    C → G = 2
    D → G = 3

    Create a priority queue

    Insert (0, S, [S]) into priority queue

    Create visited/cost table

    WHILE priority queue is not empty

        Remove node having minimum path cost

        IF node was already visited with lower cost
            CONTINUE
        END IF

        Mark node as visited

        IF node is the goal G
            Return path and cost
        END IF

        FOR each neighbour of current node

            Calculate:
                new_cost = current_cost + edge_cost

            Insert neighbour into priority queue
            along with new_cost and updated path

        END FOR

    END WHILE

END