

## Aim

To construct a Decision Tree using the ID3 algorithm by calculating Entropy and Information Gain.

## Description

This Python program implements the ID3 Decision Tree algorithm from scratch.

The program performs the following operations:

1. Stores the given dataset.
2. Calculates the Entropy of the dataset.
3. Calculates Information Gain for each attribute.
4. Selects the attribute with the highest Information Gain.
5. Constructs the Decision Tree recursively.
6. Uses the Decision Tree to predict the class of new data.

## Dataset

| Instance | a1 | a2 | a3 | Class |
|----------|----|----|----|-------|
| 1 | True | Hot | High | No |
| 2 | True | Hot | High | No |
| 3 | False | Hot | High | Yes |
| 4 | False | Cool | Normal | Yes |
| 5 | False | Cool | Normal | Yes |
| 6 | True | Cool | High | No |
| 7 | True | Hot | High | No |
| 8 | False | Hot | Normal | Yes |
| 9 | False | Cool | Normal | Yes |
| 10 | False | Cool | High | Yes |

## Entropy

The entropy of the complete dataset is:

```text
Entropy(S) = 0.9710
