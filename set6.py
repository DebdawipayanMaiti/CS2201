# L = input("Enter elements separated by space: ").split()

# # Covert to list
# print("List:", L)
# result_dict = {L[i]: L[i + 1] for i in range(0, len(L), 2)}
# print('dict: ',result_dict)


# # Convert to tuple 
# result_tuple = [(L[i],L[i + 1]) for i in range(0, len(L), 2)]
# print('tuple: ',result_tuple)





import numpy as np
# a=np.array([[1,2,3],[4,8,66],[7,81,9]])
# b=np.array([2,3,4])
# print(abs(np.linalg.det(a)))
# print(np.linalg.inv(a).dot(b)) 
# print(np.linalg.solve(a, b))



# marks_array = np.array([[50, 60, 70], [67, 88, 90], [60, 78, 97]])
# a=np.sum(marks_array,axis=1)
# b=np.sum(marks_array,axis=0)
# print(a) # rowwise=>sum of mark of each student in all subjects
# print(b) # columnwise=>sum of marks of one subject in of all students
# print(np.dstack((a,b)))
# print(np.hstack((a,b)))
# print(np.concatenate(a,b,axis=0))



def d2b(a):
    if int(a) >= 1:
        d2b(int(a)//2)
    print(int(a)%2,end='')
    return " Binary at side"

a=input("Enter the number to convert decimal to binary: ")
print(d2b(a))



import numpy as np

# Creating the 2D numpy array
marks = np.array([[50, 60, 70], [67, 88, 90], [60, 78, 97]])

# Sum of marks of individual students (1D and 2D)
student_sums_1D = np.sum(marks, axis=1)
student_sums_2D = np.sum(marks, axis=1, keepdims=True)

# Sum of subject-wise marks (1D and 2D)
subject_sums_1D = np.sum(marks, axis=0)
subject_sums_2D = np.sum(marks, axis=0, keepdims=True)

# Set operation to remove common elements
A = np.array([1, 2, 3, 4, 5])
B = np.array([3, 4])
C = np.setdiff1d(A, B)

#np.multiply and np.matmul
arr1 = np.array([[1, 2], [4, 5]])
arr2 = np.array([[3, 3], [1, 1]])

elementwise_mult = np.multiply(arr1, arr2)
matrix_mult = np.matmul(arr1, arr2)

# Applying function f(x) = x^3 + 1 on a list and numpy array
L = [1, 2, 3, 4]
f = lambda x: x**3 + 1
Lout = [f(x) for x in L]

A = np.array(L)
Aout = f(A)

print(student_sums_1D, student_sums_2D)
print(subject_sums_1D, subject_sums_2D)
print(C)
print(elementwise_mult)
print(matrix_mult)
print(Lout)
print(Aout)



import numpy as np

# Function definition
def f(x):
    if x < 0:
        return 0
    elif x == 0:
        return 1
    else:
        return x % 3

# Creating a sample numpy array
X = np.array([-5, -1, 0, 1, 3, 4, 9])

# Using frompyfunc
f_frompyfunc = np.frompyfunc(f, 1, 1)
result_frompyfunc = f_frompyfunc(X)

# Using vectorize
f_vectorized = np.vectorize(f)
result_vectorized = f_vectorized(X)

# Generating equispaced points
points_a = np.linspace(20, 21, 10, endpoint=True)
points_b = np.linspace(20, 21, 10, endpoint=False)
interval_length_a = points_a[1] - points_a[0]

print(result_frompyfunc)
print(result_vectorized)
print(points_a)
print(points_b)
print(interval_length_a)



