# L = [1, 2, 3, 4, 5]
# L1 = [x for x in L if x % 2 == 0]
# print(L1)


# def remove_duplicates(L):
#     i = 0
#     while i < len(L):
#         while L[i] in L[i + 1:]:
#             L.remove(L[i])
#         i += 1
# L = [1, 2, 2, 3, 4, 4, 5]
# remove_duplicates(L)
# print(L)  

# L1 = [1, 2, 3, 4, 5]
# L2 = [5, 4, 10, 12]
# L3 = [x for x in L1 + L2 if x % 2 != 0]
# print("List L3 containing the sum of odd elements in L1 and L2:", L3)


# while True:
#     number = int(input("Enter a number (even number to stop): "))
    
#     if number % 2 == 0:
#         print("You entered an even number. Exiting the loop.")
#         break  
#     else:
#         print("You entered an odd number. Please try again.")


# n = 7685
# rev = 0
# while n > 0:
#     last_digit = n % 10  
#     rev = rev * 10 + last_digit  
#     n //= 10  
# print("Reversed number:", rev)


# n = int(input("Enter the number you want to reverse: "))
# rev = 0
# while n > 0:
#     last_digit = n % 10  
#     rev = rev * 10 + last_digit  
#     n //= 10  
# print("Reversed number:", rev)






# d = {1 : 'ONE', 2 : 'TWO', 3 : 'THREE', 4 : 'FOUR', 5 : 'FIVE', 6 : 'SIX', 7 : 'SEVEN', 8 : 'EIGHT', 9 : 'NINE'}
# number = input("Enter a number: ")
# output = [d[int(digit)] for digit in number if digit.isdigit()]
# print(" ".join(output))


# import math

# def f(x):
#     return 10**x + x - 4
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

#        l1 = n1
#        f1 = f(l1)    




n=int(input("Enter the number: "))   
for i in range(n):
    for j in range(i,n):
        print(' ',end="")
    for j in range(i):
        print('*',end="")
    for j in range(i+1):
        print('*',end="")
    print()


# n=int(input("Enter the number: "))   
# def diamond(n):
#     for i in range(n):
#         for j in range(i,n):
#             print(' ',end="")
#         for j in range(i):
#             print('*',end="")
#         for j in range(i+1):
#             print('*',end="")
#         print()
        
        
        
        
print(diamond(n))   
    


