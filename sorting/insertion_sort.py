


# def inserton_sort(array):

#     for i in range(1,len(array)):

#         insert = i

#         for __ in range(i):

#             if array[insert]<array[insert-1]:

#                 array[insert],array[insert-1]=array[insert-1],array[insert]

#                 insert = insert-1

#             else:

#                 break
    
#     return array


# result = inserton_sort([100,10,0,-1,444,4,4,4])

# print(result)


# while loop 
def inserton_sort(array):

    for i in range(1,len(array)):

        insert = i

        while  array[insert]<array[insert-1] and insert>0:

                array[insert],array[insert-1]=array[insert-1],array[insert]

                insert = insert-1
    
    return array

result = inserton_sort([100,10,0,-1,444,4,4,4])

print(result)