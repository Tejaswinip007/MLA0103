BEGIN

    Define graph with edge costs

    Define heuristic h(n) for every node

    Create priority queue OPEN

    Insert start node S into OPEN

    Set:
        g(S) = 0
        f(S) = g(S) + h(S)

    WHILE OPEN is not empty

        Remove node with minimum f(n)

        IF node = Goal G
            Return path and total cost
        END IF

        FOR each neighbour of current node

            Calculate:

                g(new) = g(current) + edge cost

                f(new) = g(new) + h(new)

            Insert new node into OPEN

        END FOR

    END WHILE

END