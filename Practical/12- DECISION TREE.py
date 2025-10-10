import math
from collections import Counter

# Function to calculate entropy
def entropy(data):
    labels = [row[-1] for row in data]
    label_counts = Counter(labels)
    total = len(data)
    ent = 0.0
    for count in label_counts.values():
        prob = count / total
        ent -= prob * math.log2(prob)
    return ent

# Function to split dataset
def split_data(data, feature_index, value):
    subset = []
    for row in data:
        if row[feature_index] == value:
            reduced_row = row[:feature_index] + row[feature_index+1:]
            subset.append(reduced_row)
    return subset

# Function to choose best feature
def best_feature(data):
    base_entropy = entropy(data)
    best_gain = 0
    best_index = -1
    num_features = len(data[0]) - 1
    
    for i in range(num_features):
        values = set([row[i] for row in data])
        new_entropy = 0
        for value in values:
            subset = split_data(data, i, value)
            prob = len(subset) / len(data)
            new_entropy += prob * entropy(subset)
        info_gain = base_entropy - new_entropy
        if info_gain > best_gain:
            best_gain = info_gain
            best_index = i
    return best_index

# ID3 Algorithm
def id3(data, features):
    labels = [row[-1] for row in data]
    
    # If all labels are the same
    if labels.count(labels[0]) == len(labels):
        return labels[0]
    
    # If no features left
    if len(data[0]) == 1:
        return Counter(labels).most_common(1)[0][0]
    
    # Choose best feature
    best_idx = best_feature(data)
    best_feat = features[best_idx]
    
    tree = {best_feat: {}}
    
    feat_values = set([row[best_idx] for row in data])
    for value in feat_values:
        subset = split_data(data, best_idx, value)
        sub_features = features[:best_idx] + features[best_idx+1:]
        tree[best_feat][value] = id3(subset, sub_features)
    
    return tree

# Example Dataset (Play Tennis)
dataset = [
    ["Sunny", "Hot", "High", "Weak", "No"],
    ["Sunny", "Hot", "High", "Strong", "No"],
    ["Overcast", "Hot", "High", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Strong", "No"],
    ["Overcast", "Cool", "Normal", "Strong", "Yes"],
    ["Sunny", "Mild", "High", "Weak", "No"],
    ["Sunny", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "Normal", "Weak", "Yes"],
    ["Sunny", "Mild", "Normal", "Strong", "Yes"],
    ["Overcast", "Mild", "High", "Strong", "Yes"],
    ["Overcast", "Hot", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Strong", "No"]
]

features = ["Outlook", "Temperature", "Humidity", "Wind"]

# Build decision tree
tree = id3(dataset, features)
print("Decision Tree:")
print(tree)
