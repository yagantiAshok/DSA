


# def binary_search(arr,target):



#     start = 0

#     end = len(arr) - 1


#     while end >= start:

#         middle = start + (end-start)//2


#         if arr[middle]==target:

#             return middle 

#         elif arr[middle]<target:

#             start = middle + 1

#         elif arr[middle]>target:

#             end = middle - 1

#     return -1


# elements = [3,5,7,8,20,19,20,24,25,30]

# target = 0

# result = binary_search(elements,target)

# print(result)


### first occurance 


# def first_occurance(arr,tar):

#     start = 0

#     end = len(arr) - 1

#     first_occurance = -1

#     while start <= end:

#         middle = start + (end-start)//2

#         if arr[middle]==tar:

#             first_occurance = middle

#             end = middle - 1

#         elif arr[middle]<tar:

#             start = middle + 1

#         elif arr[middle]>tar:

#             end = middle -1

#     return first_occurance


# def last_occurance(arr,tar):

#     start = 0

#     end = len(arr) - 1

#     last_occurance = -1

#     while start <= end:

#         middle = start + (end-start)//2

#         if arr[middle]==tar:

#             last_occurance = middle

#             start = middle + 1

#         elif arr[middle]<tar:

#             start = middle + 1

#         elif arr[middle]>tar:

#             end = middle -1

#     return last_occurance


# arr = [2,2]

# tar = 2

# result = [first_occurance(arr,tar),last_occurance(arr,tar)]

# print(result)

def find_boundry(arr,tar,first_occurrence=True):

    start = 0

    end = len(arr) - 1

    boundry = -1

    while start <= end:

        middle = start + (end-start)//2


        if arr[middle]==tar:

            boundry = middle

            if first_occurrence:

                end = middle - 1
            else:

                start = middle + 1

            

        elif arr[middle]<tar:

            start = middle + 1

        else:

            end = middle -1

    return boundry


arr = [1,1,1,1,2,2,2,2,2,2,2]

tar = 0

result = find_boundry(arr,tar,first_occurrence=False)

print(result)