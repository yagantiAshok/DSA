

"""
Given a positive integer n. Find and return its square root. 
If n is not a perfect square, then return the floor value of sqrt(n).

"""

def squarerootnumber(num):

    start = 0

    end = num

    value = None

    while start <= end:

        middle = start + (end-start)//2

        if (middle)**2 <= num:

            value = middle

            start = middle + 1
        
        else:

            end = middle - 1
    
    return value

print(squarerootnumber(100))