'''Python program to generate prime number the upto N  numbers'''

n=int(input("Enter the value of N : "))
for num in range(2,n+1):
    k=0
    for i in range(2,num//2+1):
        if(num%i==0):
            k=k+1
    if (k<=0):
         print(num)