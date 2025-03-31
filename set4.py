# L1 = [1, 2, 3, 4, 5, 6]
# L2 = [2, 4, 6]
# result = [x for x in L1 if x not in L2]
# print(result) 


# import numpy as np
# n = int(input("Enter the number of lines: "))
# for i in range(1, n + 1):
#     print(np.arange(1.0, 1.0 + 0.5 * i, 0.5))


# def encrypt(s):
#     return ''.join(chr(219 - ord(c)) for c in s)

# print(encrypt('zbc'))


# def swap_halves(s):
#     mid = len(s) // 2
#     if len(s) % 2 == 0:
#         return s[mid:] + s[:mid]
#     else:
#         return s[mid+1:] + s[mid] + s[:mid]
# print(swap_halves('Debdawipayan')) 
# print(swap_halves('aman'))   


# user_input = input("Enter elements separated by space: ").split()
# non_repeating = [x for x in set(user_input) if user_input.count(x) == 1]
# print(non_repeating)  # Output: [1, 3, 5]

# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr[:, 0]) 
# print(arr[:, 1])
# print(arr[:, 2])


# import math

# def calc_area(r):
#     return math.pi * r ** 2

# radius_list = [1, 2, 3, 4, 5]
# area_list = [calc_area(r) for r in radius_list]
# print(area_list)


# import numpy as np
# radius_np = np.array([1, 2, 3, 4, 5])
# area_np = calc_area(radius_np)
# print(area_np)


# import numpy as np

# d = {}
# for _ in range(5):
#     roll_number = input("Enter roll number: ")
#     marks = np.array([float(input(f"Enter marks for course {i+1}: ")) for i in range(3)], dtype='float64')
#     d[roll_number] = marks

# print(d)






# a1 = np.array([1, 2, 3, 4])
# a2 = np.array([1, 2, 3, 4])

# equal = True
# for i in range(len(a1)):
#     if a1[i] != a2[i]:
#         equal = False
#         break

# print(equal) 
# print(np.array_equal(a1, a2))  


# arr = np.array([[1, 2, 3, 4, 11], [100, 55, 80, 33, 22]])
# sliced_arr = arr[:, [3, 4]]
# print(sliced_arr)



