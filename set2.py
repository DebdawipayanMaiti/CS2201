# word = "mitochondria"
# for i in range(len(word), 0, -1):
#     print(word[:i])


# elements = ["sodium", "potassium", "calcium", "magnesium", "chlorine", "argon"]
# longest_name = max(elements, key=len)
# print("The longest element name is '{}' with length {}".format(longest_name, len(longest_name)))

# full_name = input("Enter your full name: ")
# name_parts = full_name.split()
# abbreviated_name = ". ".join([name[0] for name in name_parts[:-1]]) + ". " + name_parts[-1]
# print(abbreviated_name)



# fib = [1, 1]
# for i in range(2, 10):
#     fib.append(fib[-1] + fib[-2])
# print(fib)


# n = 50
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()


# n = 5
# for i in range(1, n+1):
#     for j in range(1, 2*i, 2):
#         print(j, end=" ")
#     print()


# n = 5
# for i in range(n, 0, -1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# n = 5
# for i in range(1, n+1):
#     print(" " * (i-1), end="")
#     for j in range(i, n+1):
#         print(j, end=" ")
#     for j in range(n-1, i-1, -1):
#         print(j, end=" ")
#     print()



# # Dictionary of user ID: password pairs
# users = {"user1": "password1", "user2": "password2", "user3": "password3"}

# # Part (i): Check user credentials
# user_id = input("Enter your user ID: ")
# if user_id in users:
#     password = input("Enter your password: ")
#     if users[user_id] == password:
#         print("Welcome to the portal!")
#     else:
#         print("Invalid credentials!")
# else:
#     print("Invalid credentials!")



# # Dictionary of user ID: password pairs
# users = {"user1": "password1", "user2": "password2", "user3": "password3"}

# # Part (ii): Password change service
# user_id = input("Enter your user ID for password change: ")
# if user_id in users:
#     new_password1 = input("Enter your new password: ")
#     new_password2 = input("Re-enter your new password: ")
    
#     if new_password1 == new_password2 and new_password1 != users[user_id]:
#         users[user_id] = new_password1
#         print("Password changed successfully!")
#     else:
#         print("Passwords do not match or are the same as the current password.")
# else:
#     print("Invalid username!")
