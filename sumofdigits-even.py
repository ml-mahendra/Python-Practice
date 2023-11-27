'''Python program to display all integers within the range a & b whose sum of digits is an even number'''

a = int(input("Enter the Lower Range:"))
b = int(input("Enter the Lower Range:"))

for i in range(a,b):
    num=i
    sum=0
    while(num!=0):
        digit=num%10
        sum=sum+digit
        num=num//10
    if(sum%2==0):
        print(i)
