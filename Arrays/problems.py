
# "Linear search "
# def linear_search(array,target):

#     for index in range(len(array)):
#         if array[index]==target:
#             return index
#     return -1

# result  = linear_search([2,6,1,5,1,-1],0)
# print(result)

# array = [2,3,4,1,3]
# tar = 7
# l = len(array)
# index = 0

# while index<l:
#     if array[index]==tar:
#         print(index)
#         break
#     index = index + 1
# else:
#     print(-1)


# "Lagest element"
# def largest_element(array):

#     if len(array)==0:
#         return None
#     largest = array[0]
#     for index in range(1,len(array)):
#         if largest<array[index]:
#             largest = array[index]
#     return largest
# res = largest_element([])
# print(res)

"Second largest"
# def second_largest(array):

#     f_lar = float("-inf")
#     s_lar = float("-inf")

#     for index  in range(len(array)):
#         if f_lar<array[index]:
#             s_lar = f_lar
#             f_lar = array[index]

#         elif array[index]<f_lar and array[index]>s_lar:
#             s_lar = array[index]
#     if s_lar==array[0]:
#         return -1
#     return s_lar

# res = second_largest([-10,-5,-20])
# print(res)


# "213. Maximum Consecutive Ones"
# def max_consecutive(array):

#     max_cons = 0
#     cum_cons = 0
#     for index in range(len(array)):
#         if array[index]==1:
#             cum_cons+=1
#             if cum_cons>max_cons:
#                 max_cons = cum_cons
#             # max(max_cons,cum_cons)
#         else:
#             cum_cons = 0
#     return max_cons
# res = max_consecutive([1,1,1,1,1,1])
# print(res)



# "832. Left Rotate Array by One"
# def rotate_by_one(array,k):

#     if len(array)==0 or len(array)==1:
#         return array
#     num = 0
#     first_element = array[0]
#     while num<k:
#         for index in range(1,len(array)):
#             array[index-1] = array[index]
#             # array[index] = first_element
#         array[-1] = first_element
#         first_element = array[0]
#         num = num + 1
#     return array
        
# res = rotate_by_one([1,2,3,4,5],5)
# print(res)

"Given an integer array nums of size n, return the majority element of the array."


# def majority_elements(array):

#     data = {}
#     for num in array:
#         if num in data:
#             data[num] = data[num] + 1
#         else:
#             data[num] = 1
#     target = max(data.values())
#     key = next((k for k,v in data.items() if v == target))
#     return key
# res = majority_elements([3,4,1,1,1,1,1,1,1,7,5])
# print(res)


# gen = (x*10 for x in [1,2,3])
# print(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

"248. Move Zeros to End"

def move_zeroes(array):

    n = len(array)
    for index in range(n):
        if array[index]==0:
            for new_index in range(index+1,n):
                array[new_index-1] = array[new_index]
            array[-1] = 0
    return array
res = move_zeroes([1,2,3,0,6,7,8])
print(res)


























