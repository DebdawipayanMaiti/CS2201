import matplotlib.pyplot as plt
import math
# Marks and labels
x = [100, 90, 95, 89, 55, 70, 65, 70]  # CS1101
y = [100, 90, 80, 80, 65, 70, 70, 65]  # CS2201
labels = [0, 0, 0, 0, 1, 1, 1, 1]      # Class labels (0 = doing well, 1 = needs help)
# Point to classify
point = (70, 87.5)
# Calculate distance
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
# Simple kNN function
def simple_kNN(x, y, labels, k, point):
    distances = []
    for i in range(len(x)):
        d = euclidean_distance(x[i], y[i], point[0], point[1])
        distances.append((d, labels[i]))
    
    distances.sort()  # Sort by distance
    k_nearest = distances[:k]  # Take first k

    # Count labels
    count0 = sum(1 for d, label in k_nearest if label == 0)
    count1 = sum(1 for d, label in k_nearest if label == 1)

    return 0 if count0 > count1 else 1
# Classify
k = 3
result = simple_kNN(x, y, labels, k, point)
# Message
if result == 0:
    print("Great to know you are doing well!")
else:
    print("No worries, the instructor and the TAs will help you!")
# Plot
plt.scatter(x, y, c=labels)
plt.scatter(point[0], point[1], color='magenta', label='New Student')
plt.xlabel("CS1101 Marks")
plt.ylabel("CS2201 Marks")
plt.legend()
plt.title("kNN Classification of Student")
plt.show()



# Test data: (CS1101, CS2201, true label)
test_set = [(90, 90, 0), (50, 60, 1), (85, 80, 1), (20, 20, 0)]
# Initialize counts
TP = TN = FP = FN = 0
# Run predictions
for test_point in test_set:
    point = (test_point[0], test_point[1])
    true_label = test_point[2]
    predicted = simple_kNN(x, y, labels, 3, point)

    if true_label == 1 and predicted == 1:
        TP += 1
    elif true_label == 0 and predicted == 0:
        TN += 1
    elif true_label == 1 and predicted == 0:
        FN += 1
    else:
        FP += 1
# Compute metrics
Accuracy = (TP + TN) / len(test_set)
Precision = TP / (TP + FP) if (TP + FP) > 0 else 0
Recall = TP / (TP + FN) if (TP + FN) > 0 else 0
Fscore = 2 * (Precision * Recall) / (Precision + Recall) if (Precision + Recall) > 0 else 0
# Print results
print(f"TP = {TP}, FP = {FP}, TN = {TN}, FN = {FN}")
print(f"Accuracy = {Accuracy:.2f}")
print(f"Precision = {Precision:.2f}")
print(f"Recall = {Recall:.2f}")
print(f"F-score = {Fscore:.2f}")
