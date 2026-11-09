

"512. Leaders in an Array"

# def leaders(array):

#     leaders = []
#     n = len(array)
#     for index in range(n):
#         i  = index + 1
#         while i<n:
#             if array[index]>array[i]:
#                 i+=1
#             else:
#                 break
#         if i == n:
#             leaders.append(array[index])
#     return leaders
# res = leaders( [-3, 4, 5, 1, -4, -5])
# print(res)

def leaders_optimal(array):

    if len(array)==0:
        return []
    n = len(array) - 1
    leaders = []
    max_right = array[n]
    leaders.append(array[n])
    for i in range(1,n+1):
        if array[n-i]>max_right:
            leaders.append(array[n-i])
            max_right = array[n-i]
    left = 0
    right = len(leaders) - 1
    while left<right:
        leaders[left],leaders[right] = leaders[right], leaders[left]
        left+=1
        right-=1
    return leaders
res = leaders_optimal([1])
print(res)    
