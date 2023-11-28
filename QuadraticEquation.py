'''Python program to find the roots of a quadratic equation'''

import math

a=float(input("Enter the First Cofficient Of the equation : "))
b=float(input("Enter the Second Cofficient Of the equation : "))
c=float(input("Enter the Third Cofficient Of the equation : "))

if (a!=0.0):
    d=(b*b)-a*c*4
    if (d==0.0):
        print("The Roots are real and equal!!")
        r=-b/(2*a)
        print("The Roots are" , r ,"and" , r)
    elif(d>0.0):
        print("The Roots are real and distinct!!")
        r1=(-b+(math.sqrt(d)))/(2*a)
        r2=(-b-(math.sqrt(d)))/(2*a)
        print("The Roots are" , r1 , "and" , r2)
    else:
        print("The Roots are complex!!")
        rp=-b/(2*a)
        ip=math.sqrt(-d)/(2*a)
        print("Complex Root 1 : " , rp, "+i" , ip)
        print("Complex Root 2 : " , rp, "-i" , ip)
else:
    print("Not An Qudratic Equation!!`!~")
