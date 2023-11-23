'''6. Python program to find the circumference and area of a circle with a given radius'''
import math
radius=float(input("Enter the radius of circle : "))
circumference=2*radius*(math.pi)
area=(math.pi)*radius**2

print("Circumference of the circle is : " , '%.2f'%circumference)
print("area of the circle is " , '%.2f'%area)