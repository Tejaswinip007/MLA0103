from math import log2
from collections import Counter

# Dataset
# Instance | Class | a1 | a2
data = [
    (1, "+", "T", "T"),
    (2, "+", "T", "T"),
    (3, "-", "T", "F"),
    (4, "+", "F", "F"),
    (5, "-", "F", "T"),
    (6, "-", "F", "T")
]

FEATURES = ["a1", "a2"]
FEATURE_INDEX = {
    "a1": 2,
    "a2": 3
}
TARGET_INDEX = 1


# Calculate Entropy
def entropy(rows):
    if not rows:
        return 0

    count = Counter(row[TARGET_INDEX] for row in rows)
    total = len(rows)

    result = 0

    for value in count.values():
        probability = value / total
        result -= probability * log2(probability)

    return result


# Calculate Information Gain
def information_gain(rows, feature):
    parent_entropy = entropy(rows)

    index = FEATURE_INDEX[feature]
    total = len(rows)

    groups = {}

    for row in rows:
        value = row[index]

        if value not in groups:
            groups[value] = []

        groups[value].append(row)

    weighted_entropy = 0

    for group in groups.values():
        weighted_entropy += (
            len(group) / total
        ) * entropy(group)

    return parent_entropy - weighted_entropy


# Build Decision Tree using ID3
def build_tree(rows, features):

    classes = set(row[TARGET_INDEX] for row in rows)

    # If all records belong to same class
    if len(classes) == 1:
        return {"leaf": next(iter(classes))}

    # If no features are remaining
    if not features:
        majority = Counter(
            row[TARGET_INDEX] for row in rows
        ).most_common(1)[0][0]

        return {"leaf": majority}

    # Select feature with maximum information gain
    best_feature = max(
        features,
        key=lambda feature:
        information_gain(rows, feature)
    )

    tree = {
        "feature": best_feature,
        "branches": {}
    }

    index = FEATURE_INDEX[best_feature]

    remaining_features = [
        feature for feature in features
        if feature != best_feature
    ]

    values = sorted(set(row[index] for row in rows))

    for value in values:

        subset = [
            row for row in rows
            if row[index] == value
        ]

        tree["branches"][value] = build_tree(
            subset,
            remaining_features
        )

    return tree


# Display Decision Tree
def print_tree(tree, indent=""):

    if "leaf" in tree:
        print(indent + "-> " + tree["leaf"])
        return

    print(indent + tree["feature"])

    for value, subtree in tree["branches"].items():

        print(indent + "  " + value + ": ", end="")

        if "leaf" in subtree:
            print("-> " + subtree["leaf"])
        else:
            print()
            print_tree(subtree, indent + "      ")


# Prediction
def predict(tree, sample):

    if "leaf" in tree:
        return tree["leaf"]

    feature = tree["feature"]
    value = sample[feature]

    return predict(
        tree["branches"][value],
        sample
    )


# Main Program
print("DECISION TREE USING ID3")
print("-----------------------")

print("\nEntropy:")
print("Entropy(S) =", round(entropy(data), 4))

print("\nInformation Gain:")

for feature in FEATURES:
    print(
        "Gain(" + feature + ") =",
        round(information_gain(data, feature), 4)
    )


# Build tree
tree = build_tree(data, FEATURES)

print("\nDecision Tree:")
print_tree(tree)


# Test data
print("\nPredictions:")

test_data = [
    {"a1": "T", "a2": "T"},
    {"a1": "T", "a2": "F"},
    {"a1": "F", "a2": "F"},
    {"a1": "F", "a2": "T"}
]

for sample in test_data:

    result = predict(tree, sample)

    print(
        sample,
        "=> Class =",
        result
    )
