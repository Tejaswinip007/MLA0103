# Play Tennis Decision Tree

## Project Description

This project implements a **Decision Tree classifier using the ID3 algorithm** in Python.

The program uses a dataset containing weather conditions to predict whether **tennis should be played or not**.

The prediction is based on the following attributes:

* Outlook
* Temperature
* Humidity
* Wind

The target variable is:

* Play Tennis: Yes
* Play Tennis: No

## Dataset

The dataset contains 14 weather records.

| Day | Outlook  | Temperature | Humidity | Wind   | Play Tennis |
| --- | -------- | ----------- | -------- | ------ | ----------- |
| D1  | Sunny    | Hot         | High     | Weak   | No          |
| D2  | Sunny    | Hot         | High     | Strong | No          |
| D3  | Overcast | Hot         | High     | Weak   | Yes         |
| D4  | Rain     | Mild        | High     | Weak   | Yes         |
| D5  | Rain     | Cool        | Normal   | Weak   | Yes         |
| D6  | Rain     | Cool        | Normal   | Strong | No          |
| D7  | Overcast | Cool        | Normal   | Strong | Yes         |
| D8  | Sunny    | Mild        | High     | Weak   | No          |
| D9  | Sunny    | Cool        | Normal   | Weak   | Yes         |
| D10 | Rain     | Mild        | Normal   | Weak   | Yes         |
| D11 | Sunny    | Mild        | Normal   | Strong | Yes         |
| D12 | Overcast | Mild        | High     | Strong | Yes         |
| D13 | Overcast | Hot         | Normal   | Weak   | Yes         |
| D14 | Rain     | Mild        | High     | Strong | No          |

## Algorithm Used

The program uses the **ID3 (Iterative Dichotomiser 3) Decision Tree Algorithm**.

The algorithm performs the following steps:

1. Calculates the entropy of the dataset.
2. Splits the dataset based on each attribute.
3. Calculates the information gain for every available attribute.
4. Selects the attribute with the highest information gain.
5. Creates branches for the different attribute values.
6. Repeats the process until a final classification of **Yes** or **No** is obtained.
7. Uses the generated decision tree to predict new user input.

## Features

* Implements the ID3 algorithm from scratch.
* Calculates entropy.
* Calculates information gain.
* Automatically builds a decision tree.
* Displays the generated decision tree.
* Accepts weather conditions as user input.
* Predicts whether tennis should be played.
* Uses the majority class if an unknown attribute value is entered.

## Requirements

* Python 3.x

No external libraries are required.

The program uses only the following built-in Python modules:

```text
math
collections
```

## Project Structure

```text
Play-Tennis-Decision-Tree/
│
├── decision_tree.py
└── README.md
```

## How to Run

### Step 1: Download or Clone the Project

Make sure the following files are available in the project folder:

```text
decision_tree.py
README.md
```

### Step 2: Open Terminal or Command Prompt

Navigate to the project directory.

### Step 3: Run the Program

Execute the following command:

```bash
python decision_tree.py
```

## Sample Input

```text
Enter Outlook (Sunny/Overcast/Rain): Sunny
Enter Temperature (Hot/Mild/Cool): Mild
Enter Humidity (High/Normal): Normal
Enter Wind (Weak/Strong): Strong
```

## Sample Output

```text
========== PLAY TENNIS DECISION TREE ==========

Generated Decision Tree:

Outlook = Sunny
    Humidity = High
        Play Tennis = No
    Humidity = Normal
        Play Tennis = Yes
Outlook = Overcast
    Play Tennis = Yes
Outlook = Rain
    Wind = Weak
        Play Tennis = Yes
    Wind = Strong
        Play Tennis = No

========== ENTER WEATHER CONDITIONS ==========

========== PREDICTION RESULT ==========
Outlook     : Sunny
Temperature : Mild
Humidity    : Normal
Wind        : Strong
--------------------------------------
Play Tennis : Yes
```

## Decision Rules

The generated decision tree follows these main rules:

* If **Outlook is Overcast**, then **Play Tennis = Yes**.
* If **Outlook is Sunny** and **Humidity is High**, then **Play Tennis = No**.
* If **Outlook is Sunny** and **Humidity is Normal**, then **Play Tennis = Yes**.
* If **Outlook is Rain** and **Wind is Weak**, then **Play Tennis = Yes**.
* If **Outlook is Rain** and **Wind is Strong**, then **Play Tennis = No**.

## Example Prediction

### Input

```text
Outlook: Sunny
Temperature: Mild
Humidity: Normal
Wind: Strong
```

### Prediction

```text
Play Tennis: Yes
```

## Conclusion

This project demonstrates the implementation of a Decision Tree classifier using the ID3 algorithm. The program analyzes weather conditions, calculates entropy and information gain, builds a decision tree, and predicts whether the conditions are suitable for playing tennis.
