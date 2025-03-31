# def common_in_list(L1,L2):
#     result = False
#     for x in L1:
#         for y in L2:
#             if x==y:
#                 result = True
#     return result
            
# print(common_in_list([1,2,3,4,5,56], [1,45,87,6,99,100]))



# char = ["I","l","o","v","e","P","y","t","h","o","n"]
# result_str = "".join(char)
# print(result_str)


# L_original = [1, 1, 2, 3, 4, 4, 5, 1]


# def element_remover(L,k):
#     return L.pop(k-1)

# print(element_remover(L_original, 3,),L_original )

# def element_remover(L,k):
    
#     return L[:k+1]+L[k:]

# print(element_remover(L_original,4))

# x = "mitochondria"
# for i in range(len(x)+1,0,1):
#     print(x[:i:])

# List = input("Enter the name of elements separated by space").split()
# x = 0
# for elements in List:
#     if len(elements) > x:
#         x = len(elements)
        
# print("")



# def test_monotone(nums):
#     # Check if all elements in the list 'nums' are in increasing order
#     if all(nums[i] < nums[i + 1] for i in range(len(nums) - 1)):
#         return "Increasing."
#     # Check if all elements in the list 'nums' are in decreasing order
#     elif all(nums[i + 1] < nums[i] for i in range(len(nums) - 1)):
#         return "Decreasing."
#     else:
#         return "Not a monotonic sequence!"
# # Assign a specific list of numbers 'nums' to the variable
# nums = [1, 2, 3, 4, 5, 6]
# # Print the original list of numbers 'nums'
# print("Original list:")
# print(nums)
# # Print a message indicating the operation to be performed
# print("Check the direction ('increasing' or 'decreasing') of the said list:")
# # Print the result of the test function applied to the 'nums' list
# print(test_monotone(nums))


# def test_monotone(nums):
#     if all(nums[i]<nums[i+1] for i in range(len(nums)-1)):
#         return "Increasing"
#     elif all(nums[i+1]<nums[i] for i in range(len(nums)-1)):
#         return "Decreasing"
#     else:
#         "Not monotonically increasing or decraesing!"
        
# nums = list(map(int,input("Enter the no. of list you have to check: ").split()))
# print("original list: ",nums)
# print("Determination about the list:")
# print(test_monotone(nums))

        
import numpy as np
# a1 = np.array([1, 2, 3, 4])
# a2 = np.array([1, 2, 3, 4])
# if len(a1) != len(a2):
#     print("The arrays are not equal!")
# else:
#     unequal = False
#     for i in range(0, len(a1)):
#         if a1[i] != a2[i]:
#             unequal = True
#             break
#     if unequal == False:
#         print("The arrays are equal!")
#     else:
#         print("The arrays are not equal!")
        
# print(np.array_equal(a1, a2))




# x = [1,2,3,4,5,6,7,8,9,10]
# y = [1,2,3,4,5,6,7,8,9,10]
# for i in range(len(x)):
#     for j in range(len(y)):
        



# d = {}
# for i in range(0, 6):
#     rollno = input("Roll no: ")
#     marks = input("Three marks, space separated, press enter to end: ").split(" ")
#     d[rollno] = np.array(marks).astype('float64')
# d_sum = {}
# for e in d:
#     d_sum[e] = np.sum(d[e])    
# print(d_sum)
# print(d)

# A = np.array([[1,2,3], [4, 5, 6]])
# c = 3 #no of cols
# for i in range(0, c):
#     print(A[:,i])



# st = input('Give a list: (space separated, put an enter to end)').split(" ")

# # print(st)
# # st_out = []

# # l = len(st)

# # lst_out = []

# # for i in range(0, l):
# #     r = 0
# #     for j in range(0, l):
# #         if i != j:
# #             if st[i] == st[j]:
# #                 r = 1
# #                 break
# #     if r == 0:
# #         st_out.append(st[i])
        
# # print(st_out)
# print([x for x in range(st)])
# print(list(set(st)))



import numpy as np
# import matplotlib.pyplot as plt
# years = np.arange(2020, 2025)
# sales_A = [50, 60, 70, 80, 90]
# sales_B = [40, 50, 65, 75, 85]
# plt.subplot(2,1,1)
# plt.bar(years - 0.2, sales_A, width=0.4, label="Product A", color='blue')
# plt.bar(years + 0.2, sales_B, width=0.4, label="Product B", color='red')
# plt.xlabel("Year")
# plt.ylabel("Sales")
# plt.title("Sales of Two Products Over Time")
# plt.xticks(years)
# plt.legend()
# plt.show()
# plt.subplot(2,1,2)
# plt.bar(years, sales_A, color='blue', label="Product A")
# plt.bar(years, sales_B, bottom=sales_A, color='red', label="Product B")
# plt.xlabel("Year")
# plt.ylabel("Total Sales")
# plt.title("Stacked Bar Chart of Sales")
# plt.legend()
# plt.show()



# x = np.array([10,11,14,15,16])
# y = x + 2
# print(y)
