# -*- coding: utf-8 -*-
"""

@author: Mahendra Nath Reddy E

"""



# Method - 1

def swap_case(s):
    str = s.swapcase()
    return str


# Method - 2
    
"""
def swap_case(s):
    str=""
    for i in s:
        if str(i).islower():
            i=str(i).capitalize()
            #print(i)
        elif str(i).isupper():
            i=str(i).lower()
            #print(i)
        else:
            i=i
        str+=i
    return str

"""
# Method - 3

"""
def swap_case(s):
     
    string = ''

    for i in s:

        if i.isupper() == True:
            string += i.lower()

        elif i.islower() == True:
            string += i.upper()

        elif i.isspace() == True:  
            string += i

        elif i.isdigit() == True:
            string += i

        elif i.isalnum() == False:
            string += i

    return string

"""

# Main Function
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    

    
    
