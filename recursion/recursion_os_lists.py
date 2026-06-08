



# def sorted_or_not(array,index=0):

#     if len(array)==1:

#         return True 

#     if array[index]>array[index+1]:

#         return False
    
#     return sorted_or_not(array[index+1:])


# print(sorted_or_not([1,2,3,4,5]))




# def sorted_or_not(array,index=0):

#     if len(array)==1 or len(array) == 0:

#         return True 
    
#     ans  = sorted_or_not(array[index+1:])

#     if array[index]>array[index+1]:

#         ans = False
    
#     return ans 
    
    
    
# print(sorted_or_not([]))



# def sum_of_array(array,Index=0):

#     if len(array)==1:

#         return array[Index]
    
#     ans = array[Index] + sum_of_array(array[1:])

#     return ans 


# print(sum_of_array([1,2,3,4,5]))



# def sum_of_array(array,accumulator=0):

#     if len(array)==0:

#         return accumulator
    
#     accumulator = array[0] + accumulator
    
    
#     return sum_of_array(array[1:],accumulator)


# tail method
# def firstelementofindex(array, element, index=0):
#     if len(array) == 0:
#         return -1
    
#     if array[0] == element:
#         return index
    
#     return firstelementofindex(array[1:], element, index + 1)

# print(firstelementofindex([1,2,3,4,5,6],6))


# head method

# def firstelementofindex(array, element, index=0):
#     if len(array) == 0:
#         return -1
    
#     if array[0] == element:
#         return index
    
#     ans = firstelementofindex(array[1:], element, index + 1)

#     if array[0] == element:
       
#        ans  = array[0]

#     return ans 

# print(firstelementofindex([23,56,12,45,32],56))



# def updatelist(array,x,index,anslist):

#     if len(array)==index:

#         return anslist
    
#     if array[index]==x:

#         anslist.append(index)
    
#     updatelist(array,x,index+1,anslist)

# anslist = []

# print(updatelist([3,2,5,2,8,2,1],2,0,anslist=anslist))





# def sum_of_list(array):

#     if len(array)==0:

#         return 0
    
#     ans = sum_of_list(array[1:])

#     return ans + array[0]


# print(sum_of_list([1,2,3,4,5]))


# def sum_of_list(array,index,accumulator = 0 ):

#     if len(array)==index:

#         return accumulator
    
#     accumulator+=array[index]
    
#     return sum_of_list(array,index+1,accumulator)



# print(sum_of_list([1,2,3,4,5,100],0))


# def big_element_in_list(array,index):

#     if not array:

#         return None

#     if (len(array) - 1 == index): 

#         return array[index]
    
#     ans = big_element_in_list(array,index+1)

#     if array[index]>ans:

#         return array[index]
    
#     return ans 

# print(big_element_in_list([],0))



# def array_sorted_or_not(array,index):

#     if not array:

#         return True

#     if (len(array)-1 == index):

#         return True
    
#     if array[index]>array[index+1]:

#         return False
    
#     return array_sorted_or_not(array,index+1)


# print(array_sorted_or_not([1,2,3,4,5,6,70,1],0))


def last_occurence(array,value,index):

    if len(array) == index:

        return -1
    
    ans = last_occurence(array,value,index+1)

    if ans!=-1:

        return ans
    
    elif array[index] == value:

        return index
    
    return ans 


print(last_occurence([1,2,3,4,5,4,32,1],1,0))

