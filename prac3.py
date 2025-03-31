# import math

# def f(x):
#     return 10**x + x - 4  #f = lambda x: 10**x + x - 4

# import numpy as np
# i1 = 0.0 
# i2 = 1.0 
# l = i1
# r = i2
# f1=f(l) 
# l1 = l 
# step = 0.1
# l+=step 

# for n in np.arange(l, r+step, step):
#     f2=f(n)
#     print("l1=" + str(l1) + " f(l1)=" + str(f1) + " n=" + str(n) + " f2=" + str(f2)) 
#     if f1*f2 < 0.0:
#         print("Desired interval :" + str(l1)+ " " + str(n))
        
#         break

#     l1 = n
#     f1 = f(l1)    
   
    
   



# import matplotlib.pyplot as plt
# import numpy as np

# def f(x):
#     return 10**x + x - 4


# def bisection1(a, b):
#     if(f(a)*f(b)>=0):
#         print("Invalid interval!")
#         return

#     #print("Current interval: [%f, %f]" %(a, b))
#     mid = a
#     x = []
#     y = []

    
#     for i in range(1, 101, 1):
#         mid = (a + b)/2.0
#         if(f(a)*f(mid) < 0):
#             b = mid
#         else:
#             a = mid    

#         x.append(mid)
#         y.append(f(mid))
#         return mid, x, y

# def bisection(a, b):
#     if(f(a)*f(b)>=0):
#         print("Invalid interval!")
#         return

#     #print("Current interval, mid and f-value: [%f, %f]: %f %f" %(a, b, a, f(a)))
#     mid = a
#     x = []
#     y = []

    
#     while (b - a) >= 0.0001:
        
#         mid = (a + b)/2.0

#         #print("a, f-value, b, f-value, mid, f-value: %f %f %f %f %f" %(a, f(a), b, f(b), mid, f(mid)))
#         #print("a = %f f(a) = %f b = %f f(b) = %f mid = %f f(mid) = %f" %(a, f(a), b, f(b), mid, f(mid)))
#         print("%f %f %f %f %f %f" %(a, f(a), b, f(b), mid, f(mid)))
#         if(f(a)*f(mid) < 0):
#             b = mid
#         else:
#             a = mid    

#         #print("Current interval, mid and f-value: [%f, %f]: %f %f" %(a, b, mid, f(mid)))

#         x.append(mid)
#         y.append(f(mid))

#     return mid, x, y


# sol, x, y = bisection(0.6,0.7)
# print(x)
# print(y)
# print(f"The root is {sol}")     #"%.4f"%sol upto 4 significant digit

# """
# x = np.linspace(0, 1, 100, endpoint=True)
# y = f(x)
# zero = np.zeros(100)
# plt.plot(x, zero, label = 'x = 0')
# plt.plot(x, y, label='f(x)')
# #plt.plot(x, y1, label = 'iterations')

# plt.legend()

# plt.show()"""




# import numpy as np
# import math

# def f(x):
#     return 10**x + x - 4
# def df(x):
#     return math.log(10)*10**x + 1
# def df_num(x):
#     h = 0.0001
#     return (f(x+h) - f(x))/h
# def tabular(low, hi, step):
#     i1 = low
#     i2 = hi
    
#     l = i1
#     r = i2
    
#     f1=f(l)
#     l1 = l
    	
#     l += step
     
#     print("%f %f %f" %(low, hi, step))

#     for n in np.arange(l, r+step, step):
#         f2=f(n)
#         print("l1=" + str(l1) + " f(l1)=" + str(f1) + " n=" + str(n) + " f2=" + str(f2)) 
#         if f1*f2 < 0.0:
#             print(str(l1)+ " " + str(n))
#             break
   
#     l1 = n
#     f1 = f(l1)

#     return l1, n


# def newtonRaphson(x):
#     h = f(x)/df(x)
#     while abs(f(x)) >= 0.00001:
#         h = f(x)/df(x)
#         x = x - h
#         print('x, f, df, h values: %f %f %f %f' %(x, f(x), df(x), h))

       
#     print("Final f-value %f" %(f(x)))
#     return x


# l, r = tabular(0, 1, 0.1)
# print("The root is ", "%.4f"%newtonRaphson(r))