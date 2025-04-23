#import math module.
import math
#Define function for the equation
def f(x):
    return math.exp(-x) - x**2


#importing numpy
import numpy as np

i1 = -2 #left interval point
i2 = 2 #right interval point

l = i1  
r = i2

f1=f(l) #value at -2
l1 = l #2

step = 0.1   #defining stepsize

l+=step #0.1
# for loop to iterate over the given range
for n in np.arange(l, r+step, step):
    f2=f(n)
    print("l1=" + str(l1) + " f(l1)=" + str(f1) + " n=" + str(n) + " f2=" + str(f2)) 
    if f1*f2 < 0.0:
        print("Desired interval :" + str(l1)+ " " + str(n))  #printing desired interval
        
        break

       

    l1 = n  #left side of interval
    f1 = f(l1)   #rifgt side of interval  

    #print(n)
