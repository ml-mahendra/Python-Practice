
'''4. Python program to find out the average of a set of integers'''

integres=int(input("Enter the count of numbers"))

sum=0
i=0

for i in range(integres):
    x=int(input("Enter the integer:"))
    sum=sum+x
avg=sum/integres
print("Average of given numbers is : " , avg)