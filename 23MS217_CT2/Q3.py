# Importing the numpy library
import numpy as np
# Defining the given arrays
x = np.array( [1, 2, 3, 4])
y = np.array( [2, 3, 1, 2])
z = np.array( [3, 5, 4, 6])


p = np.array( [7, 4, 4, 3])
q = np.array([8, 6, 1, 2])
r = np.array( [15, 5, 5, 5])
# usual function defining mainly
def ele_equal(a,b,c):
    if c == (a+b):
        return True
    else:
        return False
# making the function universal vectorise function to work on arrays
numpy_ele_equal = np.vectorize(ele_equal)
# values of x,y,z arrays afterapplying function.It return list of bools
l = numpy_ele_equal(x,y,z)
m = numpy_ele_equal(p,q,r)
# if all value in bool list is true then true else print false.
if l.all() == True:
    print("true")
else:
    print("false")
    
if m.all() == True:
    print("true")
else:
    print("false")
    