
# bubble sort 

# def bubble_sort(array):

#     n = len(array)-1
#     for i in range(n):
#         is_sorted = True
#         for j in range(0,n-i):
#             if array[j]>array[j+1]:
#                 array[j],array[j+1] = array[j+1],array[j]
#                 is_sorted = False
#         if is_sorted:
#             return array
#     return array

# result = bubble_sort([10,12,9,7,0,13,20,-1,90,0,20,20])
# print(result)

"selction sort "

# def selection_Sort(array):

#     n = len(array)-1
#     for i in range(n):
#         min_element =  i
#         for j in range(i+1,n):
#             if array[j]<array[min_element]:
#                 min_element = j
#         if min_element!=i:
#             array[i],array[min_element] = array[min_element],array[i]
#     return array
# res = selection_Sort([10,12,9,7,0,13,20,-1,90,0,20,20])
# print(res)


# "insertion sort "
# def insertion_sort(array):

#     for i in range(1,len(array)):
#         index = i
#         while array[index]<array[index-1] and index>0:
#             array[index],array[index-1] = array[index-1],array[index]
#             index = index - 1
#     return array
# res = insertion_sort([10,12,9,7,0,13,20,-1,90,0,20,20])
# print(res)

"lower bound "

# def lower_bound(array,target):

#     lower_element = len(array)
#     start = 0
#     end = len(array)-1
#     while start<=end:
#         middle = start + (end-start)//2
#         if array[middle]>=target:
#             lower_element = middle
#             end = middle -1 
#         else:
#             start = middle + 1
#     return lower_element

# res = lower_bound([3,5,8,15,19],-1)
# print(res)


# "upper bound "

# def upper_bound(array,target):

#     upper = len(array)
#     start = 0
#     end = len(array) - 1
#     while start<=end:
#         middle = start + (end-start)//2
#         if array[middle]>target:
#             upper = middle
#             end = middle  - 1
#         else:
#             start = middle + 1
#     return upper
# res = upper_bound([2,3,4,5,6,7,10],-1)
# print(res)

