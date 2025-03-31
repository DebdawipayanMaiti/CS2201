# A = np.array([int(input(f"Enter element A[{i+1}, {j+1}]: ")) for i in range(4) for j in range(4)]).reshape(4, 4)
# B = np.array([
#     A[:2, :2],   
#     A[:2, 2:],  
#     A[2:, :2],   
#     A[2:, 2:]    
# ])
# print("3-D array B:\n", B)
# print("Shape of B:", B.shape)


# A = np.array([int(input(f"Enter element A[{i+1}, {j+1}]: ")) for i in range(3) for j in range(3)]).reshape(3, 3)
# B = np.array([int(input(f"Enter element B[{i+1}, {j+1}]: ")) for i in range(3) for j in range(3)]).reshape(3, 3)
# A[::2, ::2] = B[::2, ::2]
# print("Updated matrix A:\n", A)


# matrix = np.array([int(input(f"Enter element [{i+1}, {j+1}]: ")) for i in range(3) for j in range(3)]).reshape(3, 3)
# print("Last 2 columns:\n", matrix[:, -2:])
# print("First 2 rows:\n", matrix[:2, :])
# max_val = np.max(matrix)
# matrix[1:2, 1:2] = max_val
# print("Updated matrix:\n", matrix)


# arr = np.array([int(input(f"Enter element {i+1}: ")) for i in range(9)])
# print("Last 3 elements:", arr[-3:])
# print("First 3 elements:", arr[:3])
# print("Middle 3 elements:", arr[3:6])
# print("5th-last to 2nd-last element:", arr[-5:-1])
# arr[1::2] = 0
# print("Updated array:", arr)

# import numpy as np
# arr = np.array([int(input(f"Enter element {i+1}: ")) for i in range(9)])
# print("Reversed array:", arr[::-1])



