BEGIN

    Define initial state
    Define goal state

    Calculate heuristic using Manhattan Distance

    Insert initial state into priority queue

    WHILE priority queue is not empty

        Remove state having minimum f(n)

        IF state is the goal
            Display solution
            STOP
        END IF

        Find position of blank tile

        Generate all possible moves:
            Up
            Down
            Left
            Right

        FOR each possible new state

            Calculate:
                g(n) = cost from initial state
                h(n) = Manhattan distance
                f(n) = g(n) + h(n)

            Insert new state into priority queue

        END FOR

    END WHILE

    Display "No solution"

END