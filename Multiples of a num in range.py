''' Python program to display all the multiples of a number within the range a and b'''

number = int(input("Enter the number:"))

a = int(input("Enter the lower range:"))
b= int(input("Enter the upper range:"))
for i in range(a,b):
   if(i%number==0):
        print(i)