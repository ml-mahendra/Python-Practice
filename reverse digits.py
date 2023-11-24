''' Python program to display the given integer in reverse manner'''

inp=int(input("Enter the number:"))
rev=0
while(inp!=0):
    digit=inp%10
    rev=(rev*10)+digit
    inp=inp//10
    
print("Reverse Order of the Number is: ", rev)