

# def floor(array,x):

#     start = 0

#     end = len(array) - 1

#     Floor  = -1 

#     while start <= end:

#         middle = start + (end-start)//2

#         if array[middle]<=x:

#             Floor = middle

#             start = middle + 1

#         else:

#             end = middle - 1

#     return Floor 

# def ceil(array,x):

#     start = 0

#     end = len(array) - 1

#     ceil  = -1 

#     while start <= end:

#         middle = start + (end-start)//2

#         if array[middle]>=x:

#             ceil = middle

#             end = middle - 1

#         else:

#             start = middle + 1

#     return ceil 

# array  = [3,4,4,4,4,4,7,8,10]

# x = 4

# floor_index = floor(array,x)
# ceil_index = ceil(array,x)

# floor_value = array[floor_index] if floor_index!=-1 else -1

# ceil_value = array[ceil_index] if ceil_index!=-1 else -1

# print(floor_value,ceil_value)




def floor_ceil(array,x):
    
    start = 0
    end = len(array)-1

    floor = -1

    ceil = -1

    while start<=end:

        middle = start + (end-start)//2

        if array[middle] == x:

            floor = middle

            ceil = middle

            return [array[floor],array[ceil]]
        
        elif array[middle]<x:

            floor = middle

            start = middle + 1
        
        elif array[middle]>x:

            ceil = middle

            end = middle - 1

    floor = array[floor] if floor!=-1 else -1

    ceil = array[ceil] if ceil!=-1 else -1

    return [floor, ceil]


result = floor_ceil([3,5,7,9,10,12,15],20)

print(result)