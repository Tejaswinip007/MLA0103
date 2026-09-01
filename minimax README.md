MINIMAX(node, maximizing_player)

    IF node is a leaf
        RETURN value of node
    END IF

    IF maximizing_player = TRUE

        best = -∞

        FOR each child of node
            value = MINIMAX(child, FALSE)
            best = MAX(best, value)
        END FOR

        RETURN best

    ELSE

        best = +∞

        FOR each child of node
            value = MINIMAX(child, TRUE)
            best = MIN(best, value)
        END FOR

        RETURN best

    END IF