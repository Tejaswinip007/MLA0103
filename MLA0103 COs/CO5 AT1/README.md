# Student Academic Advisory Expert System

## Overview

This project is a rule-based expert system developed using SWI-Prolog. The system analyzes student academic information and provides suitable academic recommendations.

## Features

- Student knowledge base using Prolog facts
- Academic status identification using production rules
- Academic recommendations
- Forward chaining demonstration
- Backward chaining demonstration
- Unification demonstration
- Backtracking demonstration
- Multiple student test cases

## Knowledge Base

The system uses the following information:

- Attendance
- Internal marks
- Assignment performance
- Learning difficulties
- Previous academic performance

## How to Run

1. Install SWI-Prolog.
2. Open SWI-Prolog.
3. Load the program:

   ?- [expert_system].

4. Start the system:

   ?- start.

5. Enter a student name such as:

   student1.

## Example Queries

### Complete Analysis

?- analyze(student1).

### Backward Chaining

?- diagnose(student1, Advice).

### Forward Chaining

?- retractall(known(_)).
?- forward_chain.

### Unification

?- attendance(Student, low).

### Logical Inference

?- academic_status(student1, Status).

## Technologies Used

- SWI-Prolog
- Visual Studio Code
- GitHub

## Author

Tejaswini
