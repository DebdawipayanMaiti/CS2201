import numpy as np   #importing numpy
import math          #importing math
#Define the fuction
def f(x):
    return math.exp(-x) - x**2
#Define the derivative of the function
def df(x):
    return -math.exp(-x) - 2*x

def df_num(x):
    h = 0.0001   #Tolerence or accuracy given by me or in the sirs given question
    return (f(x+h) - f(x))/h

def tabular(low, hi, step):
 i1 = low
 i2 = hi

 l = i1
 r = i2

 f1=f(l)
 l1 = l
	
 l += step
 
 print("%f %f %f" %(low, hi, step))

 for n in np.arange(l, r+step, step):
  f2=f(n)
  print("l1=" + str(l1) + " f(l1)=" + str(f1) + " n=" + str(n) + " f2=" + str(f2)) 
  if f1*f2 < 0.0:
   print(str(l1)+ " " + str(n))
   break
   

  l1 = n
  f1 = f(l1)

 return l1, n


    

def newtonRaphson(x):
    h = f(x)/df(x)
    #h = f(x)/df_num(x)
    
    

    
    #run the while loop if absolute value of function is greater than or equal to 0.00001 
    while abs(f(x)) >= 0.00001:

        h = f(x)/df(x)
        #h = f(x)/df_num(x)
        x = x - h
        
       

        print('x, f, df, h values: %f %f %f %f' %(x, f(x), df(x), h))

       
    print("Final f-value %f" %(f(x)))
    
    return x

#tabular method find better boundary.
l, r = tabular(-2, 2, 0.1)
print("The root is ", "%.4f"%newtonRaphson(r))
