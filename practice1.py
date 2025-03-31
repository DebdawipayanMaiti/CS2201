# my_dict = {"Bread":15,"Sandwitch":30,"Cola":15,"Burger":20,"Pizza":30,"French-Fries":25,"Chicken_Satte":50}
# my_dict_reversed = {value:key for key,value in my_dict.items()}
# print(my_dict_reversed)


import numpy as np
import matplotlib.pyplot as plt
# a=np.array([1,2,3,4,5])
# print(np.sum(a))

# from numpy import *
# def sum(a, b):
#     print (a+b)
# a = array([1, 2, 3, 4, 5]) #array of numpy
# print(sum(a))


# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array((1, 2, 3, 4, 5))
# print(arr1)
# print(type(arr1))
# print(arr2)
# print(type(arr2))

# x = np.array(50)
# y = np.array([[[12,15,16],[11,14,17]],[[19,90,78],[11,17,67]]])
# z= np.array([[[[12,15,16],[11,14,17]],[[19,90,78],[11,17,67]]],[[[12,15,16],[11,14,17]],[[19,90,78],[11,17,67]]]])
# print(x)
# print(np.shape(x))
# print(np.size(x))

# print(z)
# print(np.ndim(z))
# print(np.shape(z))
# print(np.size(z))

# print(z[1,0,1,-1])
# print(z[:,:,:,1:])

#fizzBuzz
#Input_number = input("Enter the no: ",i)
# for i in range(101):
#     if i%3==0 & i%5==0:
#         print("Fizzbuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("buzz")
#     else:
#         print(i)

# def f(x):
#     return x**2

# x_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y_list = []
# for i in x_list:             #list => required iteration
#    y_list.append(f(i))
# print(y_list)
    

# x=np.array(x_list)
# y=f(x)      #With numpy => No required of iteration
# print(y)

# x = np.array([[12,15,16],[11,14,17]])
# y = np.array([[15,97,43],[32,87,21]])
# z = np.array([[11,12],[23,76],[11,23]])
# print(x+y)
# print(x**2)
# print(x**2+y**2)
# print(x+10)
# print(np.multiply(x,y))    #check shape => not compatible
# print(np.shape(x))
# print(np.shape(z))
# print(np.matmul(x,z))



# def fact(x):
#     if x==0 or x==1:
#         return 1
#     else:
#         f=1
#         for i in range(2,x+1):
#             f = f*i
#     return f

# a = np.array([1,2,3,4,5])
# calc_fact = np.frompyfunc(fact,1,1)
# print(calc_fact(a))


# print(z)
# print(np.sum(z,axis=0))

# L = np.sum(z,axis=1)
# print(L)
# print(np.sh'k' 25ape(L))
# print(np.sum(a, axis = 1).shape)
# print(np.sum(a, axis = 1, keepdims=True).shape
# print(np.prod(z,axis=1))
# print(np.shape(np.prod(z,axis=1)))
# print(np.shape(np.prod(z,axis=1,keepdims=True)))
# print(np.prod(z,axis=1,keepdims=True))

# print(np.add(arr1,arr2))
# print(np.subtract(arr1,arr2))
# print(np.power(arr1,arr2))
# print(np.remainder(arr1,arr2))


# x = np.array([1,2,3,4,5,6,7,8,9,10])
# y = np.array([2,3,4,8,9,10])
# print(np.intersect1d(x,y,assume_unique=True))
# print(np.intersect1d(x,y,assume_unique=False))
# print(np.setdiff1d(x,y,assume_unique=True))
# print(np.setdiff1d(y,x,assume_unique=True))

# A = np.array([[1, 1], [1, 3]])
# B = np.array([2, 6])
# C = np.array([[1, 2, 3], [12, 67, 23], [11, 56, 54]])
# D = np.array([11,156,54])
# print(np.linalg.solve(C,D))
# print(np.linalg.inv(C).dot(D))

# print(np.linspace(0,5,5))  #start-stop-number  => endpoint by default included
# print(np.arange(0,5,1))    #start-stop-step    => endpoint by default not included
# print(np.linspace(0,5,5,retstep=True))  #a,h = np.linspace(0,5,5,retstep=True)


# print(np.zeros((50,50), int))
# print(np.ones((12,13),int))
# print(np.arange(10))
# D = np.arange(10)
# E = np.array([[1,2,3],[2,45,6]])
# F = np.arange(12,13)
# print(F)
# print(np.zeros_like(F))
# print(np.ones_like(F))


# q = np.array([2,7,8,9])
# r = q  not a deepcopy & same id   [r = q.copy() change dont reflect to original] also [q.view() chamge reflect to original]  
# deepcopy & not same id
# q[0] = 13
# q[1] = 12
# print(q)
# print(r)

# x = np.array([[1,2,3],[4,5,6]])
# print(np.shape(x))
# y = x.reshape(3,2)
# print(np.shape(y))
# print(z.reshape(2, 2, -1))  -1 => unknown dimension
# also .reshape(-1) is equivalent to np.flatten make array 1d
# reshpe equivalents view id diff but modification exists

