



"""
You are given an array weights where weights[i] represents the weight of the i-th package on a conveyor belt.

All the packages must be shipped in the order given from one port to another within days days.

Each day, the ship can carry a contiguous sequence of packages, as long as the total weight does not exceed its maximum capacity.

Your task is to find the minimum possible capacity of the ship so that all packages can be shipped within the given number of days.
"""

def days__(weights,capacity):

    day = 0

    weight = 0


    for i in range(len(weights)):

        weight = weight + weights[i]

        if weight==capacity:

            weight = 0

            day+=1
        
        elif weight>capacity:

            weight = weights[i]

            day+=1

    if weight!=0:

        day+=1
    

    return day



def capacity_to_ship(weights,days):

    start = max(weights)

    end = sum(weights)

    min_capacity = 0

    while start<=end:

        middle = start + (end-start)//2

        capacity = days__(weights,middle)

        if capacity<=days:

            min_capacity = middle

            end = middle - 1
        
        else:

            start = middle + 1
    
    return min_capacity


l1  = [3, 2, 2, 4, 1, 4]

print(capacity_to_ship(l1,3))