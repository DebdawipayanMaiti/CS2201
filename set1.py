##Lists
#  x=list(range(10))
#  print(x)
#  y=list(range(3,13))
#  print(y)
#  print(y[-1])
#  print(y[::-1])
#  print(x[1::2] and y[0::2])
# print(x[3]==y[0])
# print(x.index(10))
# print(y.index(7))
# z=x+y
# print(x+y)
# print(max(z))
# print(min(z))


##Strings are lists
# x="The quick brown fox jumps over the lazy dog"
# print(x[::-1])
# print(x[::4])
# print(x[::5])
# print(len(x))
# print(x[::-2])
# y=x[0:4]
# z=x[-1:-3]   
# print(y)
# print(z)
# print(y*10)


##Misc
# print("Hello World!")
# #I am commenting for a joke.
# name="Debdawipayan Maiti"
# age="18"

# rollnumber="23MS217"
# #print("My name is" + name + "I am " + age +" years old". "My roll number is"+ rollnumber.)

# x=input("enter your string: ")
# y=input("enter your string: ")
# print(x+y)

# x=input("enter your integer: ")
# y=input("enter your integer: ")
# print(int(x)+int(y))

#print("It's good to learn Python")
#print("The man asked,Where to meet you? I said, Well, use Google Meet")



# x=6
# y=3.6
# z="Deb"
# print(type(x))
# print(type(y))
# print(type(z))

# x=input('Give your namer: ' )
# print('My name is' + 'x')




#Range is not used for List

# def common_element(x,y):
#     for i in range(x):
#         for j in range(y):
#             if i==j:
#                 print('True')
#             else:
#                 print('False')
    
# L= ['p','y','t']    
# L= '-'.join(L)
# print (L) 

# List=[1, 1, 2, 3, 4, 4, 5, 1]
# List.remove(2)
# print(List)



def have_common_member(list1, list2):
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                return True
    return False

list_a = [1, 2, 3, 4]
list_b = [4, 5, 6, 7]
list_c = [8, 9, 10]

print(have_common_member(list_a, list_b))  
print(have_common_member(list_a, list_c))  