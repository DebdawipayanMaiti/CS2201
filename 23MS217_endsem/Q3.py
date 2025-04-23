# Importing necessary libraries
import numpy as np
import math
# Input the values by user
b = float(input("Please enter the expected load (in tons):  "))
l = float(input("Please enter a deck length you wish to try (in metres): "))
h = float(input("Please enter a tower height you wish to try (in metres): "))
# Defining the function for Analysis
def design_bridge(deck_length,tower_height):
    radius_arc = ((tower_height/2) + ((deck_length**2)/(8*tower_height)))  # Determining the radius
    theta = 2*(math.degrees(math.asin(deck_length/(2*radius_arc)))) # Angle swift by the arc
    arc_length = 2*math.pi*radius_arc*(theta/360)
    return arc_length
# Assigning a variable to the calculated arc length from the function
arc_length_calculated = design_bridge(l,h)
# Conditional checking
if ((arc_length_calculated)*1400) <= b:
    print("You need longer arc to bear the given load!!!")
else:
    print("You may go ahead with this design...")
    
# print(design_bridge(b,l,h))
