

# tailend
# def linearsearcrecursion(array,target,index=0):

#     if len(array)==index:

#         return False 
    
#     if array[index]==target:

#         return True
    
#     return linearsearcrecursion(array,target,index+1)


# print(linearsearcrecursion([13,26,19,67,0,1,23,1],0))


def linearsearcrecursion(array,target,index=0):

    if len(array)==index:

        return False 

    ans = linearsearcrecursion(array,target,index+1)

    
    if array[index]==target:

        ans = True
    
    return ans 
    


print(linearsearcrecursion([13,26,19,67,0,1,23,1],0))