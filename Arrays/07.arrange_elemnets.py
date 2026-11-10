

"375. Rearrange array elements by sign"

# def arrange_elemnts_by_sign(array):

#     positive_list = []
#     negative_list = []
#     result = []
#     for num in array:
#         if num>=0:
#             positive_list.append(num)
#         else:
#             negative_list.append(num)
#     for i in range(len(positive_list)):
#         result.append(positive_list[i])
#         result.append(negative_list[i])
#     return result
# res = arrange_elemnts_by_sign([2,3,4,-1,-8,-3])
# print(res)

def optimal_arrange_elemnts_by_sign(array):

    next_positive_index = 0
    next_negative_index = 1
    result = [0] * len(array)
    for num in array:
        if num>=0:
            result[next_positive_index] = num
            next_positive_index+=2
        else:
            result[next_negative_index] = num
            next_negative_index+=2
    return result
res = optimal_arrange_elemnts_by_sign([2,3,4,-2,-3,-4])
print(res)

    