





def possible(nums,k,day):

    flowers = 0
    bouqets = 0

    for i in range(len(nums)):

        if nums[i]<=day:

            flowers+=1

            if flowers==k:

                bouqets+=1

                flowers = 0
        
        else:

            flowers = 0
    
    return bouqets


def bouqets(nums,k,m):

    start = 1

    end = max(nums)

    ans = -1

    while start<=end:

        day = start + (end-start)//2

        bouquets = possible(nums,k,day)

        if bouquets>=m:

            ans = day

            end = day - 1

        else:

            start = day + 1

    return ans 

nums = [1, 10, 3, 10, 2]

print(bouqets(nums,k=3,m=2))