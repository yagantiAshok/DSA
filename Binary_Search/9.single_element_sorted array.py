

"""
Given an array nums sorted in non-decreasing order. Every number in the array except one appears twice. 
Find the single number in the array.

"""

def single_element_sorted_array(array):

    start = 0
    end = len(array) - 1

    while start < end:

        middle = start + (end-start)//2

        if middle%2==1:

            middle = middle - 1

        if array[middle]==array[middle+1]:

            start = start + 2
        
        else:

            end = middle

    return array[end]


print(single_element_sorted_array([1,1,2,2,3,3,4,5,5,6,6]))



