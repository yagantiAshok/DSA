

"""
Given an array of integers nums and an integer limit as the threshold value, 

find the smallest positive integer divisor such that upon dividing all the elements of the array by this divisor, 
the sum of the division results is less than or equal to the threshold value.

After dividing each element by the chosen divisor, take the ceiling of the result (i.e., round up to the next whole number).


"""



from math import ceil


def divisor___(nums,divisor):


    sum_divisor  = 0

    for i in range(len(nums)):

        sum_divisor = sum_divisor + ceil(nums[i]/divisor)

    
    return sum_divisor


def smallestDivisor(nums,limit):

    start = 1

    end = max(nums)

    small_divisor = None

    while start<=end:

        middle = start + (end-start)//2
        
        divisor_sum = divisor___(nums,middle)

        if (divisor_sum<=limit):

            small_divisor = middle

            end = middle - 1
        
        else:

            start = middle + 1

    return small_divisor



nums = [10,10,10,10,10]

print(smallestDivisor(nums,10))