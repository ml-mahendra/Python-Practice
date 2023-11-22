# Python program to find the area of a triangle whose sides are given

import math
a=float(input("Enter side one : "))
b=float(input("Enter side two : "))
c=float(input("Enter side three : "))

s=(a+b+c)/2
area= math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area od the trianle whose sides are " , a , b , c , "is :" , area)