START

INPUT Number_of_Disks

IF Number_of_Disks = 1 THEN
    MOVE Source TO Destination
ELSE
    MOVE N-1 Disks FROM Source TO Auxiliary
    MOVE Largest Disk TO Destination
    MOVE N-1 Disks FROM Auxiliary TO Destination
END IF

DISPLAY All Moves

STOP
