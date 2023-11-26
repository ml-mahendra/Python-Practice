'''Python program to check whether the given integer is a prime number or not'''

num=int(input("Enter an integer : "))
isprime=1

for i in range(2,num//2):
    if(num%i==0):
        isprime=0
        break
if(isprime==1):
        print("Given number" , num , "is prime!!" )
else:
        print("Given number" , num , "is not prime..")

