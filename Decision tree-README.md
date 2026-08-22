# Decision Tree Using ID3 - Question 1

## Description

This Python program implements the ID3 (Iterative Dichotomiser 3) Decision Tree algorithm for Question 1.

The program:

- Calculates Entropy
- Calculates Information Gain
- Selects the best attribute
- Builds the Decision Tree
- Predicts the class of new records

## Dataset

| Instance | Class | a1 | a2 |
|----------|-------|----|----|
| 1 | + | T | T |
| 2 | + | T | T |
| 3 | - | T | F |
| 4 | + | F | F |
| 5 | - | F | T |
| 6 | - | F | T |

## Information Gain

```text
Entropy(S) = 1.0000

Gain(a1) = 0.0817
Gain(a2) = 0.0000
