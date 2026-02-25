"""
author: Jason
date: 2026-02-24
area and perimeter calculations for a circle, rectangle, and pentagon

"""
# Input
radius = int(input("Please enter the radius of the circle: "))
length = int(input("Please enter the length of the rectangle: "))
width = int(input("Please enter the width of the rectangle: "))
side_length = int(input("Please enter the side length of the octagon: "))
# Processing
import math
area_circle = A = 3.14159*radius**2
perimeter_circle = P = 2*3.14159*radius

area_rectangle = A = length*width
perimeter_rectangle = P = 2*length + 2*width

area_octagon = A=2*(1+math.sqrt(2))*side_length**2
perimeter_octagon = P = 8*side_length

# Output
print("The area of the circle is: ", area_circle)
print("The perimeter of the circle is: ", perimeter_circle)

print("The area of the rectangle is: ", area_rectangle)
print("The perimeter of the rectangle is: ", perimeter_rectangle)

print("The area of the octagon is: ", area_octagon)
print("The perimeter of the octagon is: ", perimeter_octagon)