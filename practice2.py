

"""Rotate an array to the right by k steps.
Input: [1, 2, 3, 4, 5], k = 2 → Output: [4, 5, 1, 2, 3]"""

# def rotate_array(nums, k):
#     k = k % len(nums)  # Handle cases where k > len(nums)
#     return nums[-k:] + nums[:-k]
# arr = [1, 2, 3, 4, 5]
# k = 2
# print(rotate_array(arr, k))


"""Find all pairs with a given sum.
Input: [1, 2, 3, 4, 5], target = 6 → Output: [(1, 5), (2, 4)]"""

# def find_pairs_brute_force(nums, target):
#     pairs = []
#     indices = []
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 pairs.append((nums[i], nums[j]))
#                 indices.append((i,j))
#     return pairs
#     return indices
# arr = [1, 2, 3, 4, 5]
# target = 6
# print(find_pairs_brute_force(arr, target)) 

"""Flatten a 2D array to 1D. arr = np.array([[1, 2, 3], [4, 5, 6]])
Output: [1, 2, 3, 4, 5, 6]"""
# flattened_arr2 = arr.flatten()   #arrr.ravel()


"""4)Reshape a 3x4 array into a 2x6 array."""

# arr = np.array([[1, 2, 3, 4], 
#                 [5, 6, 7, 8], 
#                 [9, 10, 11, 12]])
# print(arr.reshape(2,6))


"""Reshape a 1D array of 27 elements into a 3D array of shape (3, 3, 3)."""

# arr = np.arange(1, 28)
# print(arr.reshape(3,3,3))

"""6)Use np.vectorize() to apply a custom function that makes number binary."""


# import numpy as np
# def decimal_to_binary(num):
#     return bin(num)[2:]  # bin() returns '0b...' prefix, so we remove the first two characters
# def decimal_to_binary(n):
#     if n == 0:
#         return "0"
#     binary = ""
#     while n > 0:
#         binary = str(n % 2) + binary  # Get remainder and build binary string
#         n //= 2  # Divide by 2
#     return binary
# vectorized_binary = np.vectorize(decimal_to_binary)
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# binary_arr = vectorized_binary(arr)
# print(binary_arr)


"""Write a Numpy program that defines a custom ufunc that computes 3x + 4y for 
elements x and y from two arrays, and apply it to 2D arrays."""

# def custom_func(x, y):
#     return 3*x + 4*y
# ufunc_custom = np.frompyfunc(custom_func, 2, 1)  
# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# result = ufunc_custom(arr1, arr2)
# result = result.astype(np.int64)
# print("Result:\n", result)

"""You have two 2D arrays of shapes (3, 4) and (2, 4). Reshape them into 3D arrays 
of shapes (3, 2, 2) and (2, 2, 2), respectively, and then concatenate them along the first axis."""

# arr1 = np.arange(1, 13).reshape(3, 4)  # Shape (3,4)
# arr2 = np.arange(13, 21).reshape(2, 4)  # Shape (2,4)
# print("Original arr1:\n", arr1)
# print("Original arr2:\n", arr2)
# arr1_reshaped = arr1.reshape(3, 2, 2)  # Shape (3,2,2)
# arr2_reshaped = arr2.reshape(2, 2, 2)  # Shape (2,2,2)
# print("\nReshaped arr1:\n", arr1_reshaped)
# print("Reshaped arr2:\n", arr2_reshaped)
# print(np.concatenate((arr1_reshaped, arr2_reshaped), axis=0))


'''Given a dictionary of countries and their populations (in millions), plot a horizontal bar 
chart of the top 5 most populous countries in descending order. 
Sort the bars accordingly and label each bar with its population value.'''

# import matplotlib.pyplot as plt

# country_population = {
#     "China": 1441,
#     "India": 1393,
#     "USA": 332,
#     "Indonesia": 276,
#     "Pakistan": 225,
#     "Brazil": 213,
#     "Nigeria": 206,
#     "Bangladesh": 166,
#     "Russia": 146,
#     "Mexico": 128
# }

# top_countries = sorted(country_population.items(), key=lambda x: x[1], reverse=True)[:5]

# countries, populations = zip(*top_countries)

# plt.figure(figsize=(10, 6))
# plt.barh(countries, populations, color='skyblue')

# plt.gca().invert_yaxis()

# for index, value in enumerate(populations):
#     plt.text(value + 20, index, str(value), va='center', fontsize=12)

# plt.xlabel("Population (millions)")
# plt.ylabel("Country")
# plt.title("Top 5 Most Populous Countries")

# plt.show()

""")You are given the following sales data by product: products = ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard']
sales = [150000, 200000, 50000, 40000, 10000]
Create a pie chart showing only those products whose sales exceed $40,000.
Label slices with product names.
Add a title to the chart.
Show percentage contribution rounded to nearest integer."""

import matplotlib.pyplot as plt

# # Given sales data
# products = ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard']
# sales = [150000, 200000, 50000, 40000, 10000]

# # Filter products with sales > 40,000
# filtered_products = [products[i] for i in range(len(sales)) if sales[i] > 40000]
# filtered_sales = [sales[i] for i in range(len(sales)) if sales[i] > 40000]

# # Create pie chart
# plt.figure(figsize=(8, 8))
# plt.pie(
#     filtered_sales, 
#     labels=filtered_products, 
#     autopct=lambda p: f'{round(p)}%',  # Round to nearest integer
#     colors=['skyblue', 'lightcoral', 'gold'],  # Custom colors
#     startangle=140,  # Rotate for better visibility
#     wedgeprops={'edgecolor': 'black'}  # Add edge to slices
# )

