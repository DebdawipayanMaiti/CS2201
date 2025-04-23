# Importing the numpy library
import numpy as np
# Creating 1 2D array
x = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# craeting 1 3D array
y = np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[1,2,3,4,5],[6,7,8,9,10]]])
# Flattening of 2D array
flatten_x = x.flatten()
# Flattening of #D array
flatten_y = y.flatten()
# Printin 2 flat arrays 
print(flatten_x)
print(flatten_y)
# Printing of asked union
print("union")
print(np.union1d(flatten_x,flatten_y))
# Printing of asked intersection
print("intersection:")
print(np.intersect1d(flatten_x, flatten_y))
# Printing of asked set difference
print("setdifference")
print(np.setdiff1d(flatten_x,flatten_y))
print(np.setdiff1d(flatten_y,flatten_x))
