'''Python program to find the factorial of a number using recursion'''

def factorial(n):
    if(n==1):
        return 1
    else:
        fact=n*factorial(n-1)
    return fact

num=int(input("Enter the number to find factorial : "))

res=factorial(num)
print("The Factorial of given number " , num , "is" , res)