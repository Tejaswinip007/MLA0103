START

INPUT Goal

CHECK Goal

IF Goal is a Fact THEN
    DISPLAY "Goal Proven"
ELSE
    FIND Matching Rule
    VERIFY All Conditions
    IF Conditions are True THEN
        DISPLAY "Goal Proven"
    ELSE
        DISPLAY "Goal Not Proven"
    END IF
END IF

STOP
