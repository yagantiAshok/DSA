

"""
A monkey is given n piles of bananas, where the 'ith' pile has nums[i] bananas. An integer h represents the total time in hours to eat all the bananas.



Each hour, the monkey chooses a non-empty pile of bananas and eats k bananas. If the pile contains fewer than k bananas, the monkey eats all the bananas in that pile and does not consume any more bananas in that hour.



Determine the minimum number of bananas the monkey must eat per hour to finish all the bananas within h hours.

"""

# import math

# def hours_per_pile(nums,middle):

#     hou_many_hours = 0

#     for i in range(len(nums)):

#         hou_many_hours = hou_many_hours + math.ceil(nums[i]/middle)

    
#     return hou_many_hours


# def kokobanana(nums,hours):

#     start = 1

#     end = max(nums)

#     ans = None

#     while start<=end:

#         middle = start + (end-start)//2

#         hour_per_pile = hours_per_pile(nums,middle)

#         if hour_per_pile <= hours:

#             ans = middle

#             end = middle  - 1
#         else:

#             start = middle + 1

#     return ans 
    
# reuslt = kokobanana(hours=7,nums=[8,7,3,2,100])

# print(reuslt)

def bouets(array,k,middle):

    bou = 0
    bloom = 0
    for day in array:

        if middle>=day:
            bloom = bloom + 1
            if bloom==k:
                bou = bou + 1
        else:
            bloom = 0
    return bou

def flowers(array,k,bou):

    ans = -1
    start = 1
    end = max(array)
    while start<=end:
        middle = start + (end-start)//2
        bou = flowers(array,k,middle)
        if bou>=bou:
            ans = middle
            end = middle - 1
        else:
            start = middle + 1
    return ans