# # Add title
# plt.title("Sales Distribution of Products Exceeding $40,000")

# # Show chart
# plt.show()


"""Plot a grouped bar chart (side-by-side bars) showing the quarterly revenue of 
three companies over n quarters. everything user input. Plot all three as 
grouped bars for each quarter.Add a legend, different colors, and appropriate labels."""

# # User input
# n = int(input("Enter number of quarters: "))
# quarters = [input(f"Quarter {i+1}: ") for i in range(n)]
# company1 = list(map(float, input("Company 1 revenue: ").split()))
# company2 = list(map(float, input("Company 2 revenue: ").split()))
# company3 = list(map(float, input("Company 3 revenue: ").split()))


# # X-axis positions
# x = np.arange(n)
# bar_width = 0.2

# # Plot grouped bars
# plt.bar(x - bar_width, company1, width=bar_width, label="Company 1")
# plt.bar(x, company2, width=bar_width, label="Company 2")
# plt.bar(x + bar_width, company3, width=bar_width, label="Company 3")

# plt.xticks(x, quarters)
# plt.xlabel("Quarters")
# plt.ylabel("Revenue (millions)")
# plt.title("Quarterly Revenue of Companies")
# plt.legend()
# plt.show()

"""take [0,4*pi] use linspace to get 100 points store in x. apply y=sin(x). 
Next create a array a that contains 100 random numbers between (-1,1) 
add y and a to get y1. plot in a single sheet row-wise the 
following three graphs:  i)(x,y) ii)(x,y1) iii) those (x,y-y1) such that it satisfies abs(y-y1)<0.35"""
    
    
# import numpy as np
# import matplotlib.pyplot as plt

# # Generate x values from 0 to 4π with 100 points
# x = np.linspace(0, 4*np.pi, 100)

# # Compute y = sin(x)
# y = np.sin(x)

# # Generate random noise in the range (-1,1)
# a = np.random.uniform(-1, 1, 100)

# # Compute y1 = y + a
# y1 = y + a

# # Compute (x, y - y1) where abs(y - y1) < 0.35
# filtered_x = x[np.abs(y - y1) < 0.35]
# filtered_y = (y - y1)[np.abs(y - y1) < 0.35]

# # Plot all graphs row-wise in a single sheet
# plt.figure(figsize=(10, 8))

# # Plot (x, y)
# plt.subplot(3, 1, 1)
# plt.plot(x, y, label="y = sin(x)", color='b')
# plt.title("y = sin(x)")
# plt.legend()

# # Plot (x, y1)
# plt.subplot(3, 1, 2)
# plt.plot(x, y1, label="y1 = y + noise", color='r')
# plt.title("y1 = y + random noise")
# plt.legend()

# # Plot filtered (x, y - y1)
# plt.subplot(3, 1, 3)
# plt.scatter(filtered_x, filtered_y, label="Filtered points", color='g')
# plt.title("Filtered points where |y - y1| < 0.35")
# plt.legend()

# # Adjust layout and show plot
# plt.tight_layout()
# plt.show()

"""You are given two 3D arrays A and B, each of shape (3, 4, 5). 
Construct a new 3D array C of the same shape where:
   (C[i, j, k] = A[i, j, k] * B[i, j, 4 - k] + A[i, (3 - j), k]
# Print the result)"""
# import numpy as np

# # Create random 3D arrays A and B of shape (3, 4, 5)
# A = np.random.rand(3, 4, 5)
# B = np.random.rand(3, 4, 5)
# # Initialize C with the same shape
# C = np.zeros((3, 4, 5))
# # Compute C using the given formula
# for i in range(3):
#     for j in range(4):
#         for k in range(5):
#             C[i, j, k] = A[i, j, k] * B[i, j, 4 - k] + A[i, (3 - j), k]
# # Print the result
# print("C array:\n", C)

"""Generate 6 evenly spaced values from -1 to 1 (inclusive). 
Call this array lin. generate values from 1 to 6 (inclusive).
 Call this array arr. Create a 6×6 2D array result where each element is defined above, 
 Print the final result array rounded to 2 decimal places."""

# import numpy as np

# # Generate lin: 6 evenly spaced values from -1 to 1
# lin = np.linspace(-1, 1, 6)

# # Generate arr: values from 1 to 6
# arr = np.arange(1, 7)

# # Initialize the result array
# result = np.zeros((6, 6))

# # Compute the result array using the given formula
# for i in range(6):
#     for j in range(6):
#         if i <= j:
#             result[i, j] = lin[i] * arr[j] + (i - j)
#         else:
#             result[i, j] = lin[i] + arr[j] - (i * j)

# # Print the result rounded to 2 decimal places
# print(np.round(result, 2))
# print(np.zeros((6, 6)))


"""let's say you have a list containing integers that are less than 10000 
but greater than 1, for eg: l=[2,8,3,100,10]. Write a code to sort this list 
without using any python built-in functions like sort, max, etc. 
You may use sorting algorithms but I don't want that, there is a beautiful way to do this."""

def custom_sort(lst):
    max_size = 10000  # Given constraint
    presence = [False] * max_size

    # Mark the presence of each number
    for num in lst:
        presence[num] = True

    # Retrieve the sorted list
    sorted_lst = [i for i in range(2, max_size) if presence[i]]
    
    return sorted_lst

# Example usage
l = [2, 8, 3, 100, 10]
sorted_l = custom_sort(l)
print(sorted_l)



