
'''Python program to find the geometric mean of n numbers'''

c=0
product=1.0
count=int(input("Enter the count of numbers :"))
while(c<count):
    x=float(input("Enter the numbers : "))
    c=c+1
    product=product*x
gm=pow(product,1.0/count)
print("The Gometric mean fo the given numbers is : " , gm)


