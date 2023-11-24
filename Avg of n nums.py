'''Python program to find the average of n numbers using while loop'''

n = int(input("Enter the No of Integers:"))
count=0
sum=0.0
while(count<n):
    number=float(input("Enter the number : "))
    count=count+1
    sum=sum+number
avg=sum/count
print("Average of the 10 numbers : " , avg)


