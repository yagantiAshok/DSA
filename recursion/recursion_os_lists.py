



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



# print(sum_of_array([1,2,3,4,5]))


