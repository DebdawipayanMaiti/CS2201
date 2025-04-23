# method:-1
# importing the libraries
import math
import numpy as np
# input take for height ,radius and volume
h = float(input("Enter the height of the object in cm: "))
r = float(input("Enter the radius of the object in cm: "))
v = float(input("Enter the volume of the object in ml: "))
# x = 1/3*math.pi*r**2*h
# y = math.pi*r**2*h
# print(y)
# checking using ceil function
if v == np.ceil(1/3*math.pi*r**2*h):
    print("This is a cone!")
elif v == np.ceil(math.pi*r**2*h):
    print("This is a cylinadar!")
else:
    print("This is not a cone and not cylindar.")
    
    
    
# method:-2
# checking using error not greater than 0.5
import math
import numpy as np
h = float(input("Enter the height of the object in cm: "))
r = float(input("Enter the radius of the object in cm: "))
v = float(input("Enter the volume of the object in ml: "))
volume_cone = 1/3*math.pi*r**2*h
volume_cylindar = math.pi*r**2*h
if abs(volume_cone - v) < 0.5:
    print("This is a cone!")
elif abs(volume_cylindar - v) < 0.5:
    print("This is a cylindar!")
else:
    print("Not a cone and also not a cylindar!")
    
