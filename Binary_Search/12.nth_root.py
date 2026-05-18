


"""
Given two numbers N and M, find the Nth root of M. 
The Nth root of a number M is defined as a number X such that when X is raised to the power of N, it equals M. 
If the Nth root is not an integer, return -1.

"""


def nth_root(n,num):

    start = 0
    end = num

    Nt_root = -1

    while start<=end:

        middle = start + (end-start)//2

        if (middle)**n==num:

            return middle
        
        elif (middle)**n<num:

            start = middle + 1
        
        else:

            end = middle - 1

    return Nt_root




print(nth_root(5,3125))