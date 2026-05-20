

"""
A monkey is given n piles of bananas, where the 'ith' pile has nums[i] bananas. An integer h represents the total time in hours to eat all the bananas.



Each hour, the monkey chooses a non-empty pile of bananas and eats k bananas. If the pile contains fewer than k bananas, the monkey eats all the bananas in that pile and does not consume any more bananas in that hour.



Determine the minimum number of bananas the monkey must eat per hour to finish all the bananas within h hours.

"""

import math

def hours_per_pile(nums,middle):

    hou_many_hours = 0

    for i in range(len(nums)):

        hou_many_hours = hou_many_hours + math.ceil(nums[i]/middle)

    
    return hou_many_hours


def kokobanana(nums,hours):

    start = 1

    end = max(nums)

    ans = None

    while start<=end:

        middle = start + (end-start)//2

        hour_per_pile = hours_per_pile(nums,middle)

        if hour_per_pile <= hours:

            ans = middle

            end = middle  - 1
        else:

            start = middle + 1

    return ans 
    
reuslt = kokobanana(hours=7,nums=[8,7,3,2,100])

print(reuslt)