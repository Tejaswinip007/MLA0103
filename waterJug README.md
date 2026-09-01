BEGIN

    Set capacity of Jug A = 4
    Set capacity of Jug B = 3

    Initial state = (0,0)
    Goal = 2 litres

    Create a queue
    Insert (0,0) into queue

    Create VISITED set

    WHILE queue is not empty

        Remove the first state from queue

        IF Jug A contains 2 litres
           OR Jug B contains 2 litres

            Display solution
            STOP

        END IF

        Generate possible states:

            1. Fill Jug A
            2. Fill Jug B
            3. Empty Jug A
            4. Empty Jug B
            5. Pour Jug A into Jug B
            6. Pour Jug B into Jug A

        FOR each new state

            IF state is not visited

                Add state to VISITED
                Add state to queue

            END IF

        END FOR

    END WHILE

    Display "No solution"

END