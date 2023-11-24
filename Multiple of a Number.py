''' Python program to check whether the given integer is a multiple of a number'''

num1=int(input("Enter the  Integer: "))

num2=int(input("Is the integer is multiple of (Give the interger you wanna check):"))

if (num1%num2==0):
    print("Yes, Given Number" , num1 , "is multiple of", num2)
else:
    print("No, Given Number" , num1 , "is not multiple of", num2)