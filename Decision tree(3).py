import math
from collections import Counter

# Dataset from the image
data = [
    ["Sunny", "Hot",  "High",   "Weak",   "No"],
    ["Sunny", "Hot",  "High",   "Strong", "No"],
    ["Overcast", "Hot", "High", "Weak",   "Yes"],
    ["Rain",  "Mild", "High",   "Weak",   "Yes"],
    ["Rain",  "Cool", "Normal", "Weak",   "Yes"],
    ["Rain",  "Cool", "Normal", "Strong", "No"],
    ["Overcast", "Cool", "Normal", "Strong", "Yes"],
    ["Sunny", "Mild", "High",   "Weak",   "No"],
    ["Sunny", "Cool", "Normal", "Weak",   "Yes"],
    ["Rain",  "Mild", "Normal", "Weak",   "Yes"],
    ["Sunny", "Mild", "Normal", "Strong", "Yes"],
    ["Overcast", "Mild", "High", "Strong", "Yes"],
    ["Overcast", "Hot", "Normal", "Weak", "Yes"],
    ["Rain",  "Mild", "High",   "Strong", "No"]
]

attributes = ["Outlook", "Temperature", "Humidity", "Wind"]


# Calculate entropy
def entropy(rows):
    labels = [row[-1] for row in rows]
    counts = Counter(labels)
    total = len(labels)

    result = 0

    for count in counts.values():
        probability = count / total
        result -= probability * math.log2(probability)

    return result


# Split data based on an attribute
def split_data(rows, attribute_index):
    groups = {}

    for row in rows:
        value = row[attribute_index]

        if value not in groups:
            groups[value] = []

        groups[value].append(row)

    return groups


# Calculate Information Gain
def information_gain(rows, attribute_index):
    total_entropy = entropy(rows)
    groups = split_data(rows, attribute_index)

    weighted_entropy = 0

    for group in groups.values():
        weighted_entropy += (len(group) / len(rows)) * entropy(group)

    return total_entropy - weighted_entropy


# Find majority class
def majority_class(rows):
    labels = [row[-1] for row in rows]
    return Counter(labels).most_common(1)[0][0]


# Build the ID3 Decision Tree
def build_tree(rows, available_attributes):
    labels = [row[-1] for row in rows]

    # If all examples belong to the same class
    if len(set(labels)) == 1:
        return labels[0]

    # If no attributes are left
    if not available_attributes:
        return majority_class(rows)

    # Find the best attribute
    gains = {}

    for attribute_index in available_attributes:
        gains[attribute_index] = information_gain(rows, attribute_index)

    best_attribute = max(gains, key=gains.get)

    tree = {
        "attribute": best_attribute,
        "branches": {},
        "default": majority_class(rows)
    }

    groups = split_data(rows, best_attribute)

    remaining_attributes = [
        attr for attr in available_attributes
        if attr != best_attribute
    ]

    for value, group in groups.items():
        tree["branches"][value] = build_tree(
            group,
            remaining_attributes
        )

    return tree


# Predict the result
def predict(tree, sample):
    # Leaf node
    if isinstance(tree, str):
        return tree

    attribute_index = tree["attribute"]
    value = sample[attribute_index]

    if value in tree["branches"]:
        return predict(tree["branches"][value], sample)

    # If an unknown value is entered
    return tree["default"]


# Display the decision tree
def print_tree(tree, level=0):
    indent = "    " * level

    if isinstance(tree, str):
        print(indent + "Play Tennis = " + tree)
        return

    attribute_name = attributes[tree["attribute"]]

    for value, subtree in tree["branches"].items():
        print(indent + f"{attribute_name} = {value}")

        if isinstance(subtree, str):
            print(indent + "    " + "Play Tennis = " + subtree)
        else:
            print_tree(subtree, level + 1)


# Train the Decision Tree
tree = build_tree(
    data,
    list(range(len(attributes)))
)


# Main Program
print("\n========== PLAY TENNIS DECISION TREE ==========\n")

print("Generated Decision Tree:\n")
print_tree(tree)

print("\n========== ENTER WEATHER CONDITIONS ==========\n")

outlook = input("Enter Outlook (Sunny/Overcast/Rain): ").title()
temperature = input("Enter Temperature (Hot/Mild/Cool): ").title()
humidity = input("Enter Humidity (High/Normal): ").title()
wind = input("Enter Wind (Weak/Strong): ").title()

sample = [outlook, temperature, humidity, wind]

result = predict(tree, sample)

print("\n========== PREDICTION RESULT ==========")
print("Outlook     :", outlook)
print("Temperature :", temperature)
print("Humidity    :", humidity)
print("Wind        :", wind)
print("--------------------------------------")
print("Play Tennis :", result)