# x = np.arange(0,100,0.1)
# y = x**2
# z = x**3
# t = x**4
# l = x**5
# s = x**6
# r = x**7
# x_new = np.arange(0, 2*np.pi, 0.2)
# y_new = np.cos(x_new)
# z_new = np.sin(x_new)
# # plt.plot(x,y,'o-r',x,s,'g-s')
# plt.plot(x_new,y_new,'h:r',x_new,z_new,'h:m')  #also 'o-m' works
# plt.legend()
# plt.savefig('practice.png')
# plt.show()



# plt.subplot(1, 2, 1) #the figure has 1 row, 2 columns, and this plot is the first plot
# plt.title('sin')
# plt.xlabel('x-axis’)
# plt.ylabel('y-axis’)
# plt.plot(x_new,y_new,‘X:r’,label=‘Sin’)
# plt.subplot(1, 2, 2) #the figure has 1 row, 2 columns, and this plot is the second plot
# plt.title(‘Cos’)
# plt.xlabel(‘x-axis’)
# plt.ylabel(‘y-axis’)
# plt.plot(x new,z_new,‘s– –g’,label=‘Cos’)

# Student_name = np.array(['Adit','Ram','Rohit','Shyam','gitam','Raj','Nisha','Shyam','kal','Lila'])
# Marks = np.array([12,15,18,12,10,15,6,3,17,19])
# plt.subplot(1,2,1)
# plt.bar(Student_name,Marks,color='black',width=0.5,figsize=(8,8))
# plt.subplot(1,2,2)
# plt.pie(Marks,labels=Student_name,figsize=(8,8))
# plt.show()

'''practice of some very basic questions'''

# x = input("Enter 9 numbers sepated by space: ").split()
# print(np.array(x))
# print(type(np.array(x)))
# print(x[::-1])
# print(x[-3:])
# print(x[:3])
# print(x[int(len(x)/2)-1:int(len(x)/2)+2])
# print(x[-5:-1])
# x[1::2]=0
# print(x)

# a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# print(a[:,2:])
# print(a[:2,:])
# a[1:3,1:3]=np.max(a[1:3,1:3])
# print(a)

# a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# b=np.array([[-1,-2,-3,-4],[-5,-6,-7,-8],[-9,-10,-11,-12],[-13,-14,-15,-16]])
# a[::2]=b[::2]
# print(a)
# print(a[:2,:2],a[:2,2:],a[2:,:2],a[2:,2:])
# updated3d_array = b.reshape(4,2,2)
# print(updated3d_array)
# print(np.shape(a))
# print(np.ndim(a))

# list = input("enter alternate name and age: ").split()
# list_dict= {list[i]:list[i+1] for i in range(0,len(list),2)}
# list_tuple = [(list[i],list[i+1]) for i in range(0,len(list),2)]
# print(list)
# print(list_dict)
# print(type(list))
# print(type(list_dict))
# print(list_tuple)
# print(type(list_tuple))



# A = np.array([[1,2,3],[4,8,66],[7,81,9]])
# B = np.array([2,3,4])
# print(abs(np.linalg.det(A)))
# print(np.linalg.solve(A,B))

# def d2b(x):
#     if int(x)>=1:
#         d2b(int(x)//2)
#     return print(int(x)%2,end='')
    
# # a = input("Enter the number you convert into Binary: ")
# # print(d2b(a))
# numpy_DecimalToBinary = np.frompyfunc(d2b,1,1)
# a = np.array([78,45,65,76,94])
# print(numpy_DecimalToBinary(a))


# def d2b(x):
#     if x < 0:
#         raise ValueError("Input must be a non-negative integer.")
#     if x == 0:
#         return 0
#     else:
#         return d2b(x // 2) * 10 + (x % 2)

# numpy_DecimalToBinary = np.frompyfunc(d2b, 1, 1)
# a = np.array([78, 45, 65, 5, 2])
# binary_array = numpy_DecimalToBinary(a)
# print(binary_array)

# S = [[50, 60, 70], [67, 88, 90], [60, 78, 97]]
# print(np.sum(S,axis=0))  #total mark in a single subject
# print(np.sum(S,axis=1))  #total mark of a single student
# print(np.vstack((np.sum(S,axis=0),np.sum(S,axis=1))))
# print(np.array([np.sum(S,axis=0),np.sum(S,axis=1)]))

# a = np.array([1,2,3,4,5,6,78,64,23])
# b = np.array([1.67,90,46,5,23,6,11,91])
# c = np.setxor1d(a,b)  # NOT present in BOTH sets
# d = np.setdiff1d      # first set that is NOT present in the seconds set

# L = np.array([[1, 2], [4, 5]])
# M = np.array([[3, 3], [1,1]])
# print(np.multiply(L,M)) # elementwise multiplication
# print(np.matmul(L,M))   # matrix multiplication



