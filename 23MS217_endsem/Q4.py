# Importing important libraries
import matplotlib.pyplot as plt
import math
# Test data
x = [142,103,190,166,127,135,160,98,189,101]  # LDL
y = [42,42,59,48,55,50,47,42,50,52]  # HDL
labels = [1,0,1,1,0,0,1,0,1,0]  # # Class labels (0 = no risk, 1 = there is risk)
# plotting the data to see scatterness
plt.scatter(x, y, c=labels)
# Euclidean distance measurement
def distance(x, y, point):
    return math.sqrt((x-point[0])**2 + (y-point[1])**2)

# Majority labelling
def majority(labels):
    
    label_freq = {}
    for lb in labels:
        if lb not in label_freq:
            label_freq[lb] = 1
        else:
            label_freq[lb] = label_freq[lb] + 1
        
    max_freq = -1
    max_freq_label = -1
    
    for lb in label_freq:    
        if label_freq[lb] > max_freq:
            max_freq = label_freq[lb]
            max_freq_label = lb
     
    print(label_freq)        
    print("max label = %d max label freq = %d" %(max_freq, max_freq_label))        
            
    return max_freq_label            
# Simple kNN function
def kNN(x, y, labels, k, point):
    x_temp = x
    y_temp = y
    
    l = len(x_temp)
    
    knn_labels = []
    
    for j in range(1, k+1):
        min_distance = 1000
        x_coord_min = -1
        y_coord_min = -1
        min_label = -1
        
        for i in range(0, l):
            if x_temp[i] != -1 and distance(x_temp[i], y_temp[i], point) < min_distance:
                min_distance = distance(x_temp[i], y_temp[i], point)
                x_coord_min = x_temp[i]
                y_coord_min = y_temp[i]
                min_label = i
                x_temp[i] = -1 #considered
                
        print("%d %d" %(x_coord_min, y_coord_min))
        knn_labels.append(labels[min_label])
    print(knn_labels)
    knn_class = majority(knn_labels)
    return knn_class
    
# Point to classify
point = tuple((map(int,input("Enter LDL and HDL by separating a space: ").split())))
# run the knn
class_label = kNN(x, y, labels, 3, point)
# Printing the statements
if class_label == 0:
    print("You are doing great! Please keep it up!")
else:  # result == 1
    print("Please see a cardiologist")
# Final view
plt.scatter([point[0]], [point[1]], color="magenta")


