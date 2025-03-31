# Importing the numpy library
import numpy as np
# Defining the given arrays
x = np.array( [1, 2, 3, 4])
y = np.array( [2, 3, 1, 2])
z = np.array( [3, 5, 4, 6])


p = np.array( [7, 4, 4, 3])
q = np.array([8, 6, 1, 2])
r = np.array( [15, 5, 5, 5])
             

# element_sum = np.add(x,y)
# for i in range(element_sum):
#     for j in range(z):
#         if element_sum[i] == z[j]:
#             print("true")
#         else:
#             print("false")

# if np.add(x,y) == z:
#     print("true")
# else:
#     print("false")

# # print((np.sum(x+y))==z)
# # print(np.sum(x))
# # print(x[0])
# for i in x & y:
#     if (x[i]+y[i] == z[i]):
#         print("true")
#     else:
#         print("false")
        

# def sum(a, b):
#     print (a+# x = np.array( [1, 2, 3, 4])
# y = np.array( [2, 3, 1, 2])
# z = np.array( [3, 5, 4, 6])b)
# # a = array([1, 2, 3, 4, 5]) #array of numpy
# # b = array([1, 2, 3, 4, 5])
# print(sum(x,y) == z)

# for k in range(z):
#     for i in range(x):
#         for j in range(y):
#             if (i == j == k) & (x[i]+y[j] == z[k]):
#                 print("True")
#             else:
#                 print("false")

def ele_equal(a,b,c):
    if c == (a+b):
        return True
    else:
        return False
    
numpy_ele_equal = np.vectorize(ele_equal)
x = numpy_ele_equal(x,y,z)

if x.all() == True:
    print("true")
else:
    print("false")