# def f(x):
#     return x**3+1
# L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# L_out = []
# for i in L:             #list => required iteration
#     L.append(f(i))
# print(L_out)    
# L_out = [f(x) for x in L]   #can be use also lambda like f = lambda x: x**3 + 1
# print(L_out)
# A = np.array(L)
# A_out = f(A)      #With numpy => No required of iteration or loops
# print(A_out)


# x = input("Enter only integars separated by space: ").split()
# y = np.array(x)
# print(np.array(x))
# print(type(np.array(x)))
# print(type(y[0]))
# print(y+10)   # gives error as y contain numpy.string
# Get user input, split it, and convert to integers
# a = input("Enter elements separated by space: ").split()
# arr = np.array(a,dtype=int)  # have to specify dtype for integar
# print(arr)


# def sexy(x):
#     if x<0:
#         return 0
#     elif x==0:
#         return 1
#     else:
#         return x%3
# A = np.array([11,13,0,-1,0,-46,12])
# sexy_from_numpy = np.frompyfunc(sexy,1,1)
# print(sexy_from_numpy(A))
# print(type(sexy_from_numpy)    # class numpy.ufunc
# sexy_from_vectorise = np.vectorize(sexy)
# sexy_from_vectorise(A)
# print(type(sexy_from_vectorise))  # class numpy.vectorise and no arguments
# print(A)


# x = np.linspace(20,21,10,endpoint=True)  # endpoint 21 is included
# y = np.linspace(20,21,10,endpoint=False) # endpoint 21 is not included
# print(x)
# print(y)
# print(type(x))
# a,h = np.linspace(20,21,10,endpoint=False,retstep=True)  # eturn the interval length
# print(a)
# print(h)

# inputs are lists and all elements are string
# matplotlib use .str to scatter plot means it can self assume str as float
# months = input("Enter the months separated by space: ").split()
# rainfall = input("Enter the rainfall separated by space (in mL): ").split()
# temperature = input("Enter the temperature separated by space (in celcius): ").split()
# plt.plot(months,rainfall,marker='o',linestyle='--',color='b',label="rainfall")
# plt.plot(months,temperature,marker='s',linestyle='-',color='r',label="temperature")
# plt.title("Months vs Rainfall & temperature")
# plt.xlabel("Months")
# plt.ylabel("Temp or rainfall (mL)")
# plt.legend()
# plt.show()

# plt.subplot(1,2,1)
# plt.plot(months,rainfall,marker='s',linestyle='-',color='r',label="temperature")
# plt.title("Temperature")
# plt.xlabel("Months")
# plt.ylabel("rainfall (mL)")
# plt.legend()
# plt.show()
# plt.subplot(1,2,2)
# plt.plot(months,temperature,marker='o',linestyle='--',color='b',label="Rainfall (mL)")
# plt.title("Rainfall")
# plt.xlabel("Months")
# plt.ylabel("rainfall (mL)")
# plt.legend()
# plt.show()

# Single bar for single month
# plt.bar(months,rainfall,color="Hotpink",alpha=0.7,width=0.5,bottom=0)
# plt.show()
# 2 bar for single month
# x = np.arange(len(months))
# plt.bar(x-0.2,rainfall,width=0.2,color="b",label="rainfall")
# plt.bar(x+0.2,temperature,width=0.3,color="r",label="Temp.")
# plt.xticks(x, months)  # Set month labels at x-axis positions
# plt.xlabel("Months")
# plt.ylabel("Values")
# plt.title("Monthly Rainfall and Temperature")
# plt.legend()
# plt.grid(axis='y')
# plt.show()

#plt.pie(rainfall,labels=months)

# import random
# n = int(input("Enter the no. of times coin have to be tossed: "))
# head_counter = 0
# estimated_probability = []
# for i in range(1,n+1):
#     if random.random() <= 0.5:
#         head_counter += 1
#     else:
#         head_counter += 0
#     prob_after_that_toss = head_counter/i
#     estimated_probability.append(prob_after_that_toss)
# print("Now estimated probability is: ",prob_after_that_toss)
# plt.plot(range(1,n+1),estimated_probability,label="Estimated Probability",color='r')
# plt.axhline(0.5,label="Theoritical Probability")
# plt.title("Estimated probabilities in a coin toss")
# plt.xlabel("Number of Tosses")
# plt.ylabel("probability in each Toss")
# plt.legend()
# plt.show()


# a=input('Give a number:')
# b=input('Give another number')
# print('The concatenated_sum=', a+b)
# print('Add_sum=', int(a)+int(b))

# def common_list_checker(L1,L2):
#     result = False
#     for x in L1:
#         for y in L2:
#             if x == y:
#                 result = True
#                 return result
# print(common_list_checker([1,2,3],[4,5,6]))

# S = ["I"," ","l","o","v","e"," ","p","y","h","o","n"]
# total_S = "".join(S)
# print(total_S)

"""
import numpy as np
import matplotlib.pyplot as plt


x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

plt.subplot(1, 2, 1)
plt.plot(x1, y1, 'ko-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')


plt.subplot(1, 2, 2)
plt.plot(x2, y2, 'r.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')

plt.show()
"""










