BEGIN

    Set N = 8

    Create an empty 8 × 8 chessboard

    FUNCTION IS_SAFE(row, column)

        Check whether another queen exists
        in the same column

        Check upper-left diagonal

        Check upper-right diagonal

        IF any queen attacks this position
            RETURN FALSE
        ELSE
            RETURN TRUE

    END FUNCTION


    FUNCTION SOLVE(row)

        IF row == 8
            RETURN TRUE
        END IF

        FOR column = 0 to 7

            IF IS_SAFE(row, column)

                Place queen at (row, column)

                IF SOLVE(row + 1)
                    RETURN TRUE
                END IF

                Remove queen
                BACKTRACK

            END IF

        END FOR

        RETURN FALSE

    END FUNCTION


    Call SOLVE(0)

    IF solution exists
        Display chessboard
    ELSE
        Display "No solution"

END